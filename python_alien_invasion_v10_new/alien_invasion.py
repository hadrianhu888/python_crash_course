import sys
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep

# TODO: Fix up the ship movement - right now, it is not moving at all.
# FIXED - ship movement is working now.
# ISSUE: ship movement not working. Implementation issue.


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        """ self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height """
        # Make the play button
        self.play_button = Button(self, "Play")

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Set the background color.
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.check_events()
            # self.ship.update() # BUG: updating ship does not move the ship on screen. Not sure why this is the case.
            if self.stats.game_active:
                self.update_screen()
                self.update_bullets()
                # ISSUE: Not sure if this will work or not. # This actually works - all aliens move to the right of the screen.
                self.update_aliens()
            self.update_screen()

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # or use esc key to exit the game as well.
            if event.type == pygame.K_q or event.type == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_play_button(self, mouse_pos):
        """Check mouse down query to see if the play button was pressed."""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self.create_fleet()
            self.ship.center_ship()

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the
        # loop.
        self.screen.fill(self.settings.bg_color)
        # Update the ship's position:
        self.ship.blitme()
        # Draw the bullets:
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Add the alien to the screen:
        self.aliens.draw(self.screen)
        # Draw the play button if the game is inactive:
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Continue to update the screen:
        pygame.display.flip()

    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        """Responding to bullet-alien collisions."""
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self.create_fleet()

    def update_aliens(self):
        """Updates the positions of all aliens in the fleet."""
        # Check if the fleet is at the edge of the screen, and then update the positions of all aliens in the fleet.
        self.check_fleet_edges()
        # Update the alien positions
        self.aliens.update()
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollide(self.ship, self.aliens, False):
            self.ship_hit()
        # look for aliens hitting the bottom of the screen.
        self.check_aliens_bottom()

    def check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            # self.ship.rect.x = self.ship.rect.x
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            # self.ship.rect.x = self.ship.rect.x
        elif event.key == pygame.K_UP:
            self.moving_up = False
            # self.ship.rect.y = self.ship.rect.y
        elif event.key == pygame.K_DOWN:
            self.moving_down = False
            # self.ship.rect.y = self.ship.rect.y

    def check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right:
            self.ship.moving_right = True
            self.ship.rect.x += self.settings.ship_speed  # + self.settings.ship_acc
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left:
            self.ship.moving_left = True
            self.ship.rect.x -= self.settings.ship_speed  # - self.settings.ship_dec
        elif event.key == pygame.K_UP:
            # Move the ship up:
            self.ship.moving_up = True
            self.ship.rect.y -= self.settings.ship_speed  # + self.settings.ship_dec
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
            self.ship.rect.y += self.settings.ship_speed  # - self.settings.ship_dec
        elif event.key == pygame.K_SPACE:
            # Create a new bullet and add it to the bullets group:
            self.fire_bullet()
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def create_fleet(self):
        """Creates the alien fleet"""
        # Make a single alien ship
        aliens = Alien(self)
        # self.aliens.add(aliens)
        # Make a fleet of aliens:
        alien_width, alien_height = aliens.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen:
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens:
        for row_number in range(number_rows):
            # Create the first row of aliens:
            for alien_number in range(number_aliens_x):
                # Create an alien and place it in the row:
                self.create_alien(alien_number, row_number)

        # Create the first row of aliens:
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row:
            self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        # Refactoring the create_fleet() method:
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def check_fleet_edges(self):
        """Responds appropriately if any aliens have reached the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Drop the entire fleet and change the fleet direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self.create_fleet()
            self.ship.center_ship()
            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False

    def check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        # Check if any aliens have reached the bottom of the screen.
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self.ship_hit()
                break


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
