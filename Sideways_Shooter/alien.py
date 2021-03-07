import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    """A class to represent a single alien ship"""

    def __init__(self, ai_game):
        """Initialize the alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its rect attribute 
        self.image = pygame.image.load('C:/Users/Khyr/Desktop/CIT228/Sideways_Shooter/images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new aline near the top left of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizaontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien ship to up or down"""
        self.y -= (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.y = self.y 

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom or self.rect.top <= 0:
            return True
