import i18n
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
            screen_title=i18n.t('app.screens.restrictionWarning.title'),
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
        self.is_running = True
        self.is_indicator_sound_muted = False
        self.time_limit_settings = {
            "start_time": "00:00",
            "end_time": "00:00",
        }
        self.load_time_limit_from_json()
        self.load_indicator_sound_settings_from_json()

    @property
    def warning_message(self) -> str:
        start_time = self.time_limit_settings['start_time']
        end_time = self.time_limit_settings['end_time']
        return i18n.t(
            'app.screens.restrictionWarning.warningMessage',
            start_time=start_time,
            end_time=end_time,
        )

    def load_time_limit_from_json(self):
        self.time_limit_settings = Utils.loadContentFromJSON(
            Utils.getAssetPath(f'configs/{Constants.TIME_LIMIT_JSON_FILENAME}')
        )

    def load_indicator_sound_settings_from_json(self):
        indicator_sound_settings = Utils.loadContentFromJSON(
            Utils.getAssetPath(f'configs/{Constants.INDICATOR_SOUND_JSON_FILENAME}')
        )
        self.is_indicator_sound_muted = indicator_sound_settings['state'] is not True

    def exit(self):
        self.is_running = False
    
    def display(self):
        warning_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT // 3,
            text_id='warning_text_component',
            text=i18n.t('app.screens.restrictionWarning.warning'),
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.LARGE_FONT_SIZE,
            is_bold=True,
            is_muted=self.is_indicator_sound_muted,
        )

        restricted_access_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT // 3 + 60,
            text_id='restricted_access_text_component',
            text=i18n.t('app.screens.restrictionWarning.restrictedAccess'),
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
            is_muted=self.is_indicator_sound_muted,
        )

        time_restriction_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 220,
            text_id='time_restriction_text_component',
            # text=self.warning_message,
            text=i18n.t(
                'app.screens.restrictionWarning.warningMessage',
                start_time=self.time_limit_settings['start_time'],
                end_time=self.time_limit_settings['end_time'],
            ),
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
            is_muted=self.is_indicator_sound_muted,
        )

        exit_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 140,
            text_id='exit_text_component',
            text=i18n.t('app.screens.restrictionWarning.exit'),
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
            text=i18n.t('app.footer'),
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.SMALL_FONT_SIZE,
            is_muted=self.is_indicator_sound_muted,
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
