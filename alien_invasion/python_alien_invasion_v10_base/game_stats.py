class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        # Start Alien Invasion in an active state.
        # set to false to start in an inactive state before  the game starts
        self.game_active = False
        self.reset_stats()
        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Reset statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        # initialize the score to 0
        self.score = 0
        self.level = 1
