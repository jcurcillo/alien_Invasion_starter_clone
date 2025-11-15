"""
Program Name: arsenal.py
Author: Jack Curcillo
Purpose: Manage bullets fired by ship.
Date: 11/14/2025
"""

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """
    Manage ammunition fired by ship.
    """
    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize arsenal: link game, settings, create bullet group.
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """
        Update position of bullets, remove off-screen bullets.
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """
        Remove bullets off the top of screen.
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
        

    def draw(self):
        """
        Draw bullets to screen.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self):
        """
        Fire a bullet.

        Returns:
            bool: True if bullet fired, else False.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
        
        