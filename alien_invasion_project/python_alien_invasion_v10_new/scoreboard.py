import pygame.font
from pygame.sprite import Group
from ship import Ship
import csv
from csv import writer
from csv import reader
"""
_summary_ Displays the score on the screen

"""


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image.
        self.prep_score()
        self.prep_level()
        self.prep_ships()
        self.prep_high_score()
        self.record_score()
        self.show_all_scores()

    def record_score(self):
        """ Record the score in a csv file"""
        score_file = open('score.csv', 'a+', newline='')
        # Writing the score to the csv file
        csv_writer = writer(score_file)
        csv_writer.writerow([self.stats.score])
        # Append new scores to the csv file
        csv_writer.writerow([self.stats.score])
        # Close the file
        csv_writer.close()

    def show_all_scores(self, ai_game):
        """ Show all the scores in the csv file"""
        score_file = open('score.csv', 'r')
        csv_reader = reader(score_file)
        for row in csv_reader:
            print(row)
        score_file.close()
        # Show all the scores on the game screen
        self.screen.blit(self.all_scores, self.all_scores_rect)

    def prep_ships(self):
        """Prepare the ships to be displayed on the screen"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        # Also show the high score in the middle top of the screen
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # Also show the level below the score
        self.screen.blit(self.level_image, self.level_rect)
        # Also show the ships left
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect_centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """See if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
