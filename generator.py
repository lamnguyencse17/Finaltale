import random
from typing import Tuple

import pygame as pg

import config
import controller
import sprites_group
from event import event as event_store
from spec import spec
from sprites import bone, cloud, item
from sprites_group import misc_group


def continuous_bone_generator(current_specs, total_sprite, start_pos):
    x_scale_step = (current_specs["end_scale_x"] - current_specs["start_scale_x"]) / total_sprite
    y_scale_step = (current_specs["end_scale_y"] - current_specs["start_scale_y"]) / total_sprite
    bone_start_pos = (int(start_pos[0]), int(start_pos[1] + current_specs["offset_y"]))
    for i in range(total_sprite):
        new_bone_scale_x = current_specs["start_scale_x"] + x_scale_step * i
        new_bone_scale_y = current_specs["start_scale_y"] + y_scale_step * i
        new_bone_scale = (new_bone_scale_x, new_bone_scale_y)
        new_bone_start_pos = (bone_start_pos[0] + current_specs["distance"] * i, bone_start_pos[1])
        new_bone = bone.Bone(new_bone_start_pos, new_bone_scale)
        sprites_group.obstacles_group.add(new_bone)
        if i == total_sprite - 1:
            sprites_group.obstacles_group.update()
            return new_bone


def generate_double_bone_config(iteration, total_sprite, start_height, end_height, bone_start_pos, is_lower):
    height_step = (end_height - start_height) / total_sprite \
        if start_height > end_height \
        else (end_height - start_height) / total_sprite
    bone_scale_x = 0.1
    bone_scale_y = (start_height + height_step * iteration) / config.bone_height
    bone_scale = (bone_scale_x, bone_scale_y)
    bone_offset = (200 - bone_scale_y * config.bone_height / 2)
    if is_lower:
        bone_start_pos = (
            bone_start_pos[0] + spec.current_specs["distance"] * iteration,
            bone_start_pos[1] + abs(100 - bone_offset))
    else:
        bone_start_pos = (
            bone_start_pos[0] + spec.current_specs["distance"] * iteration,
            bone_start_pos[1] - abs(100 - bone_offset))
    return bone_start_pos, bone_scale


def double_bone_generator(current_specs, total_sprite, start_pos, obstacles_group):
    heart_height = config.heart_size[1]
    padding = 5
    bone_start_pos = (int(start_pos[0]), int(start_pos[1]))
    lower_bone_start_height = current_specs["heart_start_offset"] - heart_height - padding
    lower_bone_end_height = current_specs["heart_end_offset"] - heart_height - padding
    upper_bone_start_height = 200 - lower_bone_start_height - heart_height - padding
    upper_bone_end_height = 200 - lower_bone_end_height - heart_height - padding
    for i in range(total_sprite):
        bone_config = generate_double_bone_config(i, total_sprite, upper_bone_start_height, upper_bone_end_height,
                                                  bone_start_pos, False)
        upper_bone = bone.Bone(bone_config[0], bone_config[1])
        bone_config = generate_double_bone_config(i, total_sprite, lower_bone_start_height, lower_bone_end_height,
                                                  bone_start_pos, True)
        lower_bone = bone.Bone(bone_config[0], bone_config[1])
        obstacles_group.add(lower_bone)
        obstacles_group.add(upper_bone)
        if i == total_sprite - 1:
            obstacles_group.update()
            return lower_bone


def generate_sprites(start_pos: Tuple[int, int]):
    game_controller = controller.get_game_controller()
    print("RENDERING INDEX: ", spec.specs_index)
    current_specs = spec.current_specs
    total_sprite = current_specs["quantity"]

    if current_specs["type"] == "continuous":
        last_sprite = continuous_bone_generator(current_specs, total_sprite, start_pos)
    elif current_specs["type"] == "double":
        last_sprite = double_bone_generator(current_specs, total_sprite, start_pos, sprites_group.obstacles_group)
    else:
        last_sprite = continuous_bone_generator(current_specs, total_sprite, start_pos)
    game_controller.set_last_sprite(last_sprite)
    if spec.get_specs_length() == spec.specs_index + 1:
        pg.event.clear()
        game_controller.block_render()
        return
    spec.increment_spec_index()
    game_controller.allow_render()
    print("READY FOR NEXT RENDER")


def gen_cloud():
    center = config.screen_center
    game_controller = controller.get_game_controller()
    y_offset = random.randint(125, 280)
    cloud_sprite = cloud.Cloud((center[0] + 300, center[1] + y_offset))
    misc_group.add(cloud_sprite)
    misc_group.update()
    game_controller.block_new_cloud()
    pg.time.set_timer(event_store.event["ALLOW_NEW_CLOUD"]["object"], 1000, True)


def gen_item():
    center = config.screen_center
    game_controller = controller.get_game_controller()
    y_offset = random.randint(225, 285)
    item_sprite = item.Item((center[0] + 300, center[1] + y_offset))
    misc_group.add(item_sprite)
    misc_group.update()
    print("CALLING NEW ITEM")
    game_controller.block_new_item()
    pg.time.set_timer(event_store.event["ALLOW_NEW_ITEM"]["object"], 2000, True)
