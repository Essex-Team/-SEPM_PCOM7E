# TODO: Move to the ./screens/BattleScene.py
# import pygame
# import random
# import types

# from python_lib.components.Buttons import Button

# # Define window size and title
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# WINDOW_TITLE = "Pygame Game"

# # Create pygame window object
# pygame.init()
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption(WINDOW_TITLE)

# # Set window background to white
# window.fill((0, 0, 0))
# clock = pygame.time.Clock()

# # Battle Button
# battle_buttons = pygame.sprite.Group()

# # Battle Buttons Graphic
# odd_even = Button(
#     button_id="odd_even",
#     image_list={
#         "basic": pygame.image.load("assets/images/buttons/odd_even_button.png"),
#         "hovered": pygame.image.load("assets/images/buttons/odd_even_button_hovered.png"),
#         "clicked": pygame.image.load("assets/images/buttons/odd_even_button_clicked.png")
#     },
#     x=150,
#     y=500,
#     scale=0.5
# )

# odd = Button(
#     button_id="odd",
#     image_list={
#         "basic": pygame.image.load("assets/images/buttons/odd.png"),
#         "hovered": pygame.image.load("assets/images/buttons/odd_hovered.png"),
#         "clicked": pygame.image.load("assets/images/buttons/odd_clicked.png")
#     },
#     x=250,
#     y=500,
#     scale=0.5
# )
# odd.is_visible = False
# odd_even.show_after_is_pressed.append(odd)

# even = Button(
#     button_id="even",
#     image_list={
#         "basic": pygame.image.load("assets/images/buttons/even.png"),
#         "hovered": pygame.image.load("assets/images/buttons/even_hovered.png"),
#         "clicked": pygame.image.load("assets/images/buttons/even_clicked.png")
#     },
#     x=500,
#     y=500,
#     scale=0.5
# )
# even.is_visible = False
# odd_even.show_after_is_pressed.append(even)

# battle_buttons.add(odd_even)
# battle_buttons.add(odd)
# battle_buttons.add(even)


# # Game Mechanic
# def calculate_bet(choices):
#     # Button Depth
#     tier_1 = ['odd_even']
#     tier_2 = ['odd', 'even']
#     correct = False

#     crit_bonus = 0
#     dice_1 = random.randint(1, 6)
#     dice_2 = random.randint(1, 6)
#     dice_sum = dice_1 + dice_2

#     is_even = True if dice_sum % 2 == 0 else False

#     if (is_even and choices == 'even') or (not is_even and choices == 'odd'):
#         correct = True
#         crit_bonus = 5

#     for i in battle_buttons:
#         if i.button_id in tier_1:
#             i.is_visible = True
#         else:
#             i.is_visible = False

#     print(choices, dice_1, dice_2, dice_sum, correct)
#     return crit_bonus


# odd.assign_callback(calculate_bet)
# even.assign_callback(calculate_bet)

# if __name__ == '__main__':
#     # Loop pygame state until user quits
#     done = False
#     while not done:
#         # clock.tick(15)
#         # Event handling
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True

#         # if odd_even.is_visible:
#         #     odd_even.draw(window)
#         #     odd_even.update()

#         # window.fill(0)
#         window.fill(Constants.BLACK)

#         for i in battle_buttons:
#             if i.is_visible:
#                 i.draw(window)
#                 i.update()


#         # Update game state
#         # Draw game state
#         pygame.display.flip()

import sys
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
