import os
import i18n
import pygame as pg
from python_lib.constants import Constants
from python_lib.screens.MainMenuScreen import MainMenuScreen

i18n.load_path.append(
    os.path.join(
        os.path.abspath(os.curdir),
        'assets/locales',
    )
)

i18n.set('locale', 'en')
i18n.set('fallback', 'en')

# Define title
WINDOW_TITLE = i18n.t('app.windowTitle')

# Create pygame window object
pg.init()
window = pg.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
pg.display.set_caption(WINDOW_TITLE)

# Set window background to white
window.fill(Constants.WHITE)
clock = pg.time.Clock()

if __name__ == '__main__':
    mainMenuScreen = MainMenuScreen(window=window, clock=clock)
    mainMenuScreen.display()
