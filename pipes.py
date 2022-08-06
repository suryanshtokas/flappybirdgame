import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, orient, x,y):
        super(Pipe, self).__init__()
        self.image = pygame.image.load('imgs/pipe-green.png').convert_alpha()

        if orient == "face_down":
            self.image = pygame.transform.rotate(self.image, 180)

        self.rect = self.image.get_rect()

        self.rect.center = (x,y)

    def update(self):
        self.rect.right -= 5
        if self.rect.right < 0:
            self.kill()



        
