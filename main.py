# Third-Party Imports
import pygame

# Local Imports
from settings import Settings
from background import Background
from bird import BlueBird
from floor import Floor

# Initialize pygame and settings
pygame.init() # Pygame
settings = Settings() # Settings 

# Make Clocks, Screen, Set Basic Properties
CLOCK = pygame.time.Clock() # Clock
SCREEN = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT)) # Screen
pygame.display.set_caption(settings.TITLE) # Window Title

# For side scrolling
X_POS_BG = 0

# Initialize the bird, floor, background class
background = Background()
blue_bird = BlueBird()
floor = Floor()

ITR = 0

# Main Loop Flag
RUN = True
while RUN:
    CLOCK.tick(settings.FPS)

    background.blitme(SCREEN)
    floor.blitme(SCREEN)

    background.scroll()
    floor.animate() 

    blue_bird.rect.centery += settings.FALLING_SPEED
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                blue_bird.jumping = True
            elif event.key == pygame.K_x:
                blue_bird.die(background, floor, settings)

    blue_bird.touched_floor(floor)
    blue_bird.bump_ceiling()

    blue_bird.jump()
  
    blue_bird.blitme(SCREEN, ITR)

    X_POS_BG -= settings.SCROLLING_VELOCITY
    if X_POS_BG == 0-settings.WIDTH:
        X_POS_BG = 0

    ITR += 1
    if ITR == 60:
        ITR = 0

    pygame.display.update()