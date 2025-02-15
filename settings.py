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
