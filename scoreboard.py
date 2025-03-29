import pygame as pg
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """Клас для виведення ігрової інформації"""

    def __init__(self, ai_game):
        """Ініціалізує атрибути підрахунку очок"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування для виведення рахунку
        self.text_color = (128, 128, 128)
        self.font = pg.font.SysFont(None, 48)

        # Підготовка зображень
        self.prepare_score()
        self.prepare_high_score()
        self.prepare_level()
        self.prepare_ships()

    def check_high_score(self):
        """Перевіряє, чи з'явився новий рекорд"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prepare_high_score()

    def prepare_high_score(self):
        """Перетворює рекорд на графічне зображення"""
        rounded_score = round(self.stats.high_score, -1)
        score_str = f"{rounded_score:,}"
        self.high_score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Виведення рекорду по центру верхньої частини екрану
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prepare_level(self):
        """Перетворює рівень на графічне зображення"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # Виведення рівня під поточним рахунком
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prepare_score(self):
        """Перетворює поточний рахунок на графічне зображення"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Ввиедення рахунку в правій частині екрану
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prepare_ships(self):
        """Повідомляє кількість кораблів, що залишилися"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Виводе рахунок на екран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
