# ==============================================
# file:ship.py
# desc: the class of ship
# auther: 一颗橘子唐
# ==============================================
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    # ship init
    def __init__(self, opts, screen, *args):
        super().__init__()
        self.screen = screen
        self.options = opts
        self.image = pygame.image.load("./Assets/imgs/ship.png")
        if len(args) >  0:
            self.image = pygame.image.load("./Assets/imgs/bullet.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    # update location of ship
    def update(self):
        # update the location of the ship
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.options.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.options.ship_speed_factor
        # update location depend on self.center
        self.rect.centerx = self.center  # type: ignore

    # Drew ship
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
