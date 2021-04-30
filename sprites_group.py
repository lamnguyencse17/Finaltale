import pygame as pg

obstacles_group: pg.sprite.RenderUpdates = None


def init_sprites_group():
    global obstacles_group
    obstacles_group = pg.sprite.RenderUpdates()
