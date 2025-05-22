import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.shot_speed = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        ax = self.position[0]
        ay = self.position[1] 
        if self.shot_cooldown <= 0:
            self.shot_cooldown = 0.3
            new_shot = Shot(ax, ay, SHOT_RADIUS, self.shot_speed)

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.shot_radius = SHOT_RADIUS
        self.speed = velocity
        self.position = self.position

    def draw (self, screen):
        x = self.position[0]
        y = self.position[1]
        xa = int(x)
        ya = int(y)
        pygame.draw.circle(screen, (0, 255, 0), (xa,ya), self.shot_radius, width=2)        
        
    def update (self, dt):
        self.position += self.speed * dt
