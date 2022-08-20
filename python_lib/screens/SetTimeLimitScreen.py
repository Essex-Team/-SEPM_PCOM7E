import pygame as pg
from .Screen import Screen
from python_lib.utils import Utils
from python_lib.constants import Constants
from python_lib.components.Texts import Texts

class SetTimeLimitScreen(Screen):

    TIME_LIMIT_JSON_FILENAME = 'time_limit.json'

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title='Set Time Limit',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
        self.time_limit_form = {
            "start_time": "00:00",
            "end_time": "00:00",
        }
        self.load_time_limit_from_json()

    def load_time_limit_from_json(self):
        self.time_limit_form = Utils.loadContentFromJSON(SetTimeLimitScreen.TIME_LIMIT_JSON_FILENAME)

    def handle_save_time_limit_to_json(self):
        Utils.saveContentToJSON(SetTimeLimitScreen.TIME_LIMIT_JSON_FILENAME, self.time_limit_form)

    def display(self):
        running = True
        while running:
            self.window.fill(Constants.WHITE)

            set_time_limit_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT // 3,
                state='display',
                text_id='set_time_limit_text_component',
                text='SET TIME LIMIT',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.LARGE_FONT_SIZE,
                is_bold=True,
            )

            set_time_limit_text_view.display(surface=self.window)

            between_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT - 300,
                state='display',
                text_id='between_text_component',
                text='BETWEEN',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
            )

            between_text_view.display(surface=self.window)

            start_time_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2 - 100,
                coordinate_y=Constants.SCREEN_HEIGHT - 240,
                state='display',
                text_id='start_time_text_component',
                text=self.time_limit_form['start_time'],
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
            )

            start_time_text_view.display(surface=self.window)

            end_time_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2 + 100,
                coordinate_y=Constants.SCREEN_HEIGHT - 240,
                state='display',
                text_id='end_time_text_component',
                text=self.time_limit_form['end_time'],
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
            )

            end_time_text_view.display(surface=self.window)

            confirm_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2 - 200,
                coordinate_y=Constants.SCREEN_HEIGHT - 180,
                state='display',
                text_id='confirm_text_component',
                text='CONFIRM',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
            )

            confirm_text_view.display(surface=self.window)

            cancel_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2 + 200,
                coordinate_y=Constants.SCREEN_HEIGHT - 180,
                state='display',
                text_id='cancel_text_component',
                text='CANCEL',
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
            )

            cancel_text_view.display(surface=self.window)

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

                if confirm_text_view.check_has_user_clicked(event):
                    self.handle_save_time_limit_to_json()
                    running = False

                if cancel_text_view.check_has_user_clicked(event):
                    running = False

            pg.display.update()
            self.clock.tick(Constants.FPS)
