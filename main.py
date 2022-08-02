import pygame

pygame.init()


screen_width = 900
screen_height = 504

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")

run = True

bg_image = pygame.image.load(r'imgs/bg.png')
bg_image_2 = pygame.image.load(r'imgs/bg.png')

x_pos_bg = 0
scrolling_speed = 0.5

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(bg_image, (x_pos_bg,0))
    screen.blit(bg_image_2, (x_pos_bg+screen_width, 0)) 

    x_pos_bg -= scrolling_speed
    if x_pos_bg == 0-screen_width:
        x_pos_bg = 0

    pygame.display.update()

