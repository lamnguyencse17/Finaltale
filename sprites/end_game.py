import pygame as pg


class Menu(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.font = pg.font.Font("undertale.ttf", 30)
        self.image = pg.surface.Surface((1280, 720))
        center = (self.image.get_width() / 2, self.image.get_height() / 2)
        self.rect = self.image.get_rect(center=center)
        self.menu_title_rect: pg.rect.Rect = None
        self.sfx_title_rect: pg.rect.Rect = None
        self.bgm_title_rect: pg.rect.Rect = None
        self.back_title_rect: pg.rect.Rect = None
        self.render_game_over()

    def render_game_over(self):
        center = (self.image.get_width() / 2, self.image.get_height() / 2)
        menu_title = self.font.render('YOU WIN', True, (255, 255, 255))
        menu_title_pos = (int(center[0] - menu_title.get_width() / 2), center[1] - 300)
        self.image.blit(menu_title, menu_title_pos)
        self.menu_title_rect = menu_title.get_rect(
            center=[menu_title_pos[0] + menu_title.get_width() / 2, menu_title_pos[1]])

        back_title = self.font.render('BACK TO MAIN MENU', True, (255, 255, 255))
        back_title_pos = (int(center[0] - back_title.get_width() / 2), center[1] + 200)
        self.image.blit(back_title, back_title_pos)
        self.back_title_rect = back_title.get_rect(
            center=[back_title_pos[0] + back_title.get_width() / 2, back_title_pos[1]])

    def is_clicked_on_back(self):
        mouse_pos = pg.mouse.get_pos()
        if self.back_title_rect.collidepoint(mouse_pos):
            return True
        return False

    def update(self):
        self.image.fill((0, 0, 0))
        self.render_game_over()
