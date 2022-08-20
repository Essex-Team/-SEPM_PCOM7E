import pygame as pg
from pygame.math import Vector2
from typing import Tuple, Sequence, Union
from python_lib.components.GameObject import GameObject

class Arrows(GameObject):

    def __init__(
        self,
        coordinate_x: float,
        coordinate_y: float,
        state: str,
        arrow_id: str,
        color: Tuple[int, int, int],
        points: Sequence[Union[Tuple[float, float], Sequence[float], Vector2]],
        animations=None,
    ):
        super().__init__(coordinate_x=coordinate_x, coordinate_y=coordinate_y, state=state, animations=animations)
        self.arrow_id = arrow_id
        self.color = color
        self.points = points

    def display(self, surface: pg.surface.Surface):
        self.arrow_rect = pg.draw.polygon(
            surface=surface,
            color=self.color,
            points=self.points,
        )
        
    def check_has_user_clicked(self, event: pg.event.Event):
        return event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.arrow_rect.collidepoint(event.pos)
        