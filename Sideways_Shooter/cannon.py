import pygame 
from pygame.sprite import Sprite

class Cannon(Sprite):
    """A class to manage the cannon"""

    def __init__(self, ai_game):
        """Initialize the cannon and set the starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the image and get its rect
        self.image = pygame.image.load('C:/Users/Khyr/Desktop/CIT228/Sideways_Shooter/images/cannon.bmp')
        self.rect = self.image.get_rect()

        #Start each new cannon at the left of the screen
        self.rect.bottomleft = self.screen_rect.bottomleft

        #Store a decimal value for the cannon's horizontal position
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update cannon position based on movement flag"""
        #Update the ship's y value, not the rect
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.settings.cannon_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.cannon_speed

        #Update rect object from self.x.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        """Draw the cannon at current location"""
        self.screen.blit(self.image, self.rect)

    def center_cannon(self):
        """Center the cannon on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)