import random
import pygame as pg
import time

from datetime import datetime
from python_lib.utils import Utils
from python_lib.constants import Constants
from python_lib.screens.Screen import Screen
from python_lib.components.Buttons import Button
from python_lib.components.Character import Character

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

        self.parry_sound = pg.mixer.Sound(Utils.getAssetPath('sounds/misc/parry.wav'))

    def update(self):
        if self.player_is_correct is True and self.enemy_is_correct is True:
            self.parry_sound.play()
            self.player_is_correct = False
            self.enemy_is_correct = False

class BattleScene(Screen):

    def __init__(self, window: pg.surface.Surface, clock: pg.time.Clock):
        self.dice_rolled = None
        self.player_choices = None
        self.enemy_choices = None

        super().__init__(
            window=window,
            clock=clock,
            screen_title='Battle',
            screen_width=Constants.SCREEN_WIDTH,
            screen_height=Constants.SCREEN_HEIGHT,
        )
        self.initializeGame()
    
    def initializeGame(self):
        self.font = pg.font.Font(Utils.getAssetPath('fonts/pixel/PixelEmulator-xq08.ttf'), Constants.EXTRA_SMALL_FONT_SIZE)

        pg.mixer.music.load(Utils.getAssetPath('sounds/music/Ludum_Dare _8_-_Track_4.wav'))
        pg.mixer.music.set_volume(0.05)
        pg.mixer.music.play(loops=-1)

        # Battle Button
        self.battle_buttons = pg.sprite.Group()
        self.characters = pg.sprite.Group()

        # Battle Buttons Graphic
        # Odd Even Group
        # self.odd_even = Button(
        #     button_id="odd_even",
        #     image_list={
        #         "basic": pg.image.load(Utils.getAssetPath("images/buttons/odd_even_button.png")),
        #         "hovered": pg.image.load(Utils.getAssetPath("images/buttons/odd_even_button_hovered.png")),
        #         "clicked": pg.image.load(Utils.getAssetPath("images/buttons/odd_even_button_clicked.png"))
        #     },
        #     x=150,
        #     y=380,
        #     scale=0.5
        # )

        screen_width, screen_height = pg.display.get_surface().get_size()

        self.odd = Button(
            button_id="odd",
            image_list={
                "basic": pg.image.load(Utils.getAssetPath("images/buttons/odd.png")),
                "hovered": pg.image.load(Utils.getAssetPath("images/buttons/odd_hovered.png")),
                "clicked": pg.image.load(Utils.getAssetPath("images/buttons/odd_clicked.png"))
            },
            x=((screen_width - 100)/8) + (((screen_width - 100)/6) * 1) - 25,
            y=380,
            scale=0.5
        )
        # self.odd.is_visible = True
        # self.odd_even.show_after_is_pressed.append(self.odd)

        self.even = Button(
            button_id="even",
            image_list={
                "basic": pg.image.load(Utils.getAssetPath("images/buttons/even.png")),
                "hovered": pg.image.load(Utils.getAssetPath("images/buttons/even_hovered.png")),
                "clicked": pg.image.load(Utils.getAssetPath("images/buttons/even_clicked.png"))
            },
            x=((screen_width - 100)/8) + (((screen_width - 100)/6) * 2) - 25,
            y=380,
            scale=0.5
        )
        # self.even.is_visible = False
        # self.odd_even.show_after_is_pressed.append(self.even)

        # High Low Group
        # self.high_low = Button(
        #     button_id="high_low",
        #     image_list={
        #         "basic": pg.image.load(Utils.getAssetPath("images/buttons/high_low.png")),
        #         "hovered": pg.image.load(Utils.getAssetPath("images/buttons/high_low_hovered.png")),
        #         "clicked": pg.image.load(Utils.getAssetPath("images/buttons/high_low_clicked.png"))
        #     },
        #     x=500,
        #     y=380,
        #     scale=0.5
        # )

        self.high = Button(
            button_id="high",
            image_list={
                "basic": pg.image.load(Utils.getAssetPath("images/buttons/high.png")),
                "hovered": pg.image.load(Utils.getAssetPath("images/buttons/high_hovered.png")),
                "clicked": pg.image.load(Utils.getAssetPath("images/buttons/high_clicked.png"))
            },
            x=((screen_width - 100)/8) + (((screen_width - 100)/6) * 3) - 25,
            y=380,
            scale=0.5
        )
        # self.high.is_visible = False
        # self.high_low.show_after_is_pressed.append(self.high)

        self.low = Button(
            button_id="low",
            image_list={
                "basic": pg.image.load(Utils.getAssetPath("images/buttons/low.png")),
                "hovered": pg.image.load(Utils.getAssetPath("images/buttons/low_hovered.png")),
                "clicked": pg.image.load(Utils.getAssetPath("images/buttons/low_clicked.png"))
            },
            x=((screen_width - 100)/8) + (((screen_width - 100)/6) * 4) - 25,
            y=380,
            scale=0.5
        )
        # self.low.is_visible = False
        # self.high_low.show_after_is_pressed.append(self.low)

        # self.battle_buttons.add(self.odd_even)
        self.battle_buttons.add(self.odd)
        self.battle_buttons.add(self.even)

        # self.battle_buttons.add(self.high_low)
        self.battle_buttons.add(self.low)
        self.battle_buttons.add(self.high)

        # Characters
        self.player = Character(
            coordinate_x=150,
            coordinate_y=100,
            animations={
                "idle": {
                    "images": [
                        Utils.getAssetPath('images/character/player_idle_0.png'),
                        Utils.getAssetPath('images/character/player_idle_1.png'),
                        Utils.getAssetPath('images/character/player_idle_2.png'),
                        Utils.getAssetPath('images/character/player_idle_3.png'),
                        Utils.getAssetPath('images/character/player_idle_4.png'),
                        Utils.getAssetPath('images/character/player_idle_5.png'),
                        Utils.getAssetPath('images/character/player_idle_6.png'),
                        Utils.getAssetPath('images/character/player_idle_7.png')
                    ],
                    "duration_in_seconds": 4,
                    "scale": 2
                },
                "attack": {
                    "images": [
                        Utils.getAssetPath('images/character/player_attack_0.png'),
                        Utils.getAssetPath('images/character/player_attack_1.png'),
                        Utils.getAssetPath('images/character/player_attack_2.png'),
                        Utils.getAssetPath('images/character/player_attack_3.png'),
                        Utils.getAssetPath('images/character/player_attack_4.png')
                    ],
                    "duration_in_seconds": 20,
                    "scale": 2,
                    "animation_speed": 0.2
                },
                "take_hit": {
                    "images": [
                        Utils.getAssetPath('images/character/player_take_hit_0.png'),
                        Utils.getAssetPath('images/character/player_take_hit_1.png'),
                        Utils.getAssetPath('images/character/player_take_hit_2.png'),
                        Utils.getAssetPath('images/character/player_take_hit_3.png')
                    ],
                    "duration_in_seconds": 20,
                    "scale": 2,
                    "animation_speed": 0.2
                }
            },
            slower=True
        )

        self.player.take_hit_sound = pg.mixer.Sound(Utils.getAssetPath('sounds/misc/player_take_hit.wav'))

        self.enemy = Character(
            coordinate_x=250,
            coordinate_y=90,
            animations={
                "idle": {
                    "images": [
                        Utils.getAssetPath('images/character/enemy_idle_0.png'),
                        Utils.getAssetPath('images/character/enemy_idle_1.png'),
                        Utils.getAssetPath('images/character/enemy_idle_2.png'),
                        Utils.getAssetPath('images/character/enemy_idle_3.png')
                    ],
                    "duration_in_seconds": 4,
                    "scale": 2,
                    "flipped": True,
                    "animation_speed": 0.5
                },
                "attack": {
                    "images": [
                        Utils.getAssetPath('images/character/enemy_attack_0.png'),
                        Utils.getAssetPath('images/character/enemy_attack_1.png'),
                        Utils.getAssetPath('images/character/enemy_attack_2.png'),
                        Utils.getAssetPath('images/character/enemy_attack_3.png')
                    ],
                    "duration_in_seconds": 4,
                    "scale": 2,
                    "flipped": True,
                    "animation_speed": 0.5
                },
                "take_hit": {
                    "images": [
                        Utils.getAssetPath('images/character/enemy_take_hit_0.png'),
                        Utils.getAssetPath('images/character/enemy_take_hit_1.png'),
                        Utils.getAssetPath('images/character/enemy_take_hit_2.png'),
                    ],
                    "duration_in_seconds": 4,
                    "scale": 2,
                    "flipped": True,
                    "animation_speed": 0.5
                }
            },
            slower=True
        )

        self.enemy.take_hit_sound = pg.mixer.Sound(Utils.getAssetPath('sounds/misc/enemy_take_hit.wav'))

        self.characters.add(self.player)
        self.characters.add(self.enemy)

        self.engine: Engine = Engine()

        self.odd.assign_callback(self.calculate_bet)
        self.even.assign_callback(self.calculate_bet)
        self.high.assign_callback(self.calculate_bet)
        self.low.assign_callback(self.calculate_bet)

        # To time event
        self.time_of_event = None

    def calculate_bet(self, choices):
        # Button Depth
        tier_1 = ['odd_even', 'high_low']
        tier_2 = ['odd', 'even', 'high', 'low']
        correct = False
        self.engine.player_choice = choices
        self.player_choices = choices

        self.engine.there_was_an_event = True

        crit_bonus = 0
        self.engine.dice_1 = random.randint(1, 6)
        self.engine.dice_2 = random.randint(1, 6)
        self.engine.dice_sum = self.engine.dice_1 + self.engine.dice_2

        self.dice_rolled = str(self.engine.dice_sum)

        is_even = True if self.engine.dice_sum % 2 == 0 else False
        is_odd = True if self.engine.dice_sum % 2 == 1 else False
        is_lowest = True if self.engine.dice_sum in [i for i in range(1, 7)] else False
        is_highest = True if self.engine.dice_sum in [i for i in range(7, 13)] else False

        print(
            "is_even: ", is_even, "\n"
            "is_odd: ", is_odd, "\n"
            "is_lowest: ", is_lowest, "\n"
            "is_highest: ", is_highest, "\n"
        )

        # Check player choices
        if (is_even and choices == 'even') or \
                (is_odd and choices == 'odd') or \
                (is_lowest and choices == 'low') or \
                (is_highest and choices == 'high'):
            self.engine.player_is_correct = True

        # Check enemy choices
        enemy_choice = random.choice(['even', 'odd', 'low', 'high'])
        self.enemy_choices = enemy_choice
        if (is_even and enemy_choice == 'even') or \
                (is_odd and enemy_choice == 'odd') or \
                (is_lowest and enemy_choice == 'low') or \
                (is_highest and enemy_choice == 'high'):
            self.engine.enemy_is_correct = True

        # Combine player and enemy result

        damage = 0

        if self.engine.player_is_correct:
            if not self.engine.enemy_is_correct:
                self.engine.enemy_health -= 10
        else:
            if self.engine.enemy_is_correct:
                self.engine.player_health -= 10

        for i in self.battle_buttons:
            i.is_visible = True

        #
        # if self.engine.player_is_correct:
        #     print("Correct!")
        # else:
        #     print("Incorrect!")

        text = None
        if self.engine.player_is_correct:
            text = "Player is correct!"
        else:
            text = "Player is incorrect!"

        if self.engine.enemy_is_correct:
            text = text + " Enemy is correct!"
        else:
            text = text + " Enemy is incorrect!"

        print(text)

        self.engine.is_player_turn = not self.engine.is_player_turn

        return crit_bonus

    def display(self):
        # Loop pygame state until user quits
        done = False
        while not done:
            # self.clock.tick(15)
            # Event handling
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

            # window.fill(0)
            self.window.fill(Constants.WHITE)

            if self.engine.is_player_turn:
                text = "Player's Turn"
            else:
                text = "Enemy's Turn"

            # Turn information text
            # turn_text = self.font.render(text, True, Constants.BLACK)
            # textRect = turn_text.get_rect()
            # textRect.center = (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 18)

            # Player's health text
            player_health_text = self.font.render("Player: " + str(self.engine.player_health), True, Constants.BLACK)
            player_health_text_rect = player_health_text.get_rect()
            player_health_text_rect.topleft = (Constants.SCREEN_WIDTH / 4, Constants.SCREEN_HEIGHT / 15)

            # Enemy's health text
            enemy_health_text = self.font.render("Enemy: " + str(self.engine.enemy_health), True, Constants.BLACK)
            enemy_health_text_rect = enemy_health_text.get_rect()
            enemy_health_text_rect.topright = (Constants.SCREEN_WIDTH / 4 * 3, Constants.SCREEN_HEIGHT / 15)

            if self.engine.enemy_health <= 0 or self.engine.player_health <= 0:
                if self.engine.enemy_health <= 0 or self.engine.enemy_health < self.engine.player_health:
                    announcement_text = self.font.render("Player Win!", True, Constants.BLACK)
                else:
                    announcement_text = self.font.render("Enemy Win!", True, Constants.BLACK)

                announcement_text_rect = announcement_text.get_rect()
                announcement_text_rect.center = (
                    Constants.SCREEN_WIDTH / 2,
                    550
                )
                self.window.blit(announcement_text, announcement_text_rect)

                done = True

            if done is True:
                pg.display.update()
                self.engine.update()
                pg.time.Clock().tick(30)
                pg.mixer.music.stop()

                time.sleep(3)

            if self.engine.player_is_correct is True:
                self.player.current_animations.stop()
                self.enemy.current_animations.stop()
                self.player.attack()

                if self.engine.enemy_is_correct is True:
                    self.enemy.attack()
                else:
                    self.enemy.take_hit()

                self.time_of_event = datetime.now()
                self.engine.player_is_correct = False
                self.engine.enemy_is_correct = False
            else:
                if self.engine.enemy_is_correct is True:
                    self.enemy.current_animations.stop()
                    self.enemy.attack()

                    if self.engine.player_is_correct is True:
                        self.player.attack()
                    else:
                        self.player.take_hit()

                    self.time_of_event = datetime.now()
                    self.engine.enemy_is_correct = False
                    self.engine.player_is_correct = False

            if self.time_of_event is not None:
                second_diff = (datetime.now() - self.time_of_event).total_seconds()
                if self.player.current_animations.isFinished and second_diff > 0.5:
                    self.player.current_animations.stop()
                    self.time_of_event = None
                    self.player.idle()
                    self.enemy.idle()

            if self.engine.there_was_an_event:
                self.engine.there_was_an_event = False

            for i in self.battle_buttons:
                if i.is_visible:
                    i.draw(self.window)
                    i.update()

            for i in self.characters:
                i.draw(self.window)

            # Update game state
            # Draw game state
            # self.window.blit(turn_text, textRect)
            self.window.blit(player_health_text, player_health_text_rect)
            self.window.blit(enemy_health_text, enemy_health_text_rect)

            # Dice roll result
            if self.dice_rolled is not None:
                dice_rolled_text = self.font.render("Dice: " + self.dice_rolled, True, Constants.BLACK)
                dice_rolled_text_rect = dice_rolled_text.get_rect()
                dice_rolled_text_rect.center = (
                    (Constants.SCREEN_WIDTH / 2) - 250,
                    450
                )
                self.window.blit(dice_rolled_text, dice_rolled_text_rect)

            if self.player_choices is not None:
                player_choices_text = self.font.render("Player: " + self.player_choices, True, Constants.BLACK)
                player_choices_text_rect = player_choices_text.get_rect()
                player_choices_text_rect.center = (
                    Constants.SCREEN_WIDTH / 2,
                    450
                )
                self.window.blit(player_choices_text, player_choices_text_rect)

            if self.enemy_choices is not None:
                enemy_choices_text = self.font.render("Enemy: " + self.enemy_choices, True, Constants.BLACK)
                enemy_choices_text_rect = enemy_choices_text.get_rect()
                # enemy_choices_text_rect.topright = (
                #     ((Constants.SCREEN_WIDTH - 100) / 8) + (((Constants.SCREEN_HEIGHT - 100) / 6) * 3) - 25,
                #     450
                # )
                enemy_choices_text_rect.center = (
                    (Constants.SCREEN_WIDTH / 2) + 250,
                    450
                )
                self.window.blit(enemy_choices_text, enemy_choices_text_rect)

            pg.display.update()
            self.engine.update()
            pg.time.Clock().tick(30)
