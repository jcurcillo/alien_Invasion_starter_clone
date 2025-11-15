"""
Program Name: button.py
Author: Jack Curcillo
Purpose: Create and handle buttons.
Date: 11/14/2025
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion



class Button:
    """
    Play button.
    """
    def __init__(self, game: 'AlienInvasion', msg):
        """
        Initialize button: link game, settings, create rect, prep message.
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Render message to image and center in rect.
        """
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """
        Draw button rect and message to screen.
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """
        Check if mouse clicked button.

        Args:
            mouse_pos (tuple): x, y coordinates of click.

        Returns:
            bool: True if clicked, else False.
        """
        return self.rect.collidepoint(mouse_pos)