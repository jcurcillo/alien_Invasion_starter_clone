"""
Program Name: alien_fleet.py
Author: Jack Curcillo
Purpose: Manage fleet of aliens.
Date: 11/14/2025
"""

import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class AlienFleet:
    """
    Manages fleet of alien sprites.
    """    
    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the alien fleet.

        Args:
            game ('AlienInvasion'): Reference to the main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """
        Creates grid of aliens.
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_h = self.settings.screen_h
        screen_w = self.settings.screen_w
        
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """
        Builds the shape of fleet.

        Args:
            alien_w (int): Width of alien.
            alien_h (int): Height of alien.
            fleet_w (int): Number of aliens horizontally.
            fleet_h (int): Number of aliens vertically.
            x_offset (int): Horizontal offset.
            y_offset (int): Vertical offset.
        """
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if row % 2 == 1:
                    if col % 2 == 1:
                        continue
                else:
                    if col % 2 == 0:
                        continue
                        
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """
        Calculate offsets

        Args:
            alien_w (int): Width of alien.
            alien_h (int): Height of alien.
            fleet_w (int): Number of aliens horizontally.
            fleet_h (int): Number of aliens vertically.
            screen_w (int): Width of screen.

        Returns:
            tuple: (x_offset, y_offset)
        """
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset,y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):     
        """
        Determine height and width of fleet

        Args:
            alien_w (int): Width of alien.
            screen_w (int): Width of screen.
            alien_h (int): Height of alien.
            screen_h (int): Height of screen.

        Returns:
            tuple: (fleet_w, fleet_h) number of aliens horizontally and vertically
        """
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h / 2) // alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2


        return int(fleet_w), int(fleet_h)
    

    
    def _create_alien(self, current_x: int, current_y: int):
        """
        Create  Alien and add to fleet.

        Args:
            current_x (int): X coordinate of alien.
            current_y (int): Y coordinate of alien.
        """
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """
        Drop and reverse fleet when hitting edge.
        """
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break
        
    def _drop_alien_fleet(self):
        """
        Move fleet down by fleet_drop_speed.
        """
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """
        Update fleet position, checking edges and moving
        fleet in current direction.
        """
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """
        Draw all aliens in fleet to screen.
        """
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """
        Check for projectile hits.

        Args:
            other_group (pygame.sprite.Group): check collisions against.

        Returns:
            dict: Dictionary of collisions returned by pygame.sprite.groupcollide
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        """
        Check if any alien has reached bottom of screen.

        Returns:
            bool: True if alien reached bottom, else False.
        """
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self. settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        """
        Check if all aliens were destroyed.

        Returns:
            bool: True if fleet is empty, else False.
        """
        return not self.fleet