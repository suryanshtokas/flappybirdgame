import pygame

import settings


class BlueBird:
    def __init__(self):
        self.settings = settings.Settings()
        self.load_images()

        self.rect = self.mid_flap_rect

        # Set position of bird to center
        self.rect.center = (self.settings.WIDTH//2, self.settings.HEIGHT//2)

        self.jump_offset = 4

        self.jump_speed = self.settings.JUMP_HEIGHT - self.jump_offset
        self.jumping = False

    def jump(self):
        if self.jumping:
            self.rect.centery -= self.jump_speed
            self.jump_speed -= self.settings.FALLING_SPEED
            if self.jump_speed <= 0:
                self.jumping = False
                self.jump_speed = self.settings.JUMP_HEIGHT - self.jump_offset

    def blitme(self, screen):
        screen.blit(self.mid_flap, self.rect)

    def load_images(self):
        self.mid_flap = pygame.image.load(self.settings.BLUE_BIRD_DIRS[1]).convert_alpha()
        self.mid_flap_rect = self.mid_flap.get_rect()

        self.up_flap = pygame.image.load(self.settings.BLUE_BIRD_DIRS[2]).convert_alpha()
        self.up_flap_rect = self.up_flap.get_rect()

        self.down_flap = pygame.image.load(self.settings.BLUE_BIRD_DIRS[0]).convert_alpha()
        self.down_flap_rect = self.down_flap.get_rect()