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

        self.coin_image = pygame.image.load('imgs/coin.png').convert_alpha()
        self.coin_rect = self.coin_image.get_rect()

        self.coin_rect.bottomright = (self.settings.WIDTH-50, self.settings.HEIGHT-5)
        
        self.coin_score_font = pygame.font.SysFont("freesans", 16)
        self.coin_score_text = self.coin_score_font.render(str(0), True, (0,0,0))
        self.coin_score_rect = self.coin_score_text.get_rect()
        self.coin_score_rect.bottomleft = (self.settings.WIDTH-45, self.settings.HEIGHT-10)


    def blitme(self, coins, screen):
        self.score_text = self.font.render(str(int(self.score/2)), True, (0,0,0))
        screen.blit(self.score_text, self.rect)

        self.coin_score_text = self.coin_score_font.render(str(coins), True, (0,0,0))
    
        screen.blit(self.coin_score_text, self.coin_score_rect)
        screen.blit(self.coin_image, self.coin_rect)



