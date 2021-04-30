from typing import Tuple

heart_size: Tuple[int, int] = None
screen_center: Tuple[int, int] = None
bone_height = 512
speed = 1


def set_heartsize(size: Tuple[int, int]):
    global heart_size
    heart_size = size


def set_screen_center(center: Tuple[int, int]):
    global screen_center
    screen_center = center
