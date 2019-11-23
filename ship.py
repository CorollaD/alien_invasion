import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        # initilized ship and set it original location
        self.screen = screen
        self.ai_settings = ai_settings

        # loading ship's image and get it shapes
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # let every ship in center of screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # center store decinumber
        self.center = float(self.rect.centerx)

        # moving tag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        # according to moving tag alter ship's location
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # according self.center update rect object
        self.rect.centerx = self.center

    def blitme(self):
        # blit ship in certain location
        self.screen.blit(self.image, self.rect)

    def center_ship():
        # let ship in the center
        self.center = self.screen_rect.centerx