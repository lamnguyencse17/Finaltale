from typing import Tuple

import music
from sprites import game_over
from sprites_group import misc_group, gameplay_group, obstacles_group


def load_game_over(screen_center: Tuple[int, int], screen):
    music.stop_music()
    music.play_game_over_music()
    misc_group.empty()
    obstacles_group.empty()
    gameplay_group.empty()
    misc_group.update()

    game_over_sprite = game_over.Menu()
    misc_group.add(game_over_sprite)

    gameplay_group.update()
    misc_group.update()
