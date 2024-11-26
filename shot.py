import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        if self.off_screen():
            self.kill()

    def off_screen(self):
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH:
            return True
        if self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            return True
        return False
    
    def collision_check(self, other):
        distance = (self.position - other.position).length()
        return distance < (self.radius + other.radius)


    
