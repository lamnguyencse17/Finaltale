import os
import sys

import pygame as pg

import config

bone_image: pg.Surface = None


def load_bone_image():
    global bone_image
    bone_image = pg.image.load('bone.png').convert_alpha()


class Bone(pg.sprite.Sprite):

    def __init__(self, pos, scale):
        global bone_image
        super().__init__()
        self.image = bone_image.copy()
        self.image_size = (int(self.image.get_width() * scale[0]), int(self.image.get_height() * scale[1]))
        self.image = pg.transform.scale(self.image, self.image_size)
        self.is_outside = True
        self.true_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.id = int.from_bytes(os.urandom(2), sys.byteorder)
        self.tick = 0
        self.collided = False
        self.heart_size = config.heart_size
        self.__calculate_offset_based_on_speed()
        center = config.screen_center
        self.border_top_left = (center[0] - 400, center[1] + 100)

    def __calculate_offset_based_on_speed(self):
        self.offset = 800 / (config.speed * 120)

    def __check_collision(self):
        if self.collided:
            return
        (mouse_x, mouse_y) = pg.mouse.get_pos()
        is_collided = self.rect.collidepoint(mouse_x, mouse_y + config.heart_size[1] / 2)
        if is_collided:
            self.collided = True

    def __is_at_left_border(self):
        pos = [self.rect.centerx + self.image_size[0] / 2, self.rect.centerx + self.image_size[1] / 2]
        if pos[0] - 25 < self.border_top_left[0]:
            return True
        return False

    def __is_outside_right_border(self):
        pos = [self.rect.centerx + self.image_size[0] / 2, self.rect.centerx + self.image_size[1] / 2]
        if pos[0] > self.border_top_left[0] + 800:
            self.image = pg.Surface((1, 1))
            return True
        self.image = self.true_image
        self.is_outside = False
        return False

    def update(self):
        if self.is_outside:
            self.__is_outside_right_border()
        self.__check_collision()
        if self.__is_at_left_border():
            self.kill()
        self.rect = self.rect.move(-self.offset, 0)
