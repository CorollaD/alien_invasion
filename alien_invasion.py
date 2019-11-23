import pygame
from pygame.sprite import Group

from settings import Settings 
from ship import Ship 
from alien import Alien
import game_functions as gf 
from bullet import Bullet 
from game_stats import GameStats 

def run_game():
    # initilized pygame settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # creats an stored example
    stats = GameStats(ai_settings)
    alien = Alien(ai_settings, screen)
    # create an ship
    ship = Ship(ai_settings, screen)
    # create an group used to stored bullet
    bullets = Group()
    aliens = Group()
    # create alien group
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start game main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

if __name__ == '__main__':
    run_game()