class GameStats:
    """Track statistics for Sideways Shooters"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        #High Score should never be reset
        self.high_score = 0
        self.settings = ai_game.settings
        self.reset_stats()
        #Start Sideways Shooter in an active state 
        #self.game_active = True 

        #Start Sideways Shooter in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during game"""
        self.cannons_left = self.settings.cannon_limit
        self.score = 0
        self.level = 1    
    