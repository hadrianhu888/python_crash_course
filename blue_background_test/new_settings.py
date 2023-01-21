import pygame
import sys
import os


class New_Settings:
    """A class to store all settings for The blue background color test."""

    def __init__(self):
        """Initialize the game's settings."""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        red = 100
        green = 250
        blue = 255
        self.bg_color = (red, green, blue)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.screen.fill(self.bg_color)
