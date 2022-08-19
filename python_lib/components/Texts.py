import pygame as pg
from pygame.surface import Surface
from python_lib.constants import Constants

class Texts(pg.sprite.Sprite):

    def __init__(self, text_id, text, color, height, width, font=Constants.FONT, font_size=Constants.NORMAL):
        super().__init__()
        self.text_id = text_id
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color
        self.height = height
        self.width = width

    def display(self, surface: Surface):
        font = pg.font.SysFont(self.font, self.font_size)
        text = font.render(self.text, True, self.color)

        text_rect = text.get_rect()
        
        text_rect.center = (self.width, self.height)
        surface.blit(text, text_rect)
