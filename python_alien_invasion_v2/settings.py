class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        red = 100
        blue = 100
        green = 255
        self.bg_color = (red, green, blue)

        # character settings

        """Adjst the character speed"""
        self.character_speed = 1.5
