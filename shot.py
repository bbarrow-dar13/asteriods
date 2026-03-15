import pygame
from constants import *
from circleshape import *

# Shot class inherits from CircleShape(pygame.sprite.Sprite):

class Shot (CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
