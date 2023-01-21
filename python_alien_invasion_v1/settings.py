class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        red = 230
        blue = 230
        green = 230
        self.bg_color = (red, green, blue)

        # Ship settings

        """Adjst the ship speed"""
        self.ship_speed = 1.5
