class GameStats():
    # Track game statistics

    def __init__(self, ai_settings):
        # initialized statistic infomation
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        # initialized the static infomation during game
        self.ships_left = self.ai_settings.ship_limit