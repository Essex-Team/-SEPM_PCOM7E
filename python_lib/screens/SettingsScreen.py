import pygame as pg
from python_lib.constants import Constants
from python_lib.components.Texts import Texts
from python_lib.screens.Screen import Screen
from python_lib.screens.ParentControlScreen import ParentControlScreen
from python_lib.screens.SetIndicatorSoundScreen import SetIndicatorSoundScreen

class SettingsScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Settings',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
        self.is_running = True

    def show_parent_control_screen(self):
        parent_control_screen: ParentControlScreen = ParentControlScreen(
            window=self.window,
            clock=self.clock,
        )
        parent_control_screen.display()

    def show_setting_indicator_sound_screen(self):
        set_indicator_sound_screen: SetIndicatorSoundScreen = SetIndicatorSoundScreen(
            window=self.window,
            clock=self.clock,
        )
        set_indicator_sound_screen.display()

    def exit(self):
        self.is_running = False

    def display(self):
        settings_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT // 3,
            text_id='settings_text_component',
            text='SETTINGS',
            color=Constants.TEXT_COLOR,
            font=Constants.FONT,
            font_size=Constants.LARGE_FONT_SIZE,
            is_bold=True,
        )

        parent_control_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 280,
            text_id='parent_control_text_component',
            text='PARENT CONTROL',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.show_parent_control_screen,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
        )

        setting_indicator_sound_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 240,
            text_id='setting_indicator_sound_text_component',
            text='INDICATOR SOUND SETTINGS',
            color=Constants.TEXT_COLOR,
            high_light_color=Constants.TEXT_HIGH_LIGHT_COLOR,
            on_click_event=self.show_setting_indicator_sound_screen,
            font=Constants.FONT,
            font_size=Constants.NORMAL_FONT_SIZE,
            is_bold=True,
        )

        back_to_main_text_view = Texts(
            coordinate_x=Constants.SCREEN_WIDTH // 2,
            coordinate_y=Constants.SCREEN_HEIGHT - 200,
            text_id='back_to_main_text_component',
            text='BACK TO MAIN MENU',
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
            settings_text_view,
            parent_control_text_view,
            setting_indicator_sound_text_view,
            back_to_main_text_view,
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
