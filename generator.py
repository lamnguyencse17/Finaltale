import bone
import config

local_specs = {}


def continuous_bone_generator(current_specs, total_sprite, start_pos, obstacles_group):
    x_scale_step = (current_specs["end_scale_x"] - current_specs["start_scale_x"]) / total_sprite
    y_scale_step = (current_specs["end_scale_y"] - current_specs["start_scale_y"]) / total_sprite
    bone_start_pos = (int(start_pos[0]), int(start_pos[1] + current_specs["offset_y"]))
    for i in range(total_sprite):
        new_bone_scale_x = current_specs["start_scale_x"] + x_scale_step * i
        new_bone_scale_y = current_specs["start_scale_y"] + y_scale_step * i
        new_bone_scale = (new_bone_scale_x, new_bone_scale_y)
        new_bone_start_pos = (bone_start_pos[0] + current_specs["distance"] * i, bone_start_pos[1])
        new_bone = bone.Bone(new_bone_start_pos, new_bone_scale, config.screen_center, config.heart_size)
        obstacles_group.add(new_bone)
        if i == total_sprite - 1:
            return new_bone


def generate_double_bone_config(iteration, total_sprite, start_height, end_height, bone_start_pos, is_lower):
    global local_specs
    height_step = (end_height - start_height) / total_sprite \
        if start_height > end_height \
        else (end_height - start_height) / total_sprite
    bone_scale_x = 0.1
    bone_scale_y = (start_height + height_step * iteration) / config.bone_height
    bone_scale = (bone_scale_x, bone_scale_y)
    bone_offset = (200 - bone_scale_y * config.bone_height / 2)
    if is_lower:
        bone_start_pos = (
            bone_start_pos[0] + local_specs["distance"] * iteration, bone_start_pos[1] + abs(100 - bone_offset))
    else:
        bone_start_pos = (
         bone_start_pos[0] + local_specs["distance"] * iteration, bone_start_pos[1] - abs(100 - bone_offset))
    return bone_start_pos, bone_scale


def double_bone_generator(current_specs, total_sprite, start_pos, obstacles_group):
    global local_specs
    local_specs = current_specs
    heart_height = config.heart_size[1]
    padding = 5
    bone_start_pos = (int(start_pos[0]), int(start_pos[1]))
    lower_bone_start_height = current_specs["heart_start_offset"] - heart_height - padding
    lower_bone_end_height = current_specs["heart_end_offset"] - heart_height - padding
    upper_bone_start_height = 200 - lower_bone_start_height - heart_height - padding
    upper_bone_end_height = 200 - lower_bone_end_height - heart_height - padding
    for i in range(total_sprite):
        bone_config = generate_double_bone_config(i, total_sprite, upper_bone_start_height, upper_bone_end_height, bone_start_pos, False)
        upper_bone = bone.Bone(bone_config[0], bone_config[1], config.screen_center, config.heart_size)
        bone_config = generate_double_bone_config(i, total_sprite, lower_bone_start_height, lower_bone_end_height, bone_start_pos, True)
        lower_bone = bone.Bone(bone_config[0], bone_config[1], config.screen_center, config.heart_size)
        obstacles_group.add(lower_bone)
        obstacles_group.add(upper_bone)
        if i == total_sprite - 1:
            return lower_bone
