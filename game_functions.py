import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien 


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # respose key
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def fire_bullet(ai_settings, screen, ship, bullets):
    # create one bullet and add it to bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    

def check_keyup_events(event, ship):
    # respose release
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    # respose keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)          

def update_screen(ai_settings, screen, ship, aliens, bullets):
    # update images on screen and change to new screen 
    # every loop reflip the screen
    for bullet in bullets.sprites():
        bullet.draw_bullet() 

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    # let's the screen show it 
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()
    # delete bullet outside of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if len(aliens) == 0:
        # delete all bullets and new create an group of alien
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_rows(ai_settings, ship_height, alien_height):
    # account screen can hold how mang aliens
    available_space_y = (ai_settings.screen_height - 
                                    (3 * alien_height) -ship_height)
    number_rows = int(available_space_y / ( 2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    # account single column stored how many aliens
    available_space_x = ai_settings.screen_width -2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # create one alien and put it oon this line 
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    # create alien group
    # create one alien, and account single column stored how many aliens
    # alien's spacing is alien's width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create first column aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # create one alien and add into the column
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    # if alien arrived edges, adopt same ways
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    #  Move the entire group of aliens down and change their direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    # respose alien attack ship
    # reduce the ship by 1
    stats.ship_left -= 1

    # clear aliens and bullets
    aliens.empty()
    bullets.empty()

    # create an group of new aliens and set the ship in the center of bottom
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # time out 
    sleep(0.5)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    # Check if aliens have reached the bottom of the screen
    screen_rect = screen.get_rect()
    for alien in aliens.sprite():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings,stats, screen, ship, aliens, bullets):
    # Check if aliens are on the edge of the screen and update the location of the aliens
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    # test distance between alien and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
