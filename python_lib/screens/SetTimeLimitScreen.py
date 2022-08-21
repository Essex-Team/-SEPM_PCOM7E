import pygame as pg
from datetime import datetime, timedelta
from python_lib.utils import Utils
from python_lib.constants import Constants
from python_lib.screens.Screen import Screen
from python_lib.components.Texts import Texts
from python_lib.components.Arrows import Arrows

class SetTimeLimitScreen(Screen):

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
        self.generate_time_options()

    def generate_time_options(self):
        start = datetime(1900,1,1,0,0,0)
        end = datetime(1900,1,2,0,0,0)
        seconds = (end - start).total_seconds()
        step = timedelta(minutes=30)

        self.time_options = []
        for i in range(0, int(seconds), int(step.total_seconds())):
            self.time_options.append((start + timedelta(seconds=i)).strftime("%H:%M"))

    def load_time_limit_from_json(self):
        self.time_limit_form = Utils.loadContentFromJSON(
            Utils.getAssetPath(f'configs/{Constants.TIME_LIMIT_JSON_FILENAME}'),
        )

    def handle_save_time_limit_to_json(self):
        start_time = self.time_limit_form['start_time']
        end_time = self.time_limit_form['end_time']

        start_time_idx = self.time_options.index(start_time)
        end_time_idx = self.time_options.index(end_time)

        if start_time_idx < end_time_idx:
            Utils.saveContentToJSON(
                Utils.getAssetPath(f'configs/{Constants.TIME_LIMIT_JSON_FILENAME}'),
                self.time_limit_form,
            )

    def get_next_available_option(self, current_selected_option, is_up=True):
        idx = self.time_options.index(current_selected_option)

        if (is_up and idx == len(self.time_options) - 1) or (not is_up and idx == 0):
            return self.time_options[0]
        
        if is_up:
            return self.time_options[idx + 1]

        return self.time_options[idx - 1]

    def handle_start_time_up_arrow_click(self):
        start_time = self.time_limit_form['start_time']
        next_start_time = self.get_next_available_option(start_time)
        self.time_limit_form['start_time'] = next_start_time

    def handle_start_time_down_arrow_click(self):
        start_time = self.time_limit_form['start_time']
        previous_start_time = self.get_next_available_option(start_time, is_up=False)
        self.time_limit_form['start_time'] = previous_start_time

    def handle_end_time_up_arrow_click(self):
        end_time = self.time_limit_form['end_time']
        next_end_time = self.get_next_available_option(end_time)
        self.time_limit_form['end_time'] = next_end_time

    def handle_end_time_down_arrow_click(self):
        end_time = self.time_limit_form['end_time']
        previous_end_time = self.get_next_available_option(end_time, is_up=False)
        self.time_limit_form['end_time'] = previous_end_time

    def display(self):
        running = True
        
        should_display_start_time_arrows = False
        should_display_end_time_arrows = False

        while running:
            self.window.fill(Constants.WHITE)

            set_time_limit_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2,
                coordinate_y=Constants.SCREEN_HEIGHT // 3,
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
                text_id='start_time_text_component',
                text=self.time_limit_form['start_time'],
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
            )

            start_time_text_view.display(surface=self.window)

            start_time_up_arrow = None
            start_time_down_arrow = None

            end_time_up_arrow = None
            end_time_down_arrow = None

            if should_display_start_time_arrows:
                coordinate_x = Constants.SCREEN_WIDTH // 2 - 100
                coordinate_y = Constants.SCREEN_HEIGHT - 240

                start_time_up_arrow_points = [
                    (coordinate_x - 20, coordinate_y - 20),
                    (coordinate_x, coordinate_y - 40),
                    (coordinate_x + 20, coordinate_y - 20),
                ]

                start_time_up_arrow = Arrows(
                    coordinate_x=coordinate_x,
                    coordinate_y=coordinate_y,
                    arrow_id='start_time_up_arrow_component',
                    color=Constants.BLACK,
                    points=start_time_up_arrow_points,
                )

                start_time_up_arrow.display(surface=self.window)

                start_time_down_arrow_points = [
                    (coordinate_x - 20, coordinate_y + 20),
                    (coordinate_x, coordinate_y + 40),
                    (coordinate_x + 20, coordinate_y + 20),
                ]

                start_time_down_arrow = Arrows(
                    coordinate_x=coordinate_x,
                    coordinate_y=coordinate_y,
                    arrow_id='start_time_down_arrow_component',
                    color=Constants.BLACK,
                    points=start_time_down_arrow_points,
                )

                start_time_down_arrow.display(surface=self.window)

            end_time_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2 + 100,
                coordinate_y=Constants.SCREEN_HEIGHT - 240,
                text_id='end_time_text_component',
                text=self.time_limit_form['end_time'],
                color=Constants.BLACK,
                font=Constants.FONT,
                font_size=Constants.NORMAL_FONT_SIZE,
            )

            end_time_text_view.display(surface=self.window)

            if should_display_end_time_arrows:
                coordinate_x = Constants.SCREEN_WIDTH // 2 + 100
                coordinate_y = Constants.SCREEN_HEIGHT - 240

                end_time_up_arrow_points = [
                    (coordinate_x - 20, coordinate_y - 20),
                    (coordinate_x, coordinate_y - 40),
                    (coordinate_x + 20, coordinate_y - 20),
                ]

                end_time_up_arrow = Arrows(
                    coordinate_x=coordinate_x,
                    coordinate_y=coordinate_y,
                    arrow_id='end_time_up_arrow_component',
                    color=Constants.BLACK,
                    points=end_time_up_arrow_points,
                )

                end_time_up_arrow.display(surface=self.window)

                end_time_down_arrow_points = [
                    (coordinate_x - 20, coordinate_y + 20),
                    (coordinate_x, coordinate_y + 40),
                    (coordinate_x + 20, coordinate_y + 20),
                ]

                end_time_down_arrow = Arrows(
                    coordinate_x=coordinate_x,
                    coordinate_y=coordinate_y,
                    arrow_id='end_time_down_arrow_component',
                    color=Constants.BLACK,
                    points=end_time_down_arrow_points,
                )

                end_time_down_arrow.display(surface=self.window)

            confirm_text_view = Texts(
                coordinate_x=Constants.SCREEN_WIDTH // 2 - 200,
                coordinate_y=Constants.SCREEN_HEIGHT - 180,
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

                if start_time_text_view.check_has_user_clicked(event):
                    should_display_start_time_arrows = not should_display_start_time_arrows

                if start_time_up_arrow is not None and start_time_up_arrow.check_has_user_clicked(event):
                    self.handle_start_time_up_arrow_click()

                if start_time_down_arrow is not None and start_time_down_arrow.check_has_user_clicked(event):
                    self.handle_start_time_down_arrow_click()

                if end_time_up_arrow is not None and end_time_up_arrow.check_has_user_clicked(event):
                    self.handle_end_time_up_arrow_click()

                if end_time_down_arrow is not None and end_time_down_arrow.check_has_user_clicked(event):
                    self.handle_end_time_down_arrow_click()

                if end_time_text_view.check_has_user_clicked(event):
                    should_display_end_time_arrows = not should_display_end_time_arrows

                if confirm_text_view.check_has_user_clicked(event):
                    self.handle_save_time_limit_to_json()
                    running = False

                if cancel_text_view.check_has_user_clicked(event):
                    running = False

            pg.display.update()
            self.clock.tick(Constants.FPS)
