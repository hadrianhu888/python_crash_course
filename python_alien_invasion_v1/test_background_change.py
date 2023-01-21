import sys
import pygame
import os
import new_settings
from new_settings import New_Settings
from character import Character as ch
"""This class is used to create the background image for the game."""


class test_background_change:
    """Creates the self init function to change the background color of the screen in pygame"""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Blue Background Color Test")
        self.New_Settings = New_Settings()
        self.Character = ch(self)
        """self.screen_width = 1200
        self.screen_height = 800
        red = 100
        green = 250
        blue = 255
        self.bg_color = (red, green, blue)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.screen.fill(self.bg_color) """

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.Character.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    tbc = test_background_change()
    tbc.run_game()
