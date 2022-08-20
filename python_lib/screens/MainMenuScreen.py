import sys
import pygame as pg
from .Screen import Screen
from python_lib.constants import Constants
from python_lib.components.Texts import Texts

class MainMenuScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Main',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )

    def display(self):
        WELCOME_TEXT = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT // 3,
            state='display',
            text_id='welcome_text_component',
            text='GAME TITLE',
            color=Constants.BLACK,
            font=Constants.FONT,
            font_size=Constants.LARGE_FONT_SIZE,
            is_bold=True,
        )

        WELCOME_TEXT.display(surface=self.window)

        while True:
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            WELCOME_TEXT.display(surface=self.window)

            pg.display.update()
