from typing import Tuple

from sprites import attack_bar
from sprites_group import misc_group


def load_attack_bar(screen_center: Tuple[int, int]):
    misc_group.empty()
    attack_bar_sprite = attack_bar.Bar()
    misc_group.add(attack_bar_sprite)
