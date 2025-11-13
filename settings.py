from pathlib import Path

class Settings:

    def __init__(self):
        #base settings, background
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'replacement_bg.webp'

        #ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'replacement_ship.png'
        self.ship_w = 60
        self.ship_h = 60
        self.ship_speed = 5

        #bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'replacement_laser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'replacement_laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        #alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 50
        self.alien_h = 50
        self.fleet_speed = 5
        