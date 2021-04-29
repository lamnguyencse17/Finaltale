import json
from typing import Tuple

import pygame as pg

import bone
import border
import clock as internal_clock
import config
import controller
import generator
import heart
import music
import sans
import title

f = open('map.json', )

BLACK = (0, 0, 0)
collision_list = []
last_sprite: bone.Bone = None
specs = json.load(f)
specs_index = 0
allow_new_render = False


def prep_for_new_render():
    global allow_new_render
    global specs_index
    global specs
    global last_sprite
    if not allow_new_render:
        pg.event.clear()
        return
    if last_sprite.is_outside:
        return
    pg.time.set_timer(config.event["LOAD_BONE"], specs[specs_index]["start_time"], True)
    allow_new_render = False


def is_in_collision_list(bone_id):
    global collision_list
    sprite: bone.Bone
    for sprite in collision_list:
        if sprite == bone_id:
            return True
    return False


def check_for_collision(obstacles_group: pg.sprite.RenderUpdates):
    if len(obstacles_group.sprites()) == 0:
        collision_list.clear()
        return
    obstacle: bone.Bone
    for obstacle in obstacles_group.sprites():
        if obstacle.collided and not is_in_collision_list(obstacle.id):
            collision_list.append(obstacle.id)
            controller.game_controller.get_player().decrement_health()


def generate_sprites(obstacles_group: pg.sprite.RenderUpdates, start_pos: Tuple[int, int]):
    global specs
    global specs_index
    global allow_new_render
    global last_sprite
    print("RENDERING INDEX: ", specs_index)
    current_specs = specs[specs_index]
    total_sprite = current_specs["quantity"]

    if current_specs["type"] == "continuous":
        last_sprite = generator.continuous_bone_generator(current_specs, total_sprite, start_pos, obstacles_group)
    elif current_specs["type"] == "double":
        last_sprite = generator.double_bone_generator(current_specs, total_sprite, start_pos, obstacles_group)
    if len(specs) == specs_index + 1:
        pg.event.clear()
        allow_new_render = False
        return
    specs_index += 1
    allow_new_render = True
    print("READY FOR NEXT RENDER")


def main():
    global specs_index
    global last_sprite
    global specs
    global allow_new_render
    pg.init()
    pg.font.init()
    pg.display.set_caption("Final Tale")
    music.play_menu_bgm()

    config.define_event("LOAD_BONE", pg.USEREVENT + 1)

    controller.initGameController()
    game_controller = controller.getGameController()

    clock = pg.time.Clock()
    game_clock = internal_clock.Clock()
    game_clock.start_counting_action_tick()

    screen = pg.display.set_mode((1280, 720))
    screen_center = (screen.get_width() / 2, screen.get_height() / 2)

    pg.display.flip()

    bone.load_bone_image()
    heart.load_heart_image()
    heart_size = (int(heart.heart_image.get_width() * 0.1), int(heart.heart_image.get_height() * 0.1))
    config.set_heartsize(heart_size)
    config.set_screen_center(screen_center)

    character_group = pg.sprite.RenderUpdates()
    gameplay_group = pg.sprite.RenderUpdates()
    misc_group = pg.sprite.RenderUpdates()
    obstacles_group = pg.sprite.RenderUpdates()

    sans_sprite = sans.Sans((screen_center[0], screen_center[1] - 100))
    heart_sprite = heart.Heart(screen_center)
    border_sprite = border.Border(screen_center)
    title_sprite = title.Title(screen_center)

    character_group.add(sans_sprite)

    gameplay_group.add(heart_sprite)
    generate_sprites(obstacles_group, (screen_center[0] + 400, screen_center[1] + 200))

    misc_group.add(border_sprite)
    misc_group.add(title_sprite)

    character_group.update()
    gameplay_group.update()
    misc_group.update()

    while game_controller.is_game_running():
        screen.fill(BLACK)

        misc_group.draw(screen)
        character_group.draw(screen)
        obstacles_group.draw(screen)
        gameplay_group.draw(screen)

        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                game_controller.quit()
            if event.type == config.event["LOAD_BONE"]:
                generate_sprites(obstacles_group, (screen_center[0] + 400, screen_center[1] + 200))
        character_group.update()
        obstacles_group.update()
        gameplay_group.update()
        misc_group.update()
        check_for_collision(obstacles_group)
        prep_for_new_render()
        if specs_index == len(specs) - 1 and len(obstacles_group.sprites()) == 0:
            specs_index = 0
            allow_new_render = True
            generate_sprites(obstacles_group, (screen_center[0] + 400, screen_center[1] + 200))

        pg.display.update()
        game_clock.inc_tick()
        clock.tick(120)


if __name__ == "__main__":
    main()
