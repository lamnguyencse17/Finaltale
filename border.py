import pygame as pg


class Border(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((1280, 720))
        self.rect = self.image.get_rect(center=pos)
        pg.draw.rect(self.image, (255, 0, 0), (pos[0] - 400, pos[1] + 100, 800, 200), 5, 1)
