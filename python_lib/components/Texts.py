import pygame as pg
from python_lib.constants import Constants
from python_lib.components.GameObject import GameObject

class Texts(GameObject):

    def __init__(
        self,
        coordinate_x: float,
        coordinate_y: float,
        state: str,
        text_id: str,
        text: str,
        color: str,
        font: str=Constants.FONT,
        font_size: int =Constants.NORMAL_FONT_SIZE,
        animations=None,
    ):
        super().__init__(coordinate_x=coordinate_x, coordinate_y=coordinate_y, state=state, animations=animations)
        self.text_id = text_id
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color

    def display(self, surface: pg.surface.Surface):
        font = pg.font.SysFont(self.font, self.font_size)
        text = font.render(self.text, True, self.color)

        text_rect = text.get_rect()
        
        text_rect.center = (self.coordinate_x, self.coordinate_y)
        surface.blit(text, text_rect)
