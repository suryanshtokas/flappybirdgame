import pygame

from scripts.settings import Settings

class Floor:
    def __init__(self):
        self.settings = Settings()

        self.height = 112

        self.image = pygame.transform.scale(pygame.image.load(r'imgs/floor.png').convert_alpha(), (self.settings.WIDTH, self.height))
        self.rect = self.image.get_rect()

        self.rect_2 = self.image.get_rect()

        self.animate_vel = 7

        self.set_at_bottom()

        self.stop_scroll = False

    def set_at_bottom(self):
        self.rect.bottomleft = (0, self.settings.HEIGHT-1)
        self.rect_2.bottomleft = self.settings.WIDTH, self.settings.HEIGHT-1

    def animate(self):
        if not self.stop_scroll:
            self.rect.left -= self.animate_vel
            self.rect_2.left -= self.animate_vel
            if self.rect.left < 0-self.settings.WIDTH:
                self.rect.left += self.settings.WIDTH
                self.rect_2.left += self.settings.WIDTH

    def blitme(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image, self.rect_2)