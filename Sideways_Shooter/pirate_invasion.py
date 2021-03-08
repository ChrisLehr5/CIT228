import sys
import pygame

from pygame import mixer 
from time import sleep
from button import Button
from settings import Settings 
from cannon import Cannon
from cannonball import Cannonball
from pirate import Pirate
from game_stats import GameStats
from scoreboard import Scoreboard

class PirateInvasion:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Pirate Invasion")

        #Create an instance to store game statistics
        #and create a scoreboard         
        self.cannon = Cannon(self)
        self.stats= GameStats(self)
        self.sb = Scoreboard(self)       
        self.cannonballs = pygame.sprite.Group()
        self.pirates = pygame.sprite.Group()

        self._create_fleet()

        #Make the Play button 
        self.play_button = Button(self, "Start Fight!")

        #Set the background color
        self.bg_color = (62,164,236)
        #bg = pygame.image.load('C:/Users/Khyr/Desktop/CIT228/Sideways_Shooter/images/background.png')

        #Set background song 
        mixer.music.load('C:/Users/Khyr/Desktop/CIT228/Sideways_Shooter/music/music.wav') 
        mixer.music.play(-1) 

    def run_game(self):
        """Start the main loop for game"""
        while True:          
            self._check_events()

            if self.stats.game_active:
                self.cannon.update()
                self._update_cannonballs()
                self._update_pirates()           
            self._update_screen()         
          
    def _check_events(self):
        """Respond to keypresses & mouse events"""         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == ord('s'):
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP or event.type == ord('w'):
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
               
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_UP or event.key == ord('w'):
            self.cannon.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == ord('s'):
            self.cannon.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_cannonball()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP  or event.key == ord('w'):
            self.cannon.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == ord('s'):
            self.cannon.moving_down = False 

    def _check_play_button(self,mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game settings 
            self.settings.intitalize_dynamic_settings() 

            #Reset the game statistics  
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_cannons()

            #Get rid of any remaining pirates and cannonballs
            self.pirates.empty()
            self.cannonballs.empty()

            #Create a new fleet and center the cannon
            self._create_fleet()
            self.cannon.center_cannon()

            #Hide the mouse cursor 
            pygame.mouse.set_visible(False)

    def _fire_cannonball(self):
        """Create a new cannonball and add to the cannonball group"""
        if len(self.cannonballs) < self.settings.cannonballs_allowed:
            new_cannonball = Cannonball(self)
            self.cannonballs.add(new_cannonball)  

    def _update_cannonballs(self):
        """Update the position of cannonballs and get rid of old cannonballs"""
        #Update cannonball positions
        self.cannonballs.update()

        #Get rid of cannonballs off screen
        for cannonball in self.cannonballs.copy():
            if cannonball.rect.bottom <=0:
                self.cannonballs.remove(cannonball)
        self._check_cannonball_pirate_collisions()           

    def _check_cannonball_pirate_collisions(self):
        """Respond to cannonball-pirate collisions"""
        #Remove any cannonballs and pirates that have collided 
        collisions = pygame.sprite.groupcollide(
            self.cannonballs, self.pirates, True, True)

        if collisions:
            for pirates in collisions.values():
                self.stats.score += self.settings.pirate_points * len(pirates)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.pirates:
            #Destroy existing cannonballs and create new fleet
            self.cannonballs.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_pirates(self):
        """Check if the fleet is at an edge, then update the positions of all the pirates in fleet"""
        self._check_fleet_edges()
        self.pirates.update()

        #Look for pirate-cannon collisions 
        if pygame.sprite.spritecollideany(self.cannon, self.pirates):
            self._cannon_hit()

        #Look for pirates hitting the bottom of the screen
        self._check_pirates_bottom()

    def _cannon_hit(self):
        """Respond to cannon being hit by a pirate"""
        if self.stats.cannons_left > 0:
            #Decrement cannons_left, and update scoreboard
            self.stats.cannons_left -= 1
            self.sb.prep_cannons()

            #Get rid of any remaining pirates and cannonballs
            self.pirates.empty()
            self.cannonballs.empty()

            #Create a new fleet and center the cannon
            self._create_fleet()
            self.cannon.center_cannon()

            #Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True) 

    def _check_pirates_bottom(self):
        """Check if any pirates have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for pirate in self.pirates.sprites():
            if pirate.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if teh cannon got hit 
                self._cannon_hit()
                break   
    
    def _update_screen(self):
        """Updates images on the screen, flip to the new screen"""        
        self.screen.fill(self.bg_color)  
        self.cannon.blitme()
        for cannonball in self.cannonballs.sprites():
            cannonball.draw_cannonball()  
        self.pirates.draw(self.screen)

        #Draw the score information
        self.sb.show_score()

        #Draw the play button if the game is inactive 
        
        if not self.stats.game_active:
            self.play_button.draw_button()    
            
        #Make the most recent drawn screen visible 
        pygame.display.flip()

    def _create_fleet(self):
        """Make a fleet of pirates"""
        #Create a pirate ship and find the number of pirates in a row
        #Spacing between each pirate is equal to one pirate width 
        pirate = Pirate(self)
        pirate_width, pirate_height = pirate.rect.size
        available_space_x = self.settings.screen_width - (2 * pirate_width)
        number_pirates_x = available_space_x // (2 * pirate_width)

        #Determine the number of rows of pirates that fit on screen
        cannon_height = self.cannon.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * pirate_height) - cannon_height)
        number_rows = available_space_y // (2 * pirate_height)

        #Create a full fleet of pirates 
        for row_number in range(number_rows):
            for pirate_number in range(number_pirates_x):
                self._create_alien(pirate_number, row_number)

    def _create_alien(self, pirate_number, row_number):
        #Create pirate and place in row
        pirate = Pirate(self)
        pirate_width, pirate_height = pirate.rect.size
        pirate.x = pirate_width + 2 * pirate_width * pirate_number
        pirate.rect.x = pirate.x
        pirate.rect.y = pirate.rect.height + 2 * pirate.rect.height * row_number
        self.pirates.add(pirate)

    def _check_fleet_edges(self):
        """Respond if any pirates have reached an edge"""
        for pirate in self.pirates.sprites():
            if pirate.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet direction"""
        for pirate in self.pirates.sprites():
            pirate.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    #Make a game instance and run the game
    ai = PirateInvasion()
    ai.run_game()
