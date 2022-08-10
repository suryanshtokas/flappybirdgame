 # Third-Party Imports
import pygame

# Local Imports
from scripts.settings import Settings
from scripts.background import Background
from scripts.bird import BlueBird
from scripts.floor import Floor
from scripts.pipes import Pipe
from scripts.score import Score
from scripts.coin import Coin
import scripts.functions as game_functions


# Initialize pygame and settings
pygame.init() # Pygame
settings = Settings() # Settings 

# Make Clocks, Screen, Set Basic Properties
CLOCK = pygame.time.Clock() # Clock
SCREEN = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT)) # Screen
pygame.display.set_caption(settings.TITLE) # Window Title

# Initialize the bird, floor, background class
background = Background() # Background
blue_bird = BlueBird() # Bird
floor = Floor() # Floor
score = Score() # For Scoring
pipes = pygame.sprite.Group() # For all pipes
coins = pygame.sprite.Group() # For all coins

# Timer for generation of pipes
timer = pygame.USEREVENT + 1 
pygame.time.set_timer(timer, 1200)

# Main Loop Flag
RUN = True
while RUN:
    # Run game at chosen FPS
    CLOCK.tick(settings.FPS)

    # Storing all events in events variable
    events = pygame.event.get()

    # Show, Animate and Manage User Inputs
    game_functions.show(background, pipes, floor, score, blue_bird, coins, SCREEN, settings)
    game_functions.animate(settings, background, floor)
    game_functions.manage_events(events, blue_bird, Pipe, pipes, timer, coins, Coin, settings)


    # If the game is not paused, then update everything          
    if not settings.PAUSE:
        game_functions.update(blue_bird, settings, pipes, floor, coins, score)
    # If the game is paused, then show the pause screen
    else:        
        game_functions.pauseScreen(settings, SCREEN)


    # Updating the display
    pygame.display.update()