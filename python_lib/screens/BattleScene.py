import pygame
import random
import types
from python_lib.constants import Constants

from python_lib.components.Buttons import Button
from python_lib.components.GameObject import Character
from datetime import datetime

# Define window size and title
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pygame Game"

# Create pygame window object
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Set window background to white
window.fill((0, 0, 0))
clock = pygame.time.Clock()

# Battle Button
battle_buttons = pygame.sprite.Group()
characters = pygame.sprite.Group()

# Battle Buttons Graphic
odd_even = Button(
    button_id="odd_even",
    image_list={
        "basic": pygame.image.load("../../assets/images/buttons/odd_even_button.png"),
        "hovered": pygame.image.load("../../assets/images/buttons/odd_even_button_hovered.png"),
        "clicked": pygame.image.load("../../assets/images/buttons/odd_even_button_clicked.png")
    },
    x=150,
    y=380,
    scale=0.5
)

odd = Button(
    button_id="odd",
    image_list={
        "basic": pygame.image.load("../../assets/images/buttons/odd.png"),
        "hovered": pygame.image.load("../../assets/images/buttons/odd_hovered.png"),
        "clicked": pygame.image.load("../../assets/images/buttons/odd_clicked.png")
    },
    x=250,
    y=380,
    scale=0.5
)
odd.is_visible = False
odd_even.show_after_is_pressed.append(odd)

even = Button(
    button_id="even",
    image_list={
        "basic": pygame.image.load("../../assets/images/buttons/even.png"),
        "hovered": pygame.image.load("../../assets/images/buttons/even_hovered.png"),
        "clicked": pygame.image.load("../../assets/images/buttons/even_clicked.png")
    },
    x=500,
    y=380,
    scale=0.5
)
even.is_visible = False
odd_even.show_after_is_pressed.append(even)

battle_buttons.add(odd_even)
battle_buttons.add(odd)
battle_buttons.add(even)

# Characters
player = Character(
    coordinate_x=80,
    coordinate_y=100,
    animations={
        "idle": {
            "images": [
                '../../assets/images/character/player_idle_0.png',
                '../../assets/images/character/player_idle_1.png',
                '../../assets/images/character/player_idle_2.png',
                '../../assets/images/character/player_idle_3.png',
                '../../assets/images/character/player_idle_4.png',
                '../../assets/images/character/player_idle_5.png',
                '../../assets/images/character/player_idle_6.png',
                '../../assets/images/character/player_idle_7.png'
            ],
            "duration_in_seconds": 4,
            "scale": 2
        },
        "attack": {
            "images": [
                '../../assets/images/character/player_attack_0.png',
                '../../assets/images/character/player_attack_1.png',
                '../../assets/images/character/player_attack_2.png',
                '../../assets/images/character/player_attack_3.png',
                '../../assets/images/character/player_attack_4.png'
            ],
            "duration_in_seconds": 20,
            "scale": 2,
            "animation_speed": 0.2
        }
    },
    slower=True
)

characters.add(player)


# Game Mechanics
class Engine:
    def __init__(self):
        self.is_correct = False
        self.dice_1 = 0
        self.dice_2 = 0
        self.dice_sum = 0
        self.player_choice = None
        self.player_health = 100
        self.enemy_health = 100


engine = Engine()


def calculate_bet(choices):
    # Button Depth
    tier_1 = ['odd_even']
    tier_2 = ['odd', 'even']
    correct = False
    engine.player_choice = choices

    crit_bonus = 0
    engine.dice_1 = random.randint(1, 6)
    engine.dice_2 = random.randint(1, 6)
    engine.dice_sum = engine.dice_1 + engine.dice_2

    is_even = True if engine.dice_sum % 2 == 0 else False
    is_odd = True if engine.dice_sum % 2 == 1 else False

    if (is_even and choices == 'even') or (is_odd and choices == 'odd'):
        correct = True
        crit_bonus = 5

    for i in battle_buttons:
        if i.button_id in tier_1:
            i.is_visible = True
        else:
            i.is_visible = False

    print(engine.dice_1, engine.dice_2, engine.dice_sum, engine.player_choice)

    engine.is_correct = correct

    if engine.is_correct:
        print("Correct!")
    else:
        print("Incorrect!")

    return crit_bonus


odd.assign_callback(calculate_bet)
even.assign_callback(calculate_bet)

# To time event
time_of_event = None

if __name__ == '__main__':
    # Loop pygame state until user quits
    done = False
    while not done:
        # clock.tick(15)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # window.fill(0)
        window.fill(Constants.WHITE)

        there_was_an_event = False

        if engine.is_correct:
            player.attack()
            time_of_event = datetime.now()
            engine.is_correct = False

        if time_of_event is not None:
            second_diff = (datetime.now() - time_of_event).total_seconds()
            if player.current_animations.isFinished and second_diff > 0.5:
                player.current_animations.stop()
                time_of_event = None
                player.idle()

        for i in battle_buttons:
            if i.is_visible:
                i.draw(window)
                i.update()

        for i in characters:
            i.draw(window)

        # Update game state
        # Draw game state
        pygame.display.update()
        pygame.time.Clock().tick(30)
