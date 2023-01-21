import sys
import pygame 
from settings import *
from ship import *

class AlienInvasion:
    """Over all class to manage game assets and behavior"""    
    def __init__(self):
        """Initialize game assets"""
        pygame.init()            
        self.settings = Settings()        
        pygame.display.set_caption("Alien Invasion")        
        self.ship = Ship(self)             
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))        
    def run_game(self):        
        """Start the main loop for the game"""        
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()                    
            # make the most recently drawn screen visible 
            self.screen.fill(self.settings.bg_color)    
            self.ship.blitme()                
            pygame.display.flip()          
            
if __name__ == '__main__':
    ai_game = AlienInvasion()
    ai_game.run_game()
    
    