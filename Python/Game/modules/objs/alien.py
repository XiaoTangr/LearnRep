# ==============================================
# file:ship.py
# desc: the class of ship
# auther: 一颗橘子唐
# ==============================================
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, opts,screen):

        super().__init__()
        self.screen = screen
        self.opts = opts

        self.image = pygame.image.load('Assets/imgs/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        if opts.evn == "dev":
            print ("Alien width: {0},height: {1}".format(self.rect.width,self.rect.height))
        self.x = float(self.rect.x)

    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.x += (self.opts.alien_speed_factor * self.opts.alien_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True