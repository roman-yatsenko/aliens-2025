import sys

import pygame as pg

from settings import Settings


class AlienInvasion:
    """Клас для управління ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pg.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіатури та миші
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # За кожної ітерації циклу оновлюється екран
            self.screen.fill(self.settings.bg_color)

            # Відображення останнього прорисованого екрану
            pg.display.flip()


if __name__ == "__main__":
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
