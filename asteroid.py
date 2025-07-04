import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)
        # Make sure position is a Vector2 if it isn't already
        if not isinstance(self.position, pygame.Vector2):
            self.position = pygame.Vector2(self.position)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Calculate new angle for child asteroids
            random_angle = random.uniform(20.0, 50.0)

            # Apply angle to current velocity, use negative angle for child 2
            split_1 = self.velocity.rotate(random_angle)
            split_2 = self.velocity.rotate(random_angle * -1)

            # Calculate new radious
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Spawn children and apply calculated velocity
            child_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_1.velocity = split_1 * 1.2
            child_2.velocity = split_2 * 1.2
