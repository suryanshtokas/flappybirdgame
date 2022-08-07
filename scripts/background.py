import pygame

from scripts.settings import Settings


class Background:
    def __init__(self):
        self.settings = Settings()

        self.image = self.settings.BG_IMAGE.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect_2 = self.image.get_rect()

        self.rect_2.left += self.settings.WIDTH

        self.stop_scroll = False

    def scroll(self):
        if not self.stop_scroll:
            self.rect.left -= self.settings.SCROLLING_VELOCITY
            self.rect_2.left -= self.settings.SCROLLING_VELOCITY
            if self.rect.left < 0-self.settings.WIDTH:
                self.rect.left += self.settings.WIDTH
                self.rect_2.left += self.settings.WIDTH

    def blitme(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image, self.rect_2)