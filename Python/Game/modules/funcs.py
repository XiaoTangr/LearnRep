# ==============================================
# file:funcs.py
# desc: the functions define
# auther: 一颗橘子唐
# ==============================================
import sys
from time import sleep
import pygame
from objs.bullet import Bullet
from objs.alien import Alien


"""
keyboard events listener functions
keydown
keyup
key & mouse
"""
def check_keydown_events(event,opts,screen, ship,bullets):
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_a or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_w or  event.key == pygame.K_SPACE:
        fire_bullet(opts,screen,ship,bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_a or  event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(opts,screen,stats,sb,play_Button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,opts,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(opts,screen,stats,sb,play_Button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(opts,screen,stats,sb,play_Button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked = play_Button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        opts.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)

        if play_Button.rect.collidepoint(mouse_x,mouse_y):
            stats.reset_stats()
            stats.game_active = True
            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()
            aliens.empty()
            bullets.empty()
            create_fleet(opts,screen,ship,aliens)
            ship.center_ship()



"""
objects update functions
screen 屏幕（窗口对象）
bullets 子弹对象
ship 飞船对象
"""
def update_screen(opts,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(opts.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(opts,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    # del bullet when it is out of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(opts,screen,stats,sb,ship,aliens,bullets)

    
    # if dev
    if opts.evn == "dev":
        print("max bullet:{0}\n shoted bullets:{1}".format(opts.bullets_allowed,len(bullets)))

def check_bullet_alien_collisions(opts,screen,stats,sb,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,opts.bullets_keep,True)
    if collisions:
        for aliens in collisions.values():

            stats.score += opts.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats,sb)
    if len(aliens) == 0:
        bullets.empty()
        stats.level += 1
        sb.prep_level()
        opts.increase_speed()
        create_fleet(opts,screen,ship,aliens)



def check_aliens_bottom(opts,stats,screen,sb,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(opts,stats,screen,sb,ship,aliens,bullets)
            break



def update_ship(ship):
    ship.update()


"""
function of shout bullets
@:param opts 设置参数
@:param screen 屏幕对象
@:param ship 飞船对象
@:param bullets 子弹对象
"""
def fire_bullet(opts,screen,ship,bullets):
    if opts.bullets_allowed == -1:
        new_bullet = Bullet(opts, screen, ship)
        bullets.add(new_bullet)
    elif len(bullets) < opts.bullets_allowed:
        new_bullet = Bullet(opts, screen, ship)
        bullets.add(new_bullet)

'''
外星人相关函数
'''
def get_number_aliens_x(opts,alien_width):
    available_space_x = opts.screen_width - (opts.alien_space_x_multiple * alien_width)
    number_aliens_x = int(available_space_x / (opts.alien_space_x_multiple * alien_width))
    return number_aliens_x

def get_number_rows(opts,ship_height,alien_height):
    available_space_y = opts.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (opts.alien_space_y_multiple * alien_height))
    return number_rows

def create_alien(opts,screen,aliens,alien_number,row_number):
    alien = Alien(opts, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width) * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(opts,screen,ship,aliens):
    alien = Alien(opts, screen)
    number_aliens_x = get_number_aliens_x(opts,alien.rect.width)
    number_rows = get_number_rows(opts,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(opts,screen,aliens,alien_number,row_number)

"""
相应飞船与外星人撞击事件 
"""
def ship_hit(opts,stats,screen,sb,ship,aliens,bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(opts,screen,ship,aliens)
        ship.center_ship()
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  



"""
# update aliens
"""
def update_aliens(opts,stats,screen,sb,ship,aliens,bullets):
    check_fleet_edges(opts,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(opts,stats,screen,sb,ship,aliens,bullets)
    check_aliens_bottom(opts,stats,screen,sb,ship,aliens,bullets)

def check_fleet_edges(opts,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_direction(opts,aliens)
            break

def change_alien_direction(opts,aliens):
    for alien in aliens.sprites():
        alien.rect.y += opts.alien_drop_speed
    opts.alien_direction *= -1

def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
