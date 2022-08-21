import pygame as pg
from python_lib.utils import Utils
from python_lib.constants import Constants
from python_lib.screens.Screen import Screen
from python_lib.components.Texts import Texts

class RestrictionWarningScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Restriction Warning',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
        self.is_running = True
        self.time_limit_settings = {
            "start_time": "00:00",
            "end_time": "00:00",
        }
        self.load_time_limit_from_json()

    @property
    def warning_message(self) -> str:
        start_time = self.time_limit_settings['start_time']
        end_time = self.time_limit_settings['end_time']
        return f'Only access From {start_time} to {end_time} is allowed'

    def load_time_limit_from_json(self):
        self.time_limit_form = Utils.loadContentFromJSON(
            Utils.getAssetPath(f'configs/{Constants.TIME_LIMIT_JSON_FILENAME}')
        )

    def exit(self):
        self.is_running = False
    
    def display(self):
        warning_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT // 3,
            text_id='warning_text_component',
            text='WARNING',
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.LARGE_FONT_SIZE,
            is_bold=True,
        )

        restricted_access_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT // 3 + 60,
            text_id='restricted_access_text_component',
            text='RESTRICTED ACCESS',
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
        )

        time_restriction_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 220,
            text_id='time_restriction_text_component',
            text=self.warning_message,
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
        )

        exit_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 140,
            text_id='exit_text_component',
            text='EXIT',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.exit,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
        )

        footer = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 100,
            text_id='footer_text_component',
            text='Team 1, Software Engineering Project Management @ 2022',
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.SMALL_FONT_SIZE,
        )

        text_view_list = [
            warning_text_view,
            restricted_access_text_view,
            time_restriction_text_view,
            exit_text_view,
            footer,
        ]

        while self.is_running:

            self.window.fill(Constants.WHITE)

            for text_view in text_view_list:
                text_view.display(surface=self.window)
                text_view.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.exit()

            pg.display.update()
            self.clock.tick(Constants.FPS)
