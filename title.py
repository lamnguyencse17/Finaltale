import pygame as pg


class Title(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.font = pg.font.Font("undertale.ttf", 30)
        self.image = self.font.render('UNDERTALE', True, (255, 255, 255))
        self.image.blit(self.image, [pos[0] - self.image.get_width() / 2, pos[1] - 300])
        self.rect = self.image.get_rect(center=(pos[0], pos[1] - 300))
