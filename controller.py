from typing import Tuple

import player


class Controller:
    def __init__(self):
        self.__player = player.Player()
        self.scene = 1
        self.__is_running = True
        self.screen_center = None

    def quit(self):
        self.__is_running = False

    def is_game_running(self):
        return self.__is_running

    def get_player(self):
        return self.__player

    def set_screen_center(self, screen_center: Tuple[float, float]):
        self.screen_center = screen_center

    def get_screen_center(self):
        return self.screen_center


game_controller: Controller = None


def initGameController():
    global game_controller
    game_controller = Controller()


def getGameController():
    global game_controller
    return game_controller
