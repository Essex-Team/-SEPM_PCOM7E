import pygame as pg
from .Screen import Screen
from python_lib.constants import Constants
from python_lib.components.Texts import Texts
from python_lib.screens.SetTimeLimitScreen import SetTimeLimitScreen

class ParentControlScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Parent Control',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
    
    def show_set_time_limit_screen(self):
        set_time_limit_screen: SetTimeLimitScreen = SetTimeLimitScreen(
            window=self.window,
            clock=self.clock,
        )
        set_time_limit_screen.display()

    def display(self):
        running = True
        while running:
            self.window.fill(Constants.WHITE)

            parent_control_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT // 3,
                text_id='parent_control_text_component',
                text='PARENT CONTROL',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.LARGE_FONT_SIZE,
                is_bold=True,
            )

            parent_control_text_view.display(surface=self.window)

            set_time_limit_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 260,
                text_id='set_time_limit_text_component',
                text='SET TIME LIMIT',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
                is_bold=True,
            )

            set_time_limit_text_view.display(surface=self.window)

            back_to_settings_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 220,
                text_id='back_to_settings_text_component',
                text='BACK TO MAIN SETTINGS',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
                is_bold=True,
            )

            back_to_settings_text_view.display(surface=self.window)

            footer = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 100,
                state='ready',
                text_id='footer_text_component',
                text='Team 1, Software Engineering Project Management @ 2022',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.SMALL_FONT_SIZE,
            )

            footer.display(surface=self.window)

            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False

                if set_time_limit_text_view.check_has_user_clicked(event):
                    self.show_set_time_limit_screen()

                if back_to_settings_text_view.check_has_user_clicked(event):
                    running = False

            pg.display.update()
            self.clock.tick(Constants.FPS)

