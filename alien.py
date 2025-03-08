import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас для прибульця"""

    def __init__(self, ai_game):
        """Ініціалізує прибульця та задає його початкову позицію"""
        super().__init__()
        self.screen = ai_game.screen

        # Завантаження зображення прибульця та визначення rect
        self.image = pg.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Кожен новий прибулець з'являється в лівому верхньому куті екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Збереження точної горизонтальної позиції прибульця
        self.x = float(self.rect.x)
