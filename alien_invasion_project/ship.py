import pygame


class Ship:
    """A class for the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.ai_game = ai_game
        self.screen = ai_game.screen()
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen_rect

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw te ship at its current position"""
        self.screen.blit(self.image, self.rect)
