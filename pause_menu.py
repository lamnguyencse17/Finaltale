import pygame as pg


class Menu(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.font = pg.font.Font("undertale.ttf", 30)
        self.image = pg.surface.Surface((1280, 720))
        center = (self.image.get_width() / 2, self.image.get_height() / 2)

        menu_title = self.font.render('PAUSE MENU', True, (255, 255, 255))
        menu_title_pos = (int(center[0] - menu_title.get_width() / 2), center[1] - 300)
        self.image.blit(menu_title, menu_title_pos)
        self.rect = self.image.get_rect(center=center)
        self.menu_title_rect = menu_title.get_rect(
            center=[menu_title_pos[0] + menu_title.get_width() / 2, menu_title_pos[1]])

        resume_title = self.font.render('RESUME', True, (0, 255, 0))
        resume_title_pos = (int(center[0] - resume_title.get_width() / 2), center[1] - 150)
        self.image.blit(resume_title, resume_title_pos)
        self.resume_title_rect = resume_title.get_rect(
            center=[resume_title_pos[0] + resume_title.get_width() / 2, resume_title_pos[1]])

        quit_title = self.font.render('QUIT', True, (255, 0, 0))
        quit_title_pos = (int(center[0] - quit_title.get_width() / 2), center[1])
        self.image.blit(quit_title, quit_title_pos)
        self.quit_title_rect = quit_title.get_rect(
            center=[quit_title_pos[0] + quit_title.get_width() / 2, quit_title_pos[1]])

    def is_clicked_on_resume(self):
        mouse_pos = pg.mouse.get_pos()
        if self.resume_title_rect.collidepoint(mouse_pos):
            return True
        return False

    def is_clicked_on_quit(self):
        mouse_pos = pg.mouse.get_pos()
        if self.quit_title_rect.collidepoint(mouse_pos):
            return True
        return False
