import pygame
import random
from flap_flap_settings import *
from flap_flap_sprite import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.working = True
        self.font_name = pygame.font.match_font(FONT_NAME)


    def new(self):
