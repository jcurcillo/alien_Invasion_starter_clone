"""
Program Name: game_stats.py
Author: Jack Curcillo
Purpose: Track scores, lives, and levels.
Date: 11/14/2025
"""

import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats():
    """
    Track game statistics: score, lives, level, high scores.
    """
    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize stats: link game, settings, load saved scores, reset stats.
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """
        Load hi-score from JSON file or initialize to 0.
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # save the file


    def save_scores(self):
        """
        Save hi-score to JSON file.
        """
        scores = {
            'hi_score': self.hi_score
        }            
        contents = json.dumps(scores, indent = 4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """
        Reset lives, score, level.
        """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """
        Update score, max score, and hi-score based on collisions.
        """
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()


    def _update_max_score(self):
        """
        Update max score.
        """
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'Max: {self.max_score}')

    def _update_hi_score(self):
        """
        Update hi-score.
        """ 
        if self.score > self.hi_score:
            self.hi_score = self.score
        # print(f'Hi: {self.hi_score}')

    def _update_score(self, collisions):
        """
        Add points for destroyed aliens.
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f'Basic: {self.score}')

    def update_level(self):
        """
        Increment level
        """
        self.level += 1
        