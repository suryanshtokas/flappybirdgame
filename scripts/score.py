import pygame

from scripts.settings import Settings


class Score:
    def __init__(self):
        self.settings = Settings()

        self.font = pygame.font.SysFont("freesans", 64)

        self.score = 0

        self.score_text = self.font.render(str(self.score), True, (0,0,0))
        self.rect = self.score_text.get_rect()

        self.rect.center = (self.settings.WIDTH//2, self.settings.HEIGHT - 50)

    def blitme(self, screen):
        self.score_text = self.font.render(str(int(self.score/2)), True, (0,0,0))
        screen.blit(self.score_text, self.rect)