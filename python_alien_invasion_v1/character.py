import pygame as pg
import sys


class Character:
    """Creates a character for the blue background game"""

    def __init__(self, tbc_game):
        """Initialize the ship and set its starting position."""
        self.screen = tbc_game.screen
        self.screen_rect = tbc_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image = pg.image.load('images/hero.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
