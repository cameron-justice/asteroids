from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOT_COOLDOWN, PLAYER_STARTING_LIVES
from shot import Shot

import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_time_remaining = 0
        self.score = 0
        self.lives = PLAYER_STARTING_LIVES

    def add_score(self, value):
        self.score += value

    def remove_score(self, value):
        self.score = max(0, self.score - value)

    def remove_life(self):
        self.lives -= 1

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Rotation Input
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Movement Input
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Shoot Input
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.shot_cooldown_time_remaining > 0:
            self.shot_cooldown_time_remaining = max(0, self.shot_cooldown_time_remaining - dt)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown_time_remaining == 0:
            shot = Shot(self.position[0], self.position[1])
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown_time_remaining = PLAYER_SHOT_COOLDOWN

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]