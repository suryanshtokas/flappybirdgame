import pygame
import random

def pauseScreen(settings, screen):
    transparency_overlay = pygame.Surface((settings.WIDTH, settings.HEIGHT))
    transparency_overlay.set_alpha(150)
    transparency_overlay.fill(settings.TRANSPARENCY_OVERLAY_COLOR)
    screen.blit(transparency_overlay, (0,0))

    pause_screen_width = 400
    pause_screen_height = 225
    pygame.draw.rect(screen, (211,211,211), pygame.Rect(settings.WIDTH//2-pause_screen_width//2, settings.HEIGHT//2-pause_screen_height//2,
                                                            pause_screen_width,pause_screen_height))
    pause_font = pygame.font.SysFont("freesans", 32)
    pause_text = pause_font.render("PAUSED!", True, (0,0,0))
    pause_rect = pause_text.get_rect()
    pause_rect.center = (settings.WIDTH//2, settings.HEIGHT//2)

    pause_info_font = pygame.font.SysFont("freesans", 16)
    pause_info = pause_info_font.render("Press any key or do a mouse click to continue", True, (0,0,0))
    pause_info_rect = pause_info.get_rect()
    pause_info_rect.center = (settings.WIDTH//2, (settings.HEIGHT//2) + 50)

    screen.blit(pause_text, pause_rect)
    screen.blit(pause_info, pause_info_rect)

def show(background, pipes, floor, score, blue_bird, screen, settings):
    background.blitme(screen)
    pipes.draw(screen)
    floor.blitme(screen)
    score.blitme(screen)
    blue_bird.blitme(screen ,settings.ITR)
    

def animate(settings, bg, floor):
    if settings.FALLING_SPEED == 2.4 and not settings.PAUSE:
        bg.scroll()
        floor.animate()

def manage_events(events, blue_bird, pipe, pipes, timer, settings):

    for event in events:
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key != pygame.K_ESCAPE:
                settings.PAUSE = False # To get of the pause screen by pressing any key
            if event.key == pygame.K_SPACE:
                blue_bird.jumping = True
            elif event.key == pygame.K_ESCAPE:
                if settings.PAUSE:
                    settings.PAUSE = False
                else:
                    settings.PAUSE = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            settings.PAUSE = False
        elif event.type == timer and not settings.PAUSE:
            temp = random.randint(0,90)
            pipes.add(pipe(None, 1000,settings.HEIGHT-110-temp))
            pipes.add(pipe("face_down",1000, -temp))


def update(blue_bird, settings, pipes, floor, score):
    blue_bird.rect.centery += settings.FALLING_SPEED

    blue_bird.touched_floor(floor, score)
    blue_bird.bump_ceiling()

    blue_bird.jump()
    settings.FALLING_SPEED += blue_bird.pipe_check(pipes, score)

    
    if settings.FALLING_SPEED == 2.4:
        pipes.update()


    settings.ITR += 1
    if settings.ITR == 60:
        settings.ITR = 0

    # for scoring
    for pipe in pipes:
        if blue_bird.rect.left > pipe.rect.right and pipe.scored:
            pipe.scored = False
            score.score += 1