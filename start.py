import sys

import pygame as pg


class AlienInvasion:
    """Клас для управління ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pg.init()

        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Alien Invasion")

        # Призначення коліру фону
        self.bg_color = (230, 230, 230)  # RGB

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіатури та миші
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # За кожної ітерації циклу оновлюється екран
            self.screen.fill(self.bg_color)

            # Відображення останнього прорисованого екрану
            pg.display.flip()


if __name__ == "__main__":
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
