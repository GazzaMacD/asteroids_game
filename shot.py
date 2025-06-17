import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        forward = self.velocity * dt
        self.position += forward

    def collision(self, object):
        distance = self.position.distance_to(object.position)
        two_radiuses = self.radius + object.radius
        if not distance > two_radiuses:
            object.kill()
            self.kill()
