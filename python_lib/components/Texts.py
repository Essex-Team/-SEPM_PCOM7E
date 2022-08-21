import pygame as pg
from typing import Callable
from python_lib.utils import Utils
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
        high_light_color: str = None,
        on_click_event: Callable = None,
        font: str=Constants.FONT,
        font_size: int=Constants.NORMAL_FONT_SIZE,
        is_bold: bool=False,
        is_muted: bool=False,
        animations=None,
    ):
        super().__init__(coordinate_x=coordinate_x, coordinate_y=coordinate_y, animations=animations)
        self.text_id = text_id
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color
        self.high_light_color = high_light_color if high_light_color is not None else color
        self.display_color = color
        self.on_click_event = on_click_event
        self.is_bold = is_bold
        self.is_muted = is_muted

        self.clicked_sound = pg.mixer.Sound(Utils.getAssetPath("sounds/buttons/button_clicked.wav"))
        self.hovered_sound = pg.mixer.Sound(Utils.getAssetPath("sounds/buttons/button_hovered.wav"))
        self.clicked_sound.set_volume(0.06)
        self.hovered_sound.set_volume(0.06)
        self.is_previously_hovered = False
        self.is_hovered = False
        self.is_clicked = False

        self.font = pg.font.SysFont(self.font, self.font_size)
        self.font.set_bold(self.is_bold)

        text_surface = self.font.render(self.text, True, self.display_color)
        text_rect = text_surface.get_rect()

        self.text_surface: pg.surface.Surface = text_surface
        self.text_rect: pg.Rect  = text_rect

        self.update()

    def draw(self, surface: pg.surface.Surface):
        if self.text_rect.collidepoint(pg.mouse.get_pos()):
            self.is_previously_hovered = self.is_hovered
            self.is_hovered = True
            if self.is_hovered and not self.is_previously_hovered and not self.is_muted:
                self.hovered_sound.play()

            if pg.mouse.get_pressed()[0] == 1 and self.is_clicked is False:
                self.is_clicked = True
            else:
                self.is_clicked = False
        else:
            self.is_hovered = False

        if pg.mouse.get_pressed()[0] == 0:
            self.is_clicked = False

        if self.is_hovered:
            self.display_color = self.high_light_color
        else:
            self.display_color = self.color

        if self.is_hovered and self.is_clicked:
            if not self.is_muted:
                self.clicked_sound.play()

            self.display_color = self.high_light_color
            self.action()

        text_surface = self.font.render(self.text, True, self.display_color)
        text_rect = text_surface.get_rect()

        self.text_surface: pg.surface.Surface = text_surface
        self.text_rect: pg.Rect  = text_rect

        self.text_rect.center = (self.coordinate_x, self.coordinate_y)
        surface.blit(self.text_surface, self.text_rect)

    def action(self):
        if self.on_click_event is not None:
            self.on_click_event()

    def display(self, surface: pg.surface.Surface):
        self.draw(surface=surface)
