import pygame as pg

current_inc = 1


class Event:
    def __init__(self):
        self.event = {}

    def define_event(self, name):
        global current_inc
        self.event[name] = {}
        self.event[name]["object"] = pg.event.Event(pg.USEREVENT + current_inc)
        self.event[name]["value"] = pg.USEREVENT + current_inc
        current_inc += 1


event = Event()
