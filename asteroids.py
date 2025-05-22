from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.x = self.position[0]
        self.y = self.position[1]
       
    def draw (self, screen):
        x = self.position[0]
        y = self.position[1]
        pygame.draw.circle(screen, (255, 0, 0), (x, y), self.radius, width=2)        
        
    def update (self, dt):
        self.position += self.velocity * dt

    def split (self):
        if self.radius <= ASTEROID_MIN_RADIUS:   #if the asteroid is small, kills it
            pygame.sprite.Sprite.kill(self)
            return
        else:                   #if the asteroid is large or medium, create 2 smaller ones
            x = self.position[0]
            y = self.position[1]
            angle = random.uniform(20, 50)
            asteroidvector1 = self.velocity.rotate(angle)
            asteroidvector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(x, y, new_radius)
            new_asteroid_2 = Asteroid(x, y, new_radius)
            new_asteroid_1.velocity = asteroidvector1 * 1.2
            new_asteroid_2.velocity = asteroidvector2 * 1.2
            pygame.sprite.Sprite.kill(self)
        
