import pygame as pg
from python_lib.constants import Constants
from python_lib.components.Texts import Texts
from python_lib.screens.Screen import Screen
from python_lib.screens.ParentControlScreen import ParentControlScreen

class SettingsScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Settings',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )

    def show_parent_control_screen(self):
        parent_control_screen: ParentControlScreen = ParentControlScreen(
            window=self.window,
            clock=self.clock,
        )
        parent_control_screen.display()

    def display(self):
        running = True
        while running:
            self.window.fill(Constants.WHITE)

            settings_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT // 3,
                text_id='settings_text_component',
                text='SETTINGS',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.LARGE_FONT_SIZE,
                is_bold=True,
            )

            settings_text_view.display(surface=self.window)

            parent_control_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 260,
                text_id='parent_control_text_component',
                text='PARENT CONTROL',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
                is_bold=True,
            )

            parent_control_text_view.display(surface=self.window)

            back_to_main_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 220,
                text_id='back_to_main_text_component',
                text='BACK TO MAIN MENU',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
                is_bold=True,
            )

            back_to_main_text_view.display(surface=self.window)

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
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False

                if parent_control_text_view.check_has_user_clicked(event):
                    self.show_parent_control_screen()

                if back_to_main_text_view.check_has_user_clicked(event):
                    running = False

            pg.display.update()
            self.clock.tick(Constants.FPS)
