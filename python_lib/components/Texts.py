import pygame as pg
from python_lib.constants import Constants
from python_lib.components.GameObject import GameObject

class Texts(GameObject):

    def __init__(
        self,
        coordinate_x: float,
        coordinate_y: float,
        text_id: str,
        text: str,
        color: str,
        font: str=Constants.FONT,
        font_size: int=Constants.NORMAL_FONT_SIZE,
        is_bold: bool=False,
        animations=None,
    ):
        super().__init__(coordinate_x=coordinate_x, coordinate_y=coordinate_y, animations=animations)
        self.text_id = text_id
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color
        self.is_bold = is_bold

        font = pg.font.SysFont(self.font, self.font_size)
        font.set_bold(self.is_bold)

        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()

        self.text_surface: pg.surface.Surface = text_surface
        self.text_rect: pg.Rect  = text_rect

    def display(self, surface: pg.surface.Surface):
        self.text_rect.center = (self.coordinate_x, self.coordinate_y)
        surface.blit(self.text_surface, self.text_rect)

    def check_has_user_clicked(self, event: pg.event.Event):
        return event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.text_rect.collidepoint(event.pos)
