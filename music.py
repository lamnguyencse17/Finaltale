import pygame as pg


def play_menu_bgm():
    pg.mixer.music.load("menu-bgm.mp3")
    pg.mixer.music.play(-1)


def stop_menu_bgm():
    pg.mixer.music.stop()
    pg.mixer.music.unload()
