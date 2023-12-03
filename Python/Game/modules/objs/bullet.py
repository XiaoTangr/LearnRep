# ==============================================
# file:bullet.pu
# desc: the class of bullet
# auther: 一颗橘子唐
# ==============================================
import pygame
from pygame.sprite import  Sprite

class Bullet(Sprite):
    #init
    def __init__(self,opts,screen,ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,opts.bullet_width,opts.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = opts.bullet_color
        self.speed_factor = opts.bullet_speed_factor
    # update bullet location
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    # drew bullet
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)