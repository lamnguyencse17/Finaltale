import player


class Controller:
    def __init__(self):
        self.__player = player.Player()
        self.scene = 1
        self.__is_running = True

    def quit(self):
        self.__is_running = False

    def is_game_running(self):
        return self.__is_running

    def get_player(self):
        return self.__player
