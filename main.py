import pygame as pg
from python_lib.constants import Constants
from python_lib.screens.MainMenuScreen import MainMenuScreen

# Define title
WINDOW_TITLE = "Pygame Game"

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
