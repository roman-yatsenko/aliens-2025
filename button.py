import pygame as pg


class Button:

    def __init__(self, ai_game, msg):
        """Ініціалізує атрибути кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Призначення розмірів та властивостей кнопки
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        # Побудова об'єкта rect кнопки та вирівнювання по центру екрана
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Текст кнопки створюється тільки один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Перетворює msg в прямокутник і вирівнює текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Відображає пусту кнопку та виводе текст"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
