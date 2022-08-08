import pygame

class Settings:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 504 + 108 # (110 for floor)

        self.TITLE = "Flappy Bird"

        self.BG_IMAGE = pygame.image.load(r'imgs/bg.png')

        self.SCROLLING_VELOCITY = 6

        self.JUMP_HEIGHT = 25

        self.FALLING_SPEED = 2.4

        self.FPS = 60

        self.PAUSE = False

        self.ITR = 0

        self.TRANSPARENCY_OVERLAY_COLOR = (211,211,211)

        self.BLUE_BIRD_DIRS = [
                    r"imgs/bluebird-downflap.png",
                    r"imgs/bluebird-midflap.png",
                    r"imgs/bluebird-upflap.png",
                ]


        self.RED_BIRD_DIRS = [
                    r"imgs/redbird-downflap.png",
                    r"imgs/redbird-midflap.png",
                    r"imgs/redbird-upflap.png",
                ]


