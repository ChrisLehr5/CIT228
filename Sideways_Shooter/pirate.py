import pygame
from pygame.sprite import Sprite 

class Pirate(Sprite):
    """A class to represent a single pirate ship"""

    def __init__(self, ai_game):
        """Initialize the alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the pirate image and set its rect attribute 
        self.image = pygame.image.load('C:/Users/Khyr/Desktop/CIT228/Sideways_Shooter/images/pirate.bmp')
        self.rect = self.image.get_rect()

       # Start pirate near the middle of the screen
        self.rect.centerx = self.rect.right
        self.rect.centery = self.rect.centery

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the pirate ship to the left or right"""
        self.x += (self.settings.pirate_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x 

    def check_edges(self):
        """Return True if pirate is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
