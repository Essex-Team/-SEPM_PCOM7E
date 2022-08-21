import sys
import pygame as pg
from .Screen import Screen
from python_lib.constants import Constants
from python_lib.screens.StartScreen import StartScreen
from python_lib.screens.SettingsScreen import SettingsScreen
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
        self.window.fill(Constants.WHITE)
        self.click = False

    def show_start_screen(self):
        start_screen: StartScreen = StartScreen(
            window=self.window,
            clock=self.clock,
        )
        start_screen.display()

    def show_settings_screen(self):
        settings_screen: SettingsScreen = SettingsScreen(
            window=self.window,
            clock=self.clock,
        )
        settings_screen.display()

    def exit(self):
        pg.quit()
        sys.exit()

    def display(self):
        while True:
            self.window.fill(Constants.WHITE)

            welcome_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT // 3,
                text_id='welcome_text_component',
                text='GAME TITLE',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.LARGE_FONT_SIZE,
                is_bold=True,
            )

            welcome_text_view.display(surface=self.window)

            start_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 300,
                text_id='start_text_component',
                text='START',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
                is_bold=True,
            )

            start_text_view.display(surface=self.window)

            settings_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 260,
                text_id='settings_text_component',
                text='SETTINGS',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
                is_bold=True,
            )

            settings_text_view.display(surface=self.window)

            exit_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 220,
                text_id='exit_text_component',
                text='EXIT',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
                is_bold=True,
            )

            exit_text_view.display(surface=self.window)

            footer = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 100,
                text_id='footer_text_component',
                text='Team 1, Software Engineering Project Management @ 2022',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.SMALL_FONT_SIZE,
            )

            footer.display(surface=self.window)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if start_text_view.check_has_user_clicked(event):
                    self.show_start_screen()

                if settings_text_view.check_has_user_clicked(event):
                    self.show_settings_screen()

                if exit_text_view.check_has_user_clicked(event):
                    self.exit()

            pg.display.update()
            self.clock.tick(Constants.FPS)
