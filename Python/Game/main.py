# ==============================================
# file:main.py
# version: 1.0
# desc: a game of ship pvp powered by Python
# auther: TJRのTanga
# create date: 9/19/2023
# update date: 9/21/2023
# ==============================================
import sys
sys.path.append('./modules')
import pygame
import modules.funcs as funs
from modules.Options import Options
from modules.objs.ship import Ship
from modules.objs.alien import Alien
from modules.objs.stats import GameStats
from modules.objs.scoreboard import ScoreBoard
from pygame.sprite import Group
from modules.objs.stats import GameStats
from modules.objs.Button import Button


"""
    the function of start game
"""


def startGame():
    # Pygame init & create objects
    pygame.init()
    pygame.display.set_caption("Flying Shots")
    opts = Options()
    screen = pygame.display.set_mode((opts.screen_width, opts.screen_height))
    stats = GameStats(opts)
    sb = ScoreBoard(opts, screen, stats)
    ship = Ship(opts, screen)
    bullets = Group()
    aliens = Group()

    funs.create_fleet(opts, screen,ship,aliens)
    alien = Alien(opts, screen)

    pygame.display.set_caption("Alien Defense")
    play_Button = Button(opts, screen, "Play")


    # the loop for keeping game run
    while 1:
        funs.check_events(opts, screen,stats,play_Button,ship, aliens,bullets)
        if stats.game_active:
            funs.update_ship(ship)
            funs.update_aliens(opts,stats,screen,ship,aliens,bullets)
            funs.update_bullets(opts,screen,ship,aliens, bullets)
        funs.update_screen(opts,screen,stats,sb,ship,aliens,bullets,play_Button)




# Code Run!!!
if __name__ != "main":
    startGame()
