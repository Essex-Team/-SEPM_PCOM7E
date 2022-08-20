import pygame as pg
from .Screen import Screen
from python_lib.constants import Constants
from python_lib.components.Texts import Texts

class StartScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Start',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
        

    def display(self):
        running = True
        while running:

            self.window.fill(Constants.WHITE)

            start_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT // 3,
                state='display',
                text_id='start_text_component',
                text='START',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.LARGE_FONT_SIZE,
                is_bold=True,
            )

            start_text_view.display(surface=self.window)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False

            pg.display.update()
            self.clock.tick(Constants.FPS)
