class GameStats:
    """Відслідковування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізує статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Гра запускається в неактивному стані
        self.game_active = False

    def reset_stats(self):
        """Іеіціалізує статистику, що змінюється під час гри"""
        self.ships_left = self.settings.ship_limit
