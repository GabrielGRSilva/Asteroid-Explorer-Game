from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
       
    def draw (self, screen):
        x = self.position[0]
        y = self.position[1]
        pygame.draw.circle(screen, (255, 0, 0), (x,y), self.radius, width=2)        
        
    def update (self, dt):
        self.position += self.velocity * dt