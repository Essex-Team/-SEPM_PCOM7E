import pygame as pg
from python_lib.utils import Utils
from python_lib.constants import Constants
from python_lib.components.Texts import Texts
from python_lib.components.Arrows import Arrows
from python_lib.screens.Screen import Screen

class SetIndicatorSoundScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Indicator Sound Settings',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
        self.is_running = True
        self.should_display_arrows = False
        self.is_indicator_sound_muted = False
        self.indicator_sound_settings = {
            'state': True,
        }
        self.load_indicator_sound_settings_from_json()

    @property
    def current_state(self):
        if self.indicator_sound_settings['state']:
            return 'ENABLED'

        return 'DISABLED'

    def exit(self):
        self.is_running = False

    def load_indicator_sound_settings_from_json(self):
        self.indicator_sound_settings = Utils.loadContentFromJSON(
            Utils.getAssetPath(f'configs/{Constants.INDICATOR_SOUND_JSON_FILENAME}'),
        )
        self.is_indicator_sound_muted = self.indicator_sound_settings['state'] is not True

    def handle_save_time_limit_to_json(self):
        Utils.saveContentToJSON(
            Utils.getAssetPath(f'configs/{Constants.INDICATOR_SOUND_JSON_FILENAME}'),
            self.indicator_sound_settings,
        )

    def handle_on_confirm_click(self):
        self.handle_save_time_limit_to_json()
        self.exit()

    def handle_on_cancel_click(self):
        self.exit()

    def toggle_arrows(self):
        self.should_display_arrows = not self.should_display_arrows

    def handle_left_arrow_click(self):
        self.indicator_sound_settings['state'] = not self.indicator_sound_settings['state']
    
    def handle_right_arrow_click(self):
        self.indicator_sound_settings['state'] = not self.indicator_sound_settings['state']

    def display(self):
        indicator_sound_settings_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT // 3,
            text_id='indicator_sound_settings_text_component',
            text='INDICATOR SOUND SETTINGS',
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.LARGE_FONT_SIZE,
            is_bold=True,
            is_muted=self.is_indicator_sound_muted,
        )

        is_enabled_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2 - 120,
            coordinate_y=Constants.SCREEN_HEIGHT - 240,
            text_id='is_enabled_text_component',
            text='IS ENABLED',
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_muted=self.is_indicator_sound_muted,
        )

        current_state_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2 + 120,
            coordinate_y=Constants.SCREEN_HEIGHT - 240,
            text_id='current_state_text_component',
            text=self.current_state,
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.toggle_arrows,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_muted=self.is_indicator_sound_muted,
        )

        confirm_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2 - 200,
            coordinate_y=Constants.SCREEN_HEIGHT - 180,
            text_id='confirm_text_component',
            text='CONFIRM',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.handle_on_confirm_click,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_muted=self.is_indicator_sound_muted,
        )

        cancel_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2 + 200,
            coordinate_y=Constants.SCREEN_HEIGHT - 180,
            text_id='cancel_text_component',
            text='CANCEL',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.handle_on_cancel_click,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
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

        def _handle_left_arrow_click_event():
            self.handle_left_arrow_click()
            current_state_text_view.text = self.current_state

        def _handle_right_arrow_click_event():
            self.handle_right_arrow_click()
            current_state_text_view.text = self.current_state

        coordinate_x = Constants.SCREEN_WIDTH // 2 + 40
        coordinate_y = Constants.SCREEN_HEIGHT - 240

        left_arrow_points = [
            (coordinate_x + 10, coordinate_y - 20),
            (coordinate_x - 10, coordinate_y),
            (coordinate_x + 10, coordinate_y + 20),
        ]

        left_arrow = Arrows(
            coordinate_x=coordinate_x,
            coordinate_y=coordinate_y,
            arrow_id='left_arrow_component',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=_handle_left_arrow_click_event,
            points=left_arrow_points,
            is_muted=self.is_indicator_sound_muted,
        )

        right_arrow_points = [
            (coordinate_x + 150, coordinate_y - 20),
            (coordinate_x + 170, coordinate_y),
            (coordinate_x + 150, coordinate_y + 20),
        ]

        right_arrow = Arrows(
            coordinate_x=coordinate_x,
            coordinate_y=coordinate_y,
            arrow_id='right_arrow_component',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=_handle_right_arrow_click_event,
            points=right_arrow_points,
            is_muted=self.is_indicator_sound_muted,
        )

        text_view_list = [
            indicator_sound_settings_text_view,
            is_enabled_text_view,
            current_state_text_view,
            confirm_text_view,
            cancel_text_view,
            footer,
        ]

        arrow_view_list = [
            left_arrow,
            right_arrow,
        ]
        
        while self.is_running:
            self.window.fill(Constants.WHITE)

            for text_view in text_view_list:
                text_view.display(surface=self.window)
                text_view.update()

            if self.should_display_arrows:
                for arrow_view in arrow_view_list:
                    arrow_view.display(surface=self.window)
                    arrow_view.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.exit()

            pg.display.update()
            self.clock.tick(Constants.FPS)
