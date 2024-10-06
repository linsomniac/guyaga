import pygame
import random
from bullet import EnemyBullet

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        # Load enemy image
        self.image = pygame.image.load('assets/enemy_ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

        # Change direction at screen edges and move down
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed *= -1
            self.rect.y += 16  # Move down when changing direction

    def shoot(self, target_x, target_y):
        # Randomly decide to shoot
        if random.randint(1, 200) == 1:
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom, target_x, target_y)
            return bullet
        return None
