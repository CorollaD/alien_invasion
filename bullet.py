import pygame
from pygame.sprite import Sprite 


class Bullet(Sprite):
    # one class to control bullet 
    def __init__(self, ai_settings, screen, ship):
        # create an an bullet class in ship's location
        super(Bullet, self).__init__()
        self.screen = screen

        # create an box on (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # stored float indicate bullet's location
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # moving bullet up 
        # update the float indicate bullet
        self.y -= self.speed_factor
        # update the loc of bullet
        self.rect.y = self.y

    def draw_bullet(self):
        # draw bullets on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)