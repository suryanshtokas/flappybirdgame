# Third-Party Imports
import pygame

# Local Imports
from settings import Settings
from background import Background
from bird import BlueBird
from floor import Floor
from pipes import Pipe
from score import Score


# Initialize pygame and settings
pygame.init() # Pygame
settings = Settings() # Settings 

# Make Clocks, Screen, Set Basic Properties
CLOCK = pygame.time.Clock() # Clock
SCREEN = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT)) # Screen
pygame.display.set_caption(settings.TITLE) # Window Title

# Initialize the bird, floor, background class
background = Background()
blue_bird = BlueBird()
floor = Floor()
score = Score()

ITR = 0

pipes = pygame.sprite.Group()

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 1200)

# Main Loop Flag
RUN = True
while RUN:
    CLOCK.tick(settings.FPS)

    background.blitme(SCREEN)
    pipes.draw(SCREEN)
    floor.blitme(SCREEN)
    score.blitme(SCREEN)

    if settings.FALLING_SPEED == 2.4:
        background.scroll()
        floor.animate() 

    blue_bird.rect.centery += settings.FALLING_SPEED
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                blue_bird.jumping = True
        elif event.type == timer:
            pipes.add(Pipe(None, 1000,settings.HEIGHT-110))
            pipes.add(Pipe("face_down",1000, 0))

    blue_bird.touched_floor(floor, score)
    blue_bird.bump_ceiling()

    blue_bird.jump()
    settings.FALLING_SPEED += blue_bird.pipe_check(pipes, score)

    blue_bird.blitme(SCREEN, ITR)

    if settings.FALLING_SPEED == 2.4:
        pipes.update()
 

    # for scoring
    for pipe in pipes:
        if blue_bird.rect.left > pipe.rect.right and pipe.scored:
            pipe.scored = False
            score.score += 1

    ITR += 1
    if ITR == 60:
        ITR = 0
    pygame.display.update()