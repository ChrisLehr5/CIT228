import pygame
from pygame.sprite import Sprite 

class Cannonball(Sprite):
    """A class to manage cannon balls fired from cannon"""

    def __init__(self, ai_game):
        """Create a cannon object"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.cannonball_color

        #Create a cannonball rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.cannonball_width,
            self.settings.cannonball_height)
        self.rect.midright = ai_game.cannon.rect.midright        

        #Store the cannonball location as a decimal value 
        self.x = float(self.rect.x) 
    
    def update(self):
        """Move the cannonball across the screen"""
        #Update the decimal position of the cannonball
        self.x += self.settings.cannonball_speed
        #Update the rect position 
        self.rect.x = self.x

    def draw_cannonball(self):
        """Draw the cannonball to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
