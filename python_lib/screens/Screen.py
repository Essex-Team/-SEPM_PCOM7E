import pygame as pg

class Screen:

    def __init__(
        self,
        window: pg.surface.Surface,
        clock: pg.time.Clock,
        screen_title: str,
        screen_width: float,
        screen_height: float,
        background_image: str = None,
    ):
        super().__init__()
        self.window = window
        self.clock = clock
        self.screen_title = screen_title
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_image = background_image

    def switch_screen(self):
        pass

    def attach_object(self):
        pass

    def destroy_object(self):
        pass
