class Player:
    def __init__(self):
        self.__health = 100

    def get_health(self):
        return self.__health

    def decrement_health(self):
        self.__health -= 1

    def heal(self, amount):
        if self.__health + amount >= 100:
            self.__health = 100
            return
        self.__health += amount

    def attack(self):
        pass
