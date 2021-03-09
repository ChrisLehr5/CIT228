import pygame

class Settings:
    """A class to store all the settings from Pirate Invasion"""

    def __init__(self):
        """Initialize games static settings"""
        #Screen settings 
        self.screen_width = 1200
        self.screen_height = 690
        self.bg_color = (62,164,236) 
        self.background_image= pygame.image.load('C:/Users/Khyr/Desktop/CIT228/Sideways_Shooter/images/background2.jpg')         

        #Cannon settings         
        self.cannon_limit = 3
        
        #Cannonball settings       
        self.cannonball_width = 8
        self.cannonball_height = 14
        self.cannonball_color = (0, 0, 0)
        self.cannonballs_allowed = 3

        #Pirate settings        
        self.fleet_drop_speed = 5

        #How quickly the game speeds up 
        self.speedup_scale = 1.1 

        #How quickly the pirate point values increase 
        self.score_scale = 1.5

        self.intitalize_dynamic_settings()       

    def intitalize_dynamic_settings(self):
        """Intitialize settings that change throughout the game"""
        self.cannon_speed = 1.5
        self.cannonball_speed = 2.5
        self.pirate_speed = 1.3

        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        #Scoring 
        self.pirate_points = 50
    
    def increase_speed(self):
        """Increase speed settings and pirate point values"""
        self.cannon_speed *= self.speedup_scale
        self.cannonball_speed *= self.speedup_scale 
        self.pirate_speed *= self.speedup_scale

        self.pirate_points = int(self.pirate_points * self.score_scale)
        print(self.pirate_points)