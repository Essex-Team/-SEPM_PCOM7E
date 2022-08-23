import i18n
import datetime
import pygame as pg
from python_lib.utils import Utils
from python_lib.constants import Constants
from python_lib.screens.Screen import Screen
from python_lib.screens.BattleScene import BattleScene
from python_lib.screens.RestrictionWarningScreen import RestrictionWarningScreen

class StartScreen(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        super().__init__(
            window=window,
            clock=clock,
            screen_title=i18n.t('app.screens.start.title'),
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
        self.time_limit_settings = {
            "start_time": "00:00",
            "end_time": "00:00",
        }
        self.load_time_limit_from_json()
        self.load_language_settings_from_json()

    def load_time_limit_from_json(self):
        self.time_limit_settings = Utils.loadContentFromJSON(
            Utils.getAssetPath(f'configs/{Constants.TIME_LIMIT_JSON_FILENAME}')
        )

    def load_language_settings_from_json(self):
        language_settings = Utils.loadContentFromJSON(
            Utils.getAssetPath(f'configs/{Constants.LANGUAGE_SETTINGS_JSON_FILENAME}')
        )
        i18n.set('locale', language_settings['locale'] or 'en')

    @property
    def is_playing_game_allowed(self) -> bool:
        start_time = self.time_limit_settings['start_time']
        end_time = self.time_limit_settings['end_time']

        if start_time == '00:00' and end_time == '00:00':
            return True

        current = datetime.datetime.now().time()
        start = datetime.datetime.strptime(start_time, '%H:%S').time()
        end = datetime.datetime.strptime(end_time, '%H:%S').time()

        return start <= current <= end
    
    def show_battle_scene(self):
        battle_scene: BattleScene = BattleScene(
            window=self.window,
            clock=self.clock,
        )
        battle_scene.display()

    def show_restriction_warning_screen(self):
        restriction_warning_screen: RestrictionWarningScreen = RestrictionWarningScreen(
            window=self.window,
            clock=self.clock,
        )
        restriction_warning_screen.display()

    def display(self):
        if self.is_playing_game_allowed:
            self.show_battle_scene()
        else:
            self.show_restriction_warning_screen()
