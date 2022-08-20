import pygame
import types

class Button(pygame.sprite.Sprite):
    def __init__(self, button_id, image_list, x, y, scale=1, show_after_is_pressed=list()):
        super().__init__()
        self.button_id = button_id
        self.x = x
        self.y = y
        self.width = image_list['basic'].get_width()
        self.height = image_list['basic'].get_height()
        self.scale = scale
        self.image_list = image_list
        self.image = self.get_image(image_list['basic'])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked_sound = pygame.mixer.Sound("assets/sounds/buttons/button_clicked.wav")
        self.hovered_sound = pygame.mixer.Sound("assets/sounds/buttons/button_hovered.wav")
        self.clicked_sound.set_volume(0.06)
        self.hovered_sound.set_volume(0.06)
        self.is_previously_hovered = False
        self.is_hovered = False
        self.is_clicked = False
        self.is_visible = True
        self.show_after_is_pressed = show_after_is_pressed
        self.do_after_is_pressed = None
        self.update()

    def get_image(self, image):
        return pygame.transform.scale(image, (int(self.width * self.scale), int(self.height * self.scale)))

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_previously_hovered = self.is_hovered
            self.is_hovered = True

            if self.is_hovered and not self.is_previously_hovered:
                self.hovered_sound.play()

            if pygame.mouse.get_pressed()[0] == 1 and self.is_clicked is False:
                self.is_clicked = True
            else:
                self.is_clicked = False
        else:
            self.is_hovered = False

        if pygame.mouse.get_pressed()[0] == 0:
            self.is_clicked = False

        if self.is_hovered:
            self.image = self.get_image(self.image_list['hovered'])
        else:
            self.image = self.get_image(self.image_list['basic'])

        if self.is_hovered and self.is_clicked:
            self.image = self.get_image(self.image_list['clicked'])
            self.clicked_sound.play()
            self.is_visible = False
            self.action()

        surface.blit(self.image, (self.rect.x, self.rect.y))

    def action(self):
        if len(self.show_after_is_pressed) > 0:
            for i in self.show_after_is_pressed:
                i.is_visible = True

        if self.do_after_is_pressed is not None:
            self.do_after_is_pressed()

    def assign_callback(self, callback):
        self.do_after_is_pressed = types.MethodType(callback, self.button_id)
