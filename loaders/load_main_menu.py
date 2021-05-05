from typing import Tuple

import main_menu
import music
import title
from sprites import heart
from sprites_group import misc_group, gameplay_group


def load_main_menu(screen_center: Tuple[int, int]):
    misc_group.empty()
    misc_group.update()
    music.play_menu_bgm()
    heart_sprite = heart.Heart(screen_center)
    title_sprite = title.Title(screen_center)
    main_menu_sprite = main_menu.Menu()

    gameplay_group.add(heart_sprite)
    misc_group.add(title_sprite)
    misc_group.add(main_menu_sprite)

    gameplay_group.update()
    misc_group.update()
