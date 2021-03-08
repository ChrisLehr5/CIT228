import pygame 
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set the starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the image and get its rect
        self.image = pygame.image.load('C:/Users/Khyr/Desktop/CIT228/Sideways_Shooter/images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the left of the screen
        self.rect.centery = self.screen_rect.centery

        #Store a decimal value for the ship's horizontal position
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship position based on movement flag"""
        #Update the ship's y value, not the rect
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.ship_speed

        #Update rect object from self.x.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)