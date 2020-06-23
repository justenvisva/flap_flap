import pygame
from flap_flap_settings import *
from pygame.locals import *

vec = pygame.math.Vector2


class player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.rect = pygame.Surface(30, 30)
        self.image = pygame.Surface.get_rect()
        self.pos = vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def fly(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.image.y -= 10
