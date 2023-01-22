import sys
import pygame 
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
            """Initialize the game, and create game resources."""
            pygame.init()
            self.settings = Settings()
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            pygame.display.set_caption("Alien Invasion")
            self.ship = Ship(self)
            self.bullets = pygame.sprite.Group()
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            # Set the background color.
            self.bg_color  = self.settings.bg_color
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.check_events()    
            self.ship.update()
            self.bullets.update()
            self.update_screen()
            
    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the 
        # loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
    
    def check_keydown_events(self,event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
            
    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            
    def check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        
                
if __name__ == '__main__': 
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()