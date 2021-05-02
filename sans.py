import pygame as pg


class Sans(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load('sans.png').convert_alpha()
        self.image_size = (int(self.image.get_width() * 0.3), int(self.image.get_height() * 0.3))
        self.image = pg.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect(center=pos)
        self.__hp = 1000

    def __blink(self):
        pass

    def handle_attack(self):
        pass

    def update(self):
        pass
