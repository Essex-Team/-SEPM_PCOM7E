import pygame
import random
import types
from python_lib.constants import Constants

from python_lib.components.Buttons import Button
from python_lib.components.Character import Character
from datetime import datetime

# Define window size and title
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pygame Game"

# Create pygame window object
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
font = pygame.font.Font('../../assets/fonts/pixel/PixelEmulator-xq08.ttf', 14)

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
    coordinate_x=150,
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
        },
        "take_hit": {
            "images": [
                '../../assets/images/character/player_take_hit_0.png',
                '../../assets/images/character/player_take_hit_1.png',
                '../../assets/images/character/player_take_hit_2.png',
                '../../assets/images/character/player_take_hit_3.png'
            ],
            "duration_in_seconds": 20,
            "scale": 2,
            "animation_speed": 0.2
        }
    },
    slower=True
)

player.take_hit_sound = pygame.mixer.Sound('../../assets/sounds/misc/player_take_hit.wav')

enemy = Character(
    coordinate_x=250,
    coordinate_y=90,
    animations={
        "idle": {
            "images": [
                '../../assets/images/character/enemy_idle_0.png',
                '../../assets/images/character/enemy_idle_1.png',
                '../../assets/images/character/enemy_idle_2.png',
                '../../assets/images/character/enemy_idle_3.png'
            ],
            "duration_in_seconds": 4,
            "scale": 2,
            "flipped": True,
            "animation_speed": 0.5
        },
        "attack": {
            "images": [
                '../../assets/images/character/enemy_attack_0.png',
                '../../assets/images/character/enemy_attack_1.png',
                '../../assets/images/character/enemy_attack_2.png',
                '../../assets/images/character/enemy_attack_3.png'
            ],
            "duration_in_seconds": 4,
            "scale": 2,
            "flipped": True,
            "animation_speed": 0.5
        },
        "take_hit": {
            "images": [
                '../../assets/images/character/enemy_take_hit_0.png',
                '../../assets/images/character/enemy_take_hit_1.png',
                '../../assets/images/character/enemy_take_hit_2.png',
            ],
            "duration_in_seconds": 4,
            "scale": 2,
            "flipped": True,
            "animation_speed": 0.5
        }
    },
    slower=True
)

enemy.take_hit_sound = pygame.mixer.Sound('../../assets/sounds/misc/enemy_take_hit.wav')

characters.add(player)
characters.add(enemy)


# Game Mechanics
class Engine:
    def __init__(self):
        self.player_is_correct = False
        self.enemy_is_correct = False
        self.is_player_turn = True
        self.is_enemy_turn = not self.is_player_turn
        self.dice_1 = 0
        self.dice_2 = 0
        self.dice_sum = 0
        self.player_choice = None
        self.player_health = 100
        self.enemy_health = 100
        self.there_was_an_event = False

        self.parry_sound = pygame.mixer.Sound('../../assets/sounds/misc/parry.wav')

    def update(self):
        if self.player_is_correct is True and self.enemy_is_correct is True:
            self.parry_sound.play()
            self.player_is_correct = False
            self.enemy_is_correct = False


engine = Engine()


def calculate_bet(choices):
    # Button Depth
    tier_1 = ['odd_even']
    tier_2 = ['odd', 'even']
    correct = False
    engine.player_choice = choices

    engine.there_was_an_event = True

    crit_bonus = 0
    engine.dice_1 = random.randint(1, 6)
    engine.dice_2 = random.randint(1, 6)
    engine.dice_sum = engine.dice_1 + engine.dice_2

    is_even = True if engine.dice_sum % 2 == 0 else False
    is_odd = True if engine.dice_sum % 2 == 1 else False
    is_lowest = True if engine.dice_sum in [i for i in range(1, 7)] else False
    is_highest = True if engine.dice_sum in [i for i in range(7, 13)] else False

    # Check player choices
    if (is_even and choices == 'even') or \
            (is_odd and choices == 'odd') or \
            (is_lowest and choices == 'lowest') or \
            (is_highest and choices == 'highest'):
        engine.player_is_correct = True

    # Check enemy choices
    enemy_choice = random.choice(['even', 'odd', 'lower', 'highest'])
    if (is_even and enemy_choice == 'even') or \
            (is_odd and enemy_choice == 'odd') or \
            (is_lowest and enemy_choice == 'lowest') or \
            (is_highest and enemy_choice == 'highest'):
        engine.enemy_is_correct = True

    # Combine player and enemy result

    damage = 0

    if engine.player_is_correct:
        if not engine.enemy_is_correct:
            engine.enemy_health -= 10
    else:
        if engine.enemy_is_correct:
            engine.player_health -= 10

    for i in battle_buttons:
        if i.button_id in tier_1:
            i.is_visible = True
        else:
            i.is_visible = False

    if engine.player_is_correct:
        print("Correct!")
    else:
        print("Incorrect!")

    engine.is_player_turn = not engine.is_player_turn

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

        if engine.is_player_turn:
            text = "Player's Turn"
        else:
            text = "Enemy's Turn"

        # Turn information text
        turn_text = font.render(text, True, Constants.BLACK)
        textRect = turn_text.get_rect()
        textRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 18)

        # Player's health text
        player_health_text = font.render("Player: " + str(engine.player_health), True, Constants.BLACK)
        player_health_text_rect = player_health_text.get_rect()
        player_health_text_rect.topleft = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 15)

        # Enemy's health text
        enemy_health_text = font.render("Enemy: " + str(engine.enemy_health), True, Constants.BLACK)
        enemy_health_text_rect = enemy_health_text.get_rect()
        enemy_health_text_rect.topright = (WINDOW_WIDTH / 4 * 3, WINDOW_HEIGHT / 15)

        if engine.player_is_correct is True:
            player.current_animations.stop()
            enemy.current_animations.stop()
            player.attack()

            if engine.enemy_is_correct is True:
                enemy.attack()
            else:
                enemy.take_hit()

            time_of_event = datetime.now()
            engine.player_is_correct = False
            engine.enemy_is_correct = False
        else:
            if engine.enemy_is_correct is True:
                enemy.current_animations.stop()
                enemy.attack()

                if engine.player_is_correct is True:
                    player.attack()
                else:
                    player.take_hit()

                time_of_event = datetime.now()
                engine.enemy_is_correct = False
                engine.player_is_correct = False

        if time_of_event is not None:
            second_diff = (datetime.now() - time_of_event).total_seconds()
            if player.current_animations.isFinished and second_diff > 0.5:
                player.current_animations.stop()
                time_of_event = None
                player.idle()
                enemy.idle()

        if engine.there_was_an_event:
            engine.there_was_an_event = False

        for i in battle_buttons:
            if i.is_visible:
                i.draw(window)
                i.update()

        for i in characters:
            i.draw(window)

        # Update game state
        # Draw game state
        window.blit(turn_text, textRect)
        window.blit(player_health_text, player_health_text_rect)
        window.blit(enemy_health_text, enemy_health_text_rect)
        pygame.display.update()
        engine.update()
        pygame.time.Clock().tick(30)

        if engine.enemy_health <= 0 or engine.player_health <= 0:
            done = True
