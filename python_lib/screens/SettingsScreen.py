import pygame as pg
from .Screen import Screen
from python_lib.constants import Constants
from python_lib.components.Texts import Texts

class SettingsScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Settings',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )

    def display(self):
        running = True
        while running:
            self.window.fill(Constants.WHITE)

            settings_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT // 3,
                state='display',
                text_id='settings_text_component',
                text='SETTINGS',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.LARGE_FONT_SIZE,
                is_bold=True,
            )

            settings_text_view.display(surface=self.window)

            back_to_main_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 220,
                state='ready',
                text_id='back_to_main_text_component',
                text='BACK TO MAIN MENU',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
                is_bold=True,
            )

            back_to_main_text_view.display(surface=self.window)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False

                if back_to_main_text_view.check_has_user_clicked(event):
                    running = False

            pg.display.update()
            self.clock.tick(Constants.FPS)
