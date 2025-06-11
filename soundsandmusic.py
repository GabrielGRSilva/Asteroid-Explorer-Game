import pygame

class Music:

    def play_music(self):
        pygame.mixer.music.load("sounds/Mesmerizing Galaxy Loop.mp3")
        pygame.mixer.music.play(-1)  # Loop indefinitely
        pygame.mixer.music.set_volume(0.1)  # Set volume to 10%

class AsteroidSound:

    def play_sound(self):
        self.explosion_sound = pygame.mixer.Sound("sounds/asteroidkill.wav")
        self.explosion_sound.play()
        self.explosion_sound.set_volume(0.1)  # Set volume to 10%

class ShipSound:
    
    def play_sound(self):
        self.ship_sound = pygame.mixer.Sound("sounds/shipcrash.wav")
        self.ship_sound.play()
        self.ship_sound.set_volume(0.1)  # Set volume to 10%


