import controller
import option
from sprites_group import misc_group


def load_option_menu():
    game_controller = controller.get_game_controller()
    game_controller.display_option_menu()
    misc_group.empty()
    option_menu_sprite = option.Menu()
    misc_group.add(option_menu_sprite)
    # attack_bar_sprite = attack_bar.Bar()
    # misc_group.add(attack_bar_sprite)
    misc_group.update()
