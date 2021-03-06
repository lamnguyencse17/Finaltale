from typing import Tuple

import pygame as pg
from event import event as event_store
import player
from sprites import bone


class Controller:
    def __init__(self):
        self.__player = player.Player()
        self.scene = 1
        self.__is_running = True
        self.screen_center = None
        self.__is_at_main_menu = True
        self.__is_in_game = False
        self.__is_in_pause_state = False
        self.allow_new_render = False
        self.__last_sprite: bone.Bone = None
        self.game_loaded = False
        self.__is_at_option_menu = False
        self.__allow_new_cloud = True
        self.__allow_new_item = True
        self.__is_at_game_over = False
        self.__is_attacking = False
        self.__is_at_end_game = False
        self.__sans_hp = 1000

    def handle_attack(self, damage):
        if self.__sans_hp - damage <= 0:
            pg.event.post(event_store.event["END_GAME"]["object"])
        self.__sans_hp -= damage

    def get_sans_hp(self):
        return self.__sans_hp

    def toggle_attack(self):
        self.__is_attacking = not self.__is_attacking

    def is_attacking(self):
        return self.__is_attacking

    def set_last_sprite(self, sprite: pg.sprite.Sprite):
        self.__last_sprite = sprite

    def get_last_sprite(self):
        return self.__last_sprite

    def allow_render(self):
        self.allow_new_render = True

    def block_render(self):
        self.allow_new_render = False

    def quit(self):
        self.__is_running = False

    def is_game_running(self):
        return self.__is_running

    def is_in_game(self):
        return self.__is_in_game

    def is_at_main_menu(self):
        return self.__is_at_main_menu

    def get_player(self):
        return self.__player

    def set_screen_center(self, screen_center: Tuple[float, float]):
        self.screen_center = screen_center

    def get_screen_center(self):
        return self.screen_center

    def display_main_menu(self):
        self.__is_at_main_menu = True
        self.__is_in_game = False
        self.__is_at_option_menu = False
        self.__is_at_game_over = False
        self.__is_at_end_game = False

    def display_option_menu(self):
        self.__is_at_main_menu = False
        self.__is_at_option_menu = True
        self.__is_in_game = False
        self.__is_at_game_over = False
        self.__is_at_end_game = False

    def display_game(self):
        self.__is_at_main_menu = False
        self.__is_in_game = True
        self.__is_at_option_menu = False
        self.__is_at_game_over = False
        self.__is_at_end_game = False

    def display_game_over(self):
        self.__is_at_game_over = True
        self.__is_at_main_menu = False
        self.__is_in_game = False
        self.__is_at_option_menu = False
        self.__is_at_end_game = False

    def display_end_game(self):
        self.__is_at_end_game = True
        self.__is_at_game_over = False
        self.__is_at_main_menu = False
        self.__is_in_game = False
        self.__is_at_option_menu = False

    def is_at_end_game(self):
        return self.__is_at_end_game

    def unpause_game(self):
        self.__is_in_pause_state = False

    def pause_game(self):
        self.__is_in_pause_state = True

    def is_paused(self):
        return self.__is_in_pause_state

    def is_at_option_menu(self):
        return self.__is_at_option_menu

    def allow_new_cloud(self):
        self.__allow_new_cloud = True

    def block_new_cloud(self):
        self.__allow_new_cloud = False

    def is_new_cloud_allowed(self):
        return self.__allow_new_cloud

    def allow_new_item(self):
        self.__allow_new_item = True

    def block_new_item(self):
        self.__allow_new_item = False

    def is_new_item_allowed(self):
        return self.__allow_new_item

    def is_at_game_over(self):
        return self.__is_at_game_over


game_controller: Controller = None


def init_game_controller():
    global game_controller
    game_controller = Controller()


def get_game_controller():
    global game_controller
    return game_controller
