import pygame as pg


class Heart(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load('heart.png').convert_alpha()
        self.image_size = (int(self.image.get_width() * 0.1), int(self.image.get_height() * 0.1))
        self.image = pg.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))
        self.border_top_left = (pos[0] - 400, pos[1] + 100)

        self.__set_intial_mouse_pos()

    def __set_intial_mouse_pos(self):
        (mouse_x, mouse_y) = pg.mouse.get_pos()
        self.last_mouse_movement = [mouse_x, mouse_y]

    def __set_heart_position(self, pos_x, pos_y):
        center_adjustment = [pos_x - self.image_size[0] / 2, pos_y - self.image_size[1] / 2]
        if center_adjustment[1] < self.border_top_left[1] + 5:
            center_adjustment[1] = self.border_top_left[1] + 5
        elif center_adjustment[1] + self.image_size[1] > self.border_top_left[1] + 200 - 5:
            center_adjustment[1] = self.border_top_left[1] + 200 - self.image_size[1] - 5
        if center_adjustment[0] < self.border_top_left[0]:
            center_adjustment[0] = self.border_top_left[0] + 4
        elif center_adjustment[0] + self.image_size[0] > self.border_top_left[0] + 800:
            center_adjustment[0] = self.border_top_left[0] + 800 - self.image_size[0] - 5
        self.rect.x = center_adjustment[0]
        self.rect.y = center_adjustment[1]

    def __handle_mouse_event(self):
        (mouse_x, mouse_y) = pg.mouse.get_pos()
        if self.last_mouse_movement[0] != mouse_x or self.last_mouse_movement[1] != mouse_y:
            self.__set_heart_position(mouse_x, mouse_y)
            self.last_mouse_movement[0] = mouse_x
            self.last_mouse_movement[1] = mouse_y

    def update(self):
        self.__handle_mouse_event()
