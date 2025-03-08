import pygame as pg


class Ship:
    """Клас для управління кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює його початкову позицію"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантаження зображення корабля і отримання поверхні
        self.image = pg.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Кожен новий корабель з'являється в нижній частині екрану
        self.rect.midbottom = self.screen_rect.midbottom

        # Зберігання дробової координати центра корабля
        self.x = float(self.rect.x)

        # Флаг переміщення
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисує корабель в поточнй позиції"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Розміщує корабель внизу екрана"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Оновлює позицію корабля з урахування флагу"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Оновлення атрибуту rect значенням self.x
        self.rect.x = self.x
