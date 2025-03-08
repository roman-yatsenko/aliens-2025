class Settings:
    """Клас для зберігання всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Пераметри екрану
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Параметри корабля
        self.ship_speed = 1.5

        # Парематри снаряду
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Параметри прибульців
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 якщо флот рухається праворуч, -1 якщо ліворуч
        self.fleet_direction = 1
