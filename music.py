import pygame as pg


def play_menu_bgm():
    pg.mixer.music.load("menu-bgm.mp3")
    pg.mixer.music.play(-1)


def play_ingame_music():
    pg.mixer.music.unload()
    pg.mixer.music.load("game_bgm.mp3")
    pg.mixer.music.play()


def stop_music():
    pg.mixer.music.stop()
    pg.mixer.music.unload()


def pause_music():
    pg.mixer.music.pause()


def unpause_music():
    pg.mixer.music.unpause()
