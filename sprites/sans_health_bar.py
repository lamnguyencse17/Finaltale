import pygame as pg

import config
import controller


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
        self.last_health = 1000
        self.image = pg.Surface((1280, 720), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=center)
        self.font = pg.font.Font("./undertale.ttf", 28)
        self.health_bar_surface = pg.Surface((210, 110))
        self.__render_health_bar(1, 1000)

    def __render_health_bar(self, scale, current_health):
        center = config.screen_center
        health_color = _generate_health_color(current_health)
        self.health_bar_surface.fill((0, 0, 0))
        pg.draw.rect(self.health_bar_surface, (255, 255, 255), (0, 0, 210, 30), 5, 1)
        pg.draw.rect(self.health_bar_surface, health_color, (5, 5, 200 * scale, 20))

        health_info = self.font.render("HP: {}/".format(current_health, 100), True, (255, 255, 255))
        self.health_bar_surface.blit(health_info, (0, 35))
        self.image.blit(self.health_bar_surface, (center[0] + 190, center[1] - 305))

    def update(self):
        game_controller = controller.get_game_controller()
        current_health = game_controller.get_sans_hp()
        # current_health = player.get_health()
        if self.last_health != current_health:
            scale = current_health / self.last_health
            self.__render_health_bar(scale, current_health)
