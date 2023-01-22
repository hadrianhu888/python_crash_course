import pygame
import sys
from settings import Settings
from character import Character


class AlienInvasion:
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()
        self.character = character(self)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            """ for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() """
            self.check_events()
            self.character.update()
            self.update_screen()
            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.bg_color)
            """ self.screen.fill(self.settings.bg_color)
            self.character.blitme() """

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def check_events(self):
        """Responds to the key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the character to the right.
                    # self.character.rect.x += 1
                    self.character.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.character.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.character.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.character.moving_left = False

    def update_screen(self):
        """Updates the images on the screen and flips to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
