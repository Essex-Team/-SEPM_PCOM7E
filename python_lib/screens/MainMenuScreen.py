import sys
import pygame as pg
from python_lib.utils import Utils
from python_lib.constants import Constants
from python_lib.components.Texts import Texts
from python_lib.screens.Screen import Screen
from python_lib.screens.StartScreen import StartScreen
from python_lib.screens.SettingsScreen import SettingsScreen

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
        self.is_running = True
        self.is_indicator_sound_muted = False
        self.load_indicator_sound_settings_from_json()

    def load_indicator_sound_settings_from_json(self):
        indicator_sound_settings = Utils.loadContentFromJSON(
            Utils.getAssetPath(f'configs/{Constants.INDICATOR_SOUND_JSON_FILENAME}')
        )
        self.is_indicator_sound_muted = indicator_sound_settings['state'] is not True

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
        welcome_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT // 3,
            text_id='welcome_text_component',
            text='GAME TITLE',
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.LARGE_FONT_SIZE,
            is_bold=True,
            is_muted=self.is_indicator_sound_muted,
        )

        start_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 300,
            text_id='start_text_component',
            text='START',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.show_start_screen,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
            is_muted=self.is_indicator_sound_muted,
        )

        settings_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 260,
            text_id='settings_text_component',
            text='SETTINGS',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.show_settings_screen,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
            is_muted=self.is_indicator_sound_muted,
        )

        exit_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 220,
            text_id='exit_text_component',
            text='EXIT',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.exit,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
            is_muted=self.is_indicator_sound_muted,
        )

        footer = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 100,
            text_id='footer_text_component',
            text='Team 1, Software Engineering Project Management @ 2022',
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.SMALL_FONT_SIZE,
            is_muted=self.is_indicator_sound_muted,
        )

        text_view_list = [
            welcome_text_view,
            start_text_view,
            settings_text_view,
            exit_text_view,
            footer,
        ]

        while self.is_running:
            self.window.fill(Constants.WHITE)

            for text_view in text_view_list:
                text_view.display(surface=self.window)
                text_view.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.display.update()
            self.clock.tick(Constants.FPS)
