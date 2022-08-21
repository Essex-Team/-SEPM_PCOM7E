import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self, coordinate_x: float, coordinate_y: float, animations=None):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.animations = animations
        pygame.sprite.Sprite.__init__(self)
