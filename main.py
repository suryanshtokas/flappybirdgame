import pygame

from settings import Settings


# Initialize pygame and settings
pygame.init()
settings = Settings()


screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)

run = True

bg_image = pygame.image.load(settings.BG_IMAGE_DIR)
bg_image_2 = bg_image

x_pos_bg = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(bg_image, (x_pos_bg,0))
    screen.blit(bg_image_2, (x_pos_bg+settings.WIDTH, 0)) 

    x_pos_bg -= settings.SCROLLING_VELOCITY
    if x_pos_bg == 0-settings.WIDTH:
        x_pos_bg = 0

    pygame.display.update()

