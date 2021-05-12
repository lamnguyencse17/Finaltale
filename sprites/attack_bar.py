import random

import pygame as pg

import config


def _generate_health_color(current_health):
    if current_health < 33:
        return 255, 0, 0
    if current_health < 66:
        return 255, 255, 0
    return 0, 255, 0


class Bar(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        center = config.screen_center
        self.image = pg.Surface((1280, 720), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=center)
        self.health_bar_surface = pg.Surface((600, 90))
        self.bar_posx = 2
        self.__render_attack_bar()
        self.speed = random.uniform(1.0, 5.0)

    def __render_attack_bar(self):
        center = config.screen_center
        self.health_bar_surface.fill((0, 0, 0))
        pg.draw.rect(self.health_bar_surface, (255, 255, 255), (0, 0, 600, 60), 5, 1)
        pg.draw.rect(self.health_bar_surface, (255, 0, 0), (5, 5, 200, 50))
        pg.draw.rect(self.health_bar_surface, (255, 255, 0), (205, 5, 75, 50))
        pg.draw.rect(self.health_bar_surface, (0, 255, 0), (280, 5, 50, 50))
        pg.draw.rect(self.health_bar_surface, (255, 255, 0), (330, 5, 75, 50))
        pg.draw.rect(self.health_bar_surface, (255, 0, 0), (395, 5, 200, 50))

        pg.draw.rect(self.health_bar_surface, (0, 0, 255), (self.bar_posx, 5, 10, 50))
        self.image.blit(self.health_bar_surface, (center[0] - 405, center[1] - 305))

    def update(self):
        if self.bar_posx + 2 * self.speed > 600:
            self.kill()
        self.bar_posx += 2 * self.speed
        self.__render_attack_bar()
