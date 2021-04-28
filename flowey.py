import os
import sys

import pygame as pg

speed = 1


class Flowey(pg.sprite.Sprite):

    def __init__(self, pos, center, heart_size):
        global speed
        super().__init__()
        self.image = pg.image.load('flowey.png').convert_alpha()
        self.image_size = (int(self.image.get_width() * 0.05), int(self.image.get_height() * 0.05))
        self.image = pg.transform.scale(self.image, self.image_size)
        self.is_outside = True
        self.true_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.id = int.from_bytes(os.urandom(2), sys.byteorder)
        self.tick = 0
        self.speed = speed
        self.collided = False
        self.border_top_left = (center[0] - 400, center[1] + 100)
        self.heart_size = heart_size
        self.__calculate_offset_based_on_speed(speed)

    def __check_collision(self):
        if self.collided:
            return
        (mouse_x, mouse_y) = pg.mouse.get_pos()
        is_collided = self.rect.collidepoint(mouse_x, mouse_y + self.heart_size[1] / 2)
        if is_collided:
            self.collided = True

    def __is_outside_right_border(self):
        pos = [self.rect.centerx + self.image_size[0] / 2, self.rect.centerx + self.image_size[1] / 2]
        if pos[0] > self.border_top_left[0] + 800:
            self.image = pg.Surface((1, 1))
            return True
        self.image = self.true_image
        self.is_outside = False
        return False

    def __is_at_left_border(self):
        pos = [self.rect.centerx + self.image_size[0] / 2, self.rect.centerx + self.image_size[1] / 2]
        if pos[0] - 25 < self.border_top_left[0]:
            return True
        return False

    def __calculate_offset_based_on_speed(self, speed):
        self.offset = 800 / (speed * 120)

    def update(self):
        if self.is_outside:
            self.__is_outside_right_border()
        self.__check_collision()
        if self.__is_at_left_border():
            self.kill()
        self.rect = self.rect.move(-self.offset, 0)
        self.__calculate_offset_based_on_speed(self.speed)