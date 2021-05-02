import pygame as pg

current_bgm: str = None


def play_menu_bgm():
    global current_bgm
    if current_bgm == "menu_bgm":
        return
    pg.mixer.music.load("menu_bgm.mp3")
    current_bgm = "menu_bgm"
    pg.mixer.music.play(-1)


def play_ingame_music():
    global current_bgm
    if current_bgm == "game_bgm":
        return
    pg.mixer.music.unload()
    pg.mixer.music.load("game_bgm.mp3")
    current_bgm = "game_bgm"
    pg.mixer.music.play()


def toggle_bgm():
    if pg.mixer.music.get_volume() == float(0):
        pg.mixer.music.set_volume(float(1))
        return
    pg.mixer.music.set_volume(float(0))


def mute_bgm():
    pg.mixer.music.set_volume(float(0))


def unmute_bgm():
    pg.mixer.music.set_volume(float(1))


def stop_music():
    pg.mixer.music.stop()
    pg.mixer.music.unload()


def pause_music():
    pg.mixer.music.pause()


def unpause_music():
    pg.mixer.music.unpause()
