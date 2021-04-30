from typing import Tuple

import pygame as pg

import bone
import border
import clock as internal_clock
import config
import controller
import generator
import heart
import main_menu
import music
import sans
from sprites_group import obstacles_group, character_group, gameplay_group, misc_group, pause_menu_group
import title
from spec import spec
from event import event as event_store
import pause_menu

BLACK = (0, 0, 0)
collision_list = []


def prep_for_new_render():
    game_controller = controller.get_game_controller()
    last_sprite = game_controller.get_last_sprite()
    if not game_controller.allow_new_render:
        pg.event.clear()
        return
    if last_sprite.is_outside:
        return
    pg.time.set_timer(event_store.event["LOAD_BONE"], spec.current_specs["start_time"], True)
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


def map_event():
    event_store.define_event("START_GAME")
    event_store.define_event("MAIN_MENU")
    event_store.define_event("IN_GAME")
    event_store.define_event("END_GAME")
    event_store.define_event("PAUSE")
    event_store.define_event("UNPAUSE")
    event_store.define_event("LOAD_BONE")


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
            print("RESUME")
            game_controller.unpause_game()
            music.unpause_music()
        if pause_menu_sprite.is_clicked_on_quit():
            game_controller.quit()
    if game_controller.is_at_main_menu():
        print("AT MAIN MENU")
        main_menu_sprite: main_menu.Menu = misc_group.sprites()[1]
        if main_menu_sprite.is_play_title_clicked():
            game_controller.display_game()
            pg.event.post(event_store.event["IN_GAME"])


def load_in_game(screen_center: Tuple[int, int]):
    spec.load_specs()

    sans_sprite = sans.Sans((screen_center[0], screen_center[1] - 100))
    border_sprite = border.Border(screen_center)

    generator.generate_sprites((screen_center[0] + 400, screen_center[1] + 200))
    character_group.add(sans_sprite)
    misc_group.add(border_sprite)

    character_group.update()
    misc_group.update()


def load_main_menu(screen_center: Tuple[int, int]):
    heart_sprite = heart.Heart(screen_center)
    title_sprite = title.Title(screen_center)
    main_menu_sprite = main_menu.Menu()

    gameplay_group.add(heart_sprite)
    misc_group.add(title_sprite)
    misc_group.add(main_menu_sprite)

    gameplay_group.update()
    misc_group.update()


def main():
    pg.init()
    pg.font.init()
    pg.display.set_caption("Final Tale")
    music.play_menu_bgm()

    controller.init_game_controller()
    game_controller = controller.get_game_controller()
    game_controller.display_main_menu()
    clock = pg.time.Clock()
    game_clock = internal_clock.Clock()
    game_clock.start_counting_action_tick()

    screen = pg.display.set_mode((1280, 720))
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
            if event.type == event_store.event["IN_GAME"]:
                load_in_game(screen_center)
            if event.type == event_store.event["LOAD_BONE"]:
                generator.generate_sprites((screen_center[0] + 400, screen_center[1] + 200))
        if game_controller.is_at_main_menu():
            misc_group.draw(screen)
            gameplay_group.draw(screen)

            gameplay_group.update()
            misc_group.update()

        if game_controller.is_in_game() and not game_controller.is_paused():
            if game_controller.is_paused():
                pause_menu_group.draw(screen)
            else:
                misc_group.draw(screen)
                character_group.draw(screen)
                obstacles_group.draw(screen)
                gameplay_group.draw(screen)

                character_group.update()
                obstacles_group.update()
                gameplay_group.update()
                misc_group.update()
                check_for_collision()
                prep_for_new_render()
                if spec.specs_index == spec.get_specs_length() - 1 and len(obstacles_group.sprites()) == 0:
                    spec.reset_spec_index()
                    game_controller.allow_render()
                    generator.generate_sprites((screen_center[0] + 400, screen_center[1] + 200))

        pg.display.update()
        game_clock.inc_tick()
        clock.tick(120)


if __name__ == "__main__":
    main()
