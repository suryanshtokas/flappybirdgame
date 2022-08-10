import pygame

from scripts.settings import Settings


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Coin, self).__init__()

        self.animation_list = []
        self.img1 = pygame.image.load('imgs/coin1.png').convert_alpha()
        self.img2 = pygame.image.load('imgs/coin2.png').convert_alpha()
        self.img3 = pygame.image.load('imgs/coin3.png').convert_alpha()
        self.img4 = pygame.image.load('imgs/coin4.png').convert_alpha()
        self.img5 = pygame.image.load('imgs/coin5.png').convert_alpha()
        self.img6 = pygame.image.load('imgs/coin6.png').convert_alpha()
        self.img7 = pygame.image.load('imgs/coin7.png').convert_alpha()       

        self.rect = self.img1.get_rect()
        self.rect.topleft = (x,y)

        self.ITR = 0

        for i in range(1, 64):
            if i < 9:
                self.animation_list.append(pygame.transform.scale(self.img1, (32,32)))
            elif i < 18:
                self.animation_list.append(pygame.transform.scale(self.img2, (28,32)))
            elif i < 27:
                self.animation_list.append(pygame.transform.scale(self.img3, (24,32)))
            elif i < 36:
                self.animation_list.append(pygame.transform.scale(self.img4, (10,32)))
            elif i < 45:
                self.animation_list.append(pygame.transform.scale(self.img5, (24,32)))
            elif i < 54:
                self.animation_list.append(pygame.transform.scale(self.img6, (28,32)))
            elif i <= 63:
                self.animation_list.append(pygame.transform.scale(self.img7, (32,32)))


    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()
        
        self.ITR += 1
        if self.ITR == 63:
            self.ITR = 0

        self.image = self.animation_list[self.ITR]