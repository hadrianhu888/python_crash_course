import pygame
import sys
from settings import Settings
from ship import Ship
"""
    Game class generation and initialization.
    This class is responsible for the game's main loop and
    other game functions.
"""


class AlienInvasion:
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self.check_events()
            self.ship.update()
            self.update_screen()
            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """_summary_
        Generates events from key presses and mouse events.
        Args:
            event (_type_): _description_
        """
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            # self.ship.rect.x += 1
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """_summary_
        Generates events from key presses and mouse events.
        Args:
            event (_type_): _description_
        """
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            # self.ship.rect.x -= 1
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    """
    Allows the game to be played by running the file.
    """
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
