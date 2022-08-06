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

        self.animation_list = []
        for i in range(60):
            if i <= 20:
                self.animation_list.append(self.up_flap)
            elif i <= 40:
                self.animation_list.append(self.mid_flap)
            else:
                self.animation_list.append(self.down_flap)

        self.is_dead = False

    def jump(self):
        if self.jumping:
            self.rect.centery -= self.jump_speed
            self.jump_speed -= self.settings.FALLING_SPEED
            if self.jump_speed <= 0:
                self.jumping = False
                self.jump_speed = self.settings.JUMP_HEIGHT - self.jump_offset

    def touched_floor(self, floor):
        if (pygame.Rect.colliderect(self.rect, floor.rect) or pygame.Rect.colliderect(self.rect, floor.rect_2)) and not self.is_dead:
            quit()
        else:
            if self.rect.bottom >= self.settings.HEIGHT:
                quit()
    
    def die(self, bg, floor, settings):
        self.is_dead = True
    
        # Stop everything from moving
        bg.stop_scroll = True
        floor.stop_scroll = True

        # Fall down fast   
        settings.FALLING_SPEED *= 3
    
    def bump_ceiling(self):
        if self.rect.top <= 0:
            self.rect.top = 0

    def blitme(self, screen, itr):
        if not self.is_dead:
            screen.blit(self.animation_list[itr], self.rect)
        else:
            screen.blit(pygame.transform.rotate(self.up_flap, -45), self.rect)

    def load_images(self):
        self.mid_flap = pygame.image.load(self.settings.BLUE_BIRD_DIRS[1]).convert_alpha()
        self.mid_flap_rect = self.mid_flap.get_rect()

        self.up_flap = pygame.image.load(self.settings.BLUE_BIRD_DIRS[2]).convert_alpha()
        self.up_flap_rect = self.up_flap.get_rect()

        self.down_flap = pygame.image.load(self.settings.BLUE_BIRD_DIRS[0]).convert_alpha()
        self.down_flap_rect = self.down_flap.get_rect()