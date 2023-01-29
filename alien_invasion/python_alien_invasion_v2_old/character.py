import pygame as pg
from settings import Settings


class Character:
    """A class to manage the character."""

    def __init__(self, ai_game):
        """Initialize the character and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the character image and get its rect.
        self.image = pg.image.load('images/hero.bmp')
        self.rect = self.image.get_rect()

        # Store a decimal value for the character's horizontal position.
        self.x = float(self.rect.x)

        # movement flag

        self.moving_right = False
        self.moving_left = False

        # Start each new character at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        """Update the character's position on the movement flag"""

        if self.moving_right:
            # self.rect.x += 1
            self.x += self.settings.character_speed
        if self.moving_left:
            # self.rect.x -= 1
            self.x -= self.settings.character_speed

        # Limit the character's range on the screen.

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.character_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.character_speed

        # Update rect object from self.x.

        self.rect.x = self.x

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
