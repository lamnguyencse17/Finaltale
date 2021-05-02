from typing import Tuple

import border
import controller
import generator
import health_bar
import music
import sans
from spec import spec
from sprites_group import character_group, misc_group, gameplay_group


def load_in_game(screen_center: Tuple[int, int]):
    music.play_ingame_music()
    spec.load_specs()
    game_controller = controller.get_game_controller()
    game_controller.game_loaded = True

    sans_sprite = sans.Sans((screen_center[0], screen_center[1] - 100))
    border_sprite = border.Border(screen_center)
    health_bar_sprite = health_bar.Bar()
    generator.generate_sprites((screen_center[0] + 400, screen_center[1] + 200))

    character_group.add(sans_sprite)
    misc_group.add(border_sprite)
    gameplay_group.add(health_bar_sprite)

    gameplay_group.update()
    character_group.update()
    misc_group.update()
    game_controller.display_game()
