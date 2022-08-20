import pygame
import pyganim


class GameObject(pygame.sprite.Sprite):

    def __init__(self, coordinate_x: float, coordinate_y: float, animations=None):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.animations = animations
        pygame.sprite.Sprite.__init__(self)


class Character(GameObject):

    def __init__(self,
                 coordinate_x: float,
                 coordinate_y: float,
                 animations: dict,
                 slower: bool=False):
        self.state = 'idle'
        self.idle_animation = None
        self.attack_animation = None
        self.take_hit_animation = None
        self.animations = animations
        self.slower = slower
        self.construct_animations()
        self.current_animations = self.idle_animation
        self.current_animations.play()
        self.rect = self.current_animations.getRect()
        self.rect.topleft = (coordinate_x, coordinate_y)
        # self.rect.bottomleft = (coordinate_x, coordinate_y)
        super().__init__(coordinate_x, coordinate_y, animations)

        self.take_hit_sound=None

    def get_image(self, image, flipped=False, scale=1):
        _image = pygame.image.load(image).convert_alpha()
        if flipped:
            _image = pygame.transform.flip(_image, True, False)
        width = _image.get_width()
        height = _image.get_height()
        _image = pygame.transform.smoothscale(_image, (int(width * scale), int(height * scale)))
        return _image

    def construct_animations(self):
        # idle_sprite_sheet = self.animations['idle']
        # attack_sprite_sheet = self.animations['attack']
        # take_hit_sprite_sheet = self.animations['take_hit']

        for state, data in self.animations.items():
            duration_in_seconds = data.get('duration_in_seconds')
            scale = data.get('scale')
            animation_speed = data.get('animation_speed')
            flipped = data.get("flipped", False)
            sprites = list()
            for _image in data['images']:
                _single_sprite = (
                    self.get_image(image=_image, flipped=flipped, scale=scale), duration_in_seconds
                )
                sprites.append(_single_sprite)

            anim = pyganim.PygAnimation(sprites)

            if animation_speed is not None:
                anim._rate = animation_speed

            if state == 'idle':
                self.idle_animation = anim
            elif state == 'attack':
                self.attack_animation = anim
            else:
                self.take_hit_animation = anim

    def draw(self, surface):
        if self.state == 'idle':
            self.current_animations = self.idle_animation
        elif self.state == 'attack':
            self.current_animations = self.attack_animation
        else:
            self.current_animations = self.take_hit_animation

        self.rect = self.current_animations.getRect()
        self.rect.topleft = (self.coordinate_x, self.coordinate_y)
        self.current_animations.play()

        self.current_animations.blit(surface, (self.coordinate_x, self.coordinate_y))

    def attack(self):
        self.state = 'attack'

    def idle(self):
        self.state = 'idle'

    def take_hit(self):
        self.state = 'take_hit'
        self.take_hit_sound.play()
