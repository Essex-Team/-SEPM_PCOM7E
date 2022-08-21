import pygame as pg
from typing import Callable
from pygame.math import Vector2
from typing import Tuple, Sequence, Union
from python_lib.utils import Utils
from python_lib.components.GameObject import GameObject

class Arrows(GameObject):

    def __init__(
        self,
        coordinate_x: float,
        coordinate_y: float,
        arrow_id: str,
        color: Tuple[int, int, int],
        high_light_color: Tuple[int, int, int],
        points: Sequence[Union[Tuple[float, float], Sequence[float], Vector2]],
        on_click_event: Callable=None,
        is_muted: bool=False,
        animations=None,
    ):
        super().__init__(coordinate_x=coordinate_x, coordinate_y=coordinate_y, animations=animations)
        self.arrow_id = arrow_id
        self.color = color
        self.high_light_color = high_light_color
        self.display_color = self.color
        self.points = points
        self.on_click_event = on_click_event
        self.is_muted = is_muted

        self.clicked_sound = pg.mixer.Sound(Utils.getAssetPath("sounds/buttons/button_clicked.wav"))
        self.hovered_sound = pg.mixer.Sound(Utils.getAssetPath("sounds/buttons/button_hovered.wav"))
        self.clicked_sound.set_volume(0.06)
        self.hovered_sound.set_volume(0.06)
        self.is_previously_hovered = False
        self.is_hovered = False
        self.is_clicked = False

    def draw(self, surface: pg.surface.Surface):
        self.arrow_rect = pg.draw.polygon(
            surface=surface,
            color=self.display_color,
            points=self.points,
        )
        if self.arrow_rect.collidepoint(pg.mouse.get_pos()):
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

    def action(self):
        if self.on_click_event is not None:
            self.on_click_event()

    def display(self, surface: pg.surface.Surface):
        self.draw(surface=surface)
