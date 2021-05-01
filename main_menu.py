import pygame as pg


class Menu(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        title_font = pg.font.Font("undertale.ttf", 40)
        option_font = pg.font.Font("undertale.ttf", 30)
        self.image = pg.surface.Surface((1280, 720))
        center = (self.image.get_width() / 2, self.image.get_height() / 2)
        self.rect = self.image.get_rect(center=center)

        cover = pg.image.load("cover.jpg")
        cover = pg.transform.scale(cover, [int(cover.get_width() * 0.9), int(cover.get_height() * 0.9)])
        cover_pos = (int(center[0] - cover.get_width() / 2), center[1] - 350)
        self.image.blit(cover, cover_pos)

        game_title = title_font.render('UNDERTALE', True, (255, 255, 255))
        self.image.blit(game_title, [center[0] - game_title.get_width() / 2, center[1] - 50])
        self.game_title_rect = game_title.get_rect(center=(center[0], center[1]))

        play_title = option_font.render('PLAY', True, (0, 255, 0))
        play_title_pos = (int(center[0] - play_title.get_width() / 2), center[1] + 100)
        self.image.blit(play_title, play_title_pos)
        self.play_title_rect = play_title.get_rect(
            center=[play_title_pos[0] + play_title.get_width() / 2, play_title_pos[1]])

        option_title = option_font.render('OPTION', True, (255, 255, 0))
        option_title_pos = (int(center[0] - option_title.get_width() / 2), center[1] + 150)
        self.image.blit(option_title, option_title_pos)
        self.option_title_rect = option_title.get_rect(
            center=[option_title_pos[0] + option_title.get_width() / 2, option_title_pos[1]])

        quit_title = option_font.render('QUIT', True, (255, 0, 0))
        quit_title_pos = (int(center[0] - quit_title.get_width() / 2), center[1] + 200)
        self.image.blit(quit_title, quit_title_pos)
        self.quit_title_rect = quit_title.get_rect(
            center=[quit_title_pos[0] + quit_title.get_width() / 2, quit_title_pos[1]])

    def is_quit_title_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        if self.quit_title_rect.collidepoint(mouse_pos):
            return True
        return False

    def is_play_title_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        if self.play_title_rect.collidepoint(mouse_pos):
            return True
        return False

    def is_option_title_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        if self.option_title_rect.collidepoint(mouse_pos):
            return True
        return False
