import pygame as pg


class Scoreboard:
    """Клас для виведення ігрової інформації"""

    def __init__(self, ai_game):
        """Ініціалізує атрибути підрахунку очок"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування для виведення рахунку
        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        # Підготовка початкового зображення
        self._prepare_score()

    def _prepare_score(self):
        """Перетворює поточний рахунок на графічне зображення"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Ввиедення рахунку в правій частині екрану
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Виводе рахунок на екран"""
        self.screen.blit(self.score_image, self.score_rect)
