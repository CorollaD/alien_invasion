import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    # indicate single alien class
    def __init__(self, ai_settings, screen):
        # initilized alien and set it location
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien's picture, and set rect belongs
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien in the top of screen in the first
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # stored alien's accurate location
        self.x = float(self.rect.x)

    def blitme(self):
        # blit alien in certain loction
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        # if alien's arrive edges,return True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # moving alien's to right or left
        self.x += (self.ai_settings.alien_speed_factor * 
                                self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
