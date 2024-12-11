from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate smaller asteroids
        angle = random.randint(20, 50)

        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        sub1 = Asteroid(self.position[0], self.position[1], new_radius)
        sub1.velocity = v1

        sub2 = Asteroid(self.position[0], self.position[1], new_radius)
        sub2.velocity = v2

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt