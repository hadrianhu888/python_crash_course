import pygame

# TODO: Fix up the ship movement - right now, it is not moving at all.


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.moving_right = True
            self.rect.x = self.settings.ship_speed + self.settings.ship_acc
        elif self.moving_left and self.rect.left > 0:
            self.moving_left = True
            self.rect.x = self.settings.ship_speed - self.settings.ship_dec
        elif self.moving_up and self.rect.top < 0:
            self.moving_up = True
            self.rect.y = self.settings.ship_speed - self.settings.ship_dec
        elif self.moving_down and self.rect.bottom > self.screen_rect.bottom:
            self.moving_down = True
            self.rect.y = self.settings.ship_speed + self.settings.ship_acc

        # Update rect object from self.x.
        self.rect.x = self.rect.x + self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
