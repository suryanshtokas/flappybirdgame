import pygame

from scripts.settings import Settings


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Coin, self).__init__()
        self.image = pygame.image.load("imgs/coin.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()