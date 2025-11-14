from pathlib import Path

class Settings:

    def __init__(self):
        #base settings, background
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'replacement_bg.webp'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        #ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'replacement_ship.png'
        self.ship_w = 60
        self.ship_h = 60
        

        #bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'replacement_laser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'replacement_laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'replacement_impact.mp3'
        

        #alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'replacement_enemy.png'
        self.alien_w = 60
        self.alien_h = 60
        self.fleet_speed = 2
        
        

        #button settings
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        #font settings
        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'


    #dynamic
    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.fleet_direction = 1
        self.fleet_drop_speed = self.alien_h / 2

        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale

