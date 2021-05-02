class Player:
    def __init__(self):
        self.__health = 100

    def get_health(self):
        return self.__health

    def decrement_health(self):
        self.__health -= 1

    def attack(self):
        pass
