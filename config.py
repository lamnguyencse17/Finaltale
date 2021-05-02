from typing import Tuple

heart_size: Tuple[int, int] = None
screen_center: Tuple[int, int] = None
bone_height = 512
speed = 1
is_bgm_muted = False
is_sfx_muted = False


def toggle_bgm():
    global is_bgm_muted
    is_bgm_muted = not is_bgm_muted


def toggle_sfx():
    global is_sfx_muted
    is_sfx_muted = not is_sfx_muted


def set_heartsize(size: Tuple[int, int]):
    global heart_size
    heart_size = size


def set_screen_center(center: Tuple[int, int]):
    global screen_center
    screen_center = center
