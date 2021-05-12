from typing import Tuple

import pygame as pg

import config
import controller
import generator
import main_menu
import music
import option
import pause_menu
from event import event as event_store
from loaders.load_game_over import load_game_over
from loaders.load_in_game import load_in_game
from loaders.load_main_menu import load_main_menu
from loaders.load_option_menu import load_option_menu
from spec import spec
from sprites import bone, heart, game_over
from sprites_group import obstacles_group, character_group, gameplay_group, misc_group, pause_menu_group

BLACK = (0, 0, 0)
collision_list = []


def prep_for_new_render():
    game_controller = controller.get_game_controller()
    last_sprite = game_controller.get_last_sprite()
    if not game_controller.allow_new_render:
        return
    if last_sprite.is_outside:
        return
    if spec.current_specs["type"] != "attack":
        pg.time.set_timer(event_store.event["LOAD_BONE"]["object"], spec.current_specs["start_time"], True)
        game_controller.block_render()
    else:
        if len(obstacles_group.sprites()) == 0:
            pg.event.post(event_store.event["ATTACK_SANS"]["object"])
            game_controller.block_render()


def is_in_collision_list(bone_id):
    global collision_list
    sprite: bone.Bone
    for sprite in collision_list:
        if sprite == bone_id:
            return True
    return False


def check_for_collision():
    if len(obstacles_group.sprites()) == 0:
        collision_list.clear()
        return
    obstacle: bone.Bone
    for obstacle in obstacles_group.sprites():
        if obstacle.collided and not is_in_collision_list(obstacle.id):
            collision_list.append(obstacle.id)
            controller.game_controller.get_player().decrement_health()


def load_config(screen_center: Tuple[int, int]):
    bone.load_bone_image()
    heart.load_heart_image()
    heart_size = (int(heart.heart_image.get_width() * 0.1), int(heart.heart_image.get_height() * 0.1))
    config.set_heartsize(heart_size)
    config.set_screen_center(screen_center)
    # music.mute_bgm()


def map_event():
    event_store.define_event("START_GAME")
    event_store.define_event("MAIN_MENU")
    event_store.define_event("OPTION_MENU")
    event_store.define_event("IN_GAME")
    event_store.define_event("GAME_OVER")
    event_store.define_event("PAUSE")
    event_store.define_event("UNPAUSE")
    event_store.define_event("LOAD_BONE")
    event_store.define_event("ATTACK_SANS")
    event_store.define_event("ALLOW_NEW_CLOUD")
    event_store.define_event("ALLOW_NEW_ITEM")


def key_handling(key: int):
    game_controller = controller.get_game_controller()
    if key == pg.K_ESCAPE:
        if game_controller.is_paused():
            game_controller.unpause_game()
            music.unpause_music()
        else:
            pause_menu_sprite = pause_menu.Menu()
            pause_menu_group.add(pause_menu_sprite)
            pause_menu_group.update()
            game_controller.pause_game()
            music.pause_music()


def click_handling():
    game_controller = controller.get_game_controller()
    if game_controller.is_paused():
        pause_menu_sprite: pause_menu.Menu = pause_menu_group.sprites()[0]
        if pause_menu_sprite.is_clicked_on_resume():
            game_controller.unpause_game()
            music.unpause_music()
        if pause_menu_sprite.is_clicked_on_quit():
            game_controller.quit()
    if game_controller.is_at_main_menu():
        main_menu_sprite: main_menu.Menu = misc_group.sprites()[1]
        if main_menu_sprite.is_play_title_clicked():
            game_controller.display_game()
            pg.event.post(event_store.event["IN_GAME"]["object"])
        if main_menu_sprite.is_quit_title_clicked():
            game_controller.quit()
        if main_menu_sprite.is_option_title_clicked():
            pg.event.post(event_store.event["OPTION_MENU"]["object"])
    if game_controller.is_at_game_over():
        game_over_sprite: game_over.Menu = misc_group.sprites()[0]
        if game_over_sprite.is_clicked_on_back():
            game_controller.display_main_menu()
            load_main_menu(config.screen_center)
    if game_controller.is_at_option_menu():
        option_menu_sprite: option.Menu = misc_group.sprites()[0]
        if option_menu_sprite.is_clicked_on_bgm():
            music.toggle_bgm()
            config.toggle_bgm()
        if option_menu_sprite.is_clicked_on_sfx():
            config.toggle_sfx()
        if option_menu_sprite.is_clicked_on_back():
            game_controller.display_main_menu()
            load_main_menu(config.screen_center)


def init_game():
    pg.init()
    pg.font.init()
    pg.display.set_caption("Final Tale")
    controller.init_game_controller()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    return screen, clock


def main():
    screen, clock = init_game()
    game_controller = controller.get_game_controller()
    game_controller.display_main_menu()

    screen_center = (screen.get_width() / 2, screen.get_height() / 2)

    load_config(screen_center)
    map_event()
    load_main_menu(screen_center)
    pg.display.flip()

    while game_controller.is_game_running():
        screen.fill(BLACK)
        events = pg.event.get()

        for event in events:
            if event.type == pg.KEYDOWN:
                key_handling(event.key)
            if event.type == pg.MOUSEBUTTONUP:
                click_handling()
            if event.type == pg.QUIT:
                game_controller.quit()
            if event.type == event_store.event["IN_GAME"]["value"]:
                load_in_game(screen_center)
            if event.type == event_store.event["LOAD_BONE"]["value"]:
                generator.generate_sprites((screen_center[0] + 400, screen_center[1] + 200))
            if event.type == event_store.event["OPTION_MENU"]["value"]:
                load_option_menu()
            if event.type == event_store.event["ALLOW_NEW_CLOUD"]["value"]:
                game_controller.allow_new_cloud()
            if event.type == event_store.event["ALLOW_NEW_ITEM"]["value"]:
                game_controller.allow_new_item()
            if event.type == event_store.event["GAME_OVER"]["value"]:
                game_controller.display_game_over()
                load_game_over(screen_center, screen)
            if event.type == event_store.event["ATTACK_SANS"]["value"]:
                print("ATTACK")
        if game_controller.is_at_game_over():
            misc_group.draw(screen)
            spec.reset_spec_index()
            game_controller.allow_render()
        if game_controller.is_at_main_menu() or game_controller.is_at_option_menu():
            misc_group.draw(screen)
            gameplay_group.draw(screen)
            gameplay_group.update()
            misc_group.update()
        if game_controller.game_loaded and game_controller.is_in_game():
            if game_controller.is_paused():
                pause_menu_group.draw(screen)
            else:
                misc_group.draw(screen)
                if game_controller.is_new_cloud_allowed():
                    generator.gen_cloud()
                if game_controller.is_new_item_allowed():
                    generator.gen_item()
                character_group.draw(screen)
                obstacles_group.draw(screen)
                gameplay_group.draw(screen)
                character_group.update()
                obstacles_group.update()
                gameplay_group.update()
                misc_group.update()
                check_for_collision()
                prep_for_new_render()
                # if spec.specs_index == spec.get_specs_length() - 1 and len(obstacles_group.sprites()) == 0:
                #     spec.reset_spec_index()
                #     game_controller.allow_render()
                #     generator.generate_sprites((screen_center[0] + 400, screen_center[1] + 200))
        pg.display.update()
        clock.tick(120)


if __name__ == "__main__":
    main()
