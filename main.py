# Third-Party Imports
import pygame

# Local Imports
from settings import Settings
from bird import BlueBird

# Initialize pygame and settings
pygame.init() # Pygame
settings = Settings() # Settings 

# Make Clocks, Screen, Set Basic Properties
CLOCK = pygame.time.Clock() # Clock
SCREEN = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT)) # Screen
pygame.display.set_caption(settings.TITLE) # Window Title

# For side scrolling
X_POS_BG = 0

# Initialize the bird class
blue_bird = BlueBird()

# Main Loop Flag
RUN = True
while RUN:
    CLOCK.tick(settings.FPS)

    blue_bird.rect.centery += settings.FALLING_SPEED

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                blue_bird.jumping = True


    blue_bird.jump()

    SCREEN.blit(settings.BG_IMAGE, (X_POS_BG,0))
    SCREEN.blit(settings.BG_IMAGE, (X_POS_BG+settings.WIDTH, 0)) 
    
    blue_bird.blitme(SCREEN)

    X_POS_BG -= settings.SCROLLING_VELOCITY
    if X_POS_BG == 0-settings.WIDTH:
        X_POS_BG = 0

    pygame.display.update()

