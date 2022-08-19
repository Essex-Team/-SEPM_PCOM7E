import pygame as pg

class GameObject(pg.sprite.Sprite):

    def __init__(self, coordinate_x: float, coordinate_y: float, state: str, animations=None):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.state = state
        self.animations = animations
