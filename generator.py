import bone


def continuous_bone_generator(current_specs, total_sprite, start_pos, obstacles_group, screen_center, heart_size):
    x_scale_step = (current_specs["end_scale_x"] - current_specs["start_scale_x"]) / total_sprite
    y_scale_step = (current_specs["end_scale_y"] - current_specs["start_scale_y"]) / total_sprite
    bone_start_pos = (int(start_pos[0]), int(start_pos[1] + current_specs["offset_y"]))
    for i in range(total_sprite):
        new_bone_scale_x = current_specs["start_scale_x"] + x_scale_step * i
        new_bone_scale_y = current_specs["start_scale_y"] + y_scale_step * i
        new_bone_scale = (new_bone_scale_x, new_bone_scale_y)
        new_bone_start_pos = (bone_start_pos[0] + current_specs["distance"] * i, bone_start_pos[1])
        new_bone = bone.Bone(new_bone_start_pos, new_bone_scale, screen_center, heart_size)
        obstacles_group.add(new_bone)
        if i == total_sprite - 1:
            return new_bone


def double_bone_generator(current_specs, total_sprite, start_pos, obstacles_group, screen_center, heart_size):
    heart_height = heart_size[1]
    bone_height = 512
    padding = 5
    bone_start_pos = (int(start_pos[0]), int(start_pos[1]))
    lower_bone_start_height = current_specs["heart_start_offset"] - heart_height - padding
    lower_bone_end_height = current_specs["heart_end_offset"] - heart_height - padding
    upper_bone_start_height = 200 - lower_bone_start_height - heart_height - padding
    upper_bone_end_height = 200 - lower_bone_end_height - heart_height - padding
    for i in range(total_sprite):
        lower_bone_height_step = (lower_bone_end_height - lower_bone_start_height) / total_sprite \
            if lower_bone_start_height > lower_bone_end_height \
            else (lower_bone_end_height - lower_bone_start_height) / total_sprite
        lower_bone_scale_x = 0.1
        lower_bone_scale_y = (lower_bone_start_height + lower_bone_height_step * i) / bone_height
        lower_bone_scale = (lower_bone_scale_x, lower_bone_scale_y)
        lower_bone_offset = (200 - lower_bone_scale_y * bone_height / 2)
        lower_bone_start_pos = (
            bone_start_pos[0] + current_specs["distance"] * i, bone_start_pos[1] + abs(100 - lower_bone_offset))
        lower_bone = bone.Bone(lower_bone_start_pos, lower_bone_scale, screen_center, heart_size)

        upper_bone_height_step = (upper_bone_end_height - upper_bone_start_height) / total_sprite \
            if upper_bone_start_height > upper_bone_end_height \
            else (upper_bone_end_height - upper_bone_start_height) / total_sprite
        upper_bone_scale_x = 0.1
        upper_bone_scale_y = (upper_bone_start_height + upper_bone_height_step * i) / bone_height
        upper_bone_scale = (upper_bone_scale_x, upper_bone_scale_y)
        upper_bone_offset = (200 - upper_bone_scale_y * bone_height / 2)
        upper_bone_start_pos = (
            bone_start_pos[0] + current_specs["distance"] * i, bone_start_pos[1] - abs(100 - upper_bone_offset))
        upper_bone = bone.Bone(upper_bone_start_pos, upper_bone_scale, screen_center, heart_size)
        obstacles_group.add(lower_bone)
        obstacles_group.add(upper_bone)
        if i == total_sprite - 1:
            return lower_bone
