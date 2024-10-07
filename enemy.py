import pygame
import random
from bullet import EnemyBullet

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, path=None, formation_pos=None):
        super().__init__()
        # Load enemy image
        self.image = pygame.image.load('assets/enemy_ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

        # New attributes for path movement
        self.path = path  # The path the enemy will follow
        self.path_index = 0  # Current index in the path
        self.in_formation = False  # Whether the enemy has reached its formation position
        self.formation_pos = formation_pos  # The position in formation
        self.attacking = False  # Whether the enemy is currently attacking

    def update(self):
        if not self.in_formation:
            # Move along the entrance path
            if self.path and self.path_index < len(self.path):
                self.rect.center = self.path[self.path_index]
                self.path_index += 1
            else:
                # Enemy has reached formation
                self.in_formation = True
                self.rect.center = self.formation_pos
        elif self.attacking:
            # Move along the attack path
            if self.path and self.path_index < len(self.path):
                self.rect.center = self.path[self.path_index]
                self.path_index += 1
            else:
                # Return to formation after attack
                self.attacking = False
                self.in_formation = True
                self.rect.center = self.formation_pos
        elif not self.in_formation:
            # After attack, move back to formation from top
            if self.path_index < len(self.path):
                self.rect.center = self.path[self.path_index]
                self.path_index += 1
            else:
                self.in_formation = True
                self.rect.center = self.formation_pos

    def shoot(self, target_x, target_y):
        if self.attacking:
            # Randomly decide to shoot
            if random.randint(1, 100) == 1:
                bullet = EnemyBullet(self.rect.centerx, self.rect.bottom, target_x, target_y)
                return bullet
        return None

    def start_attack(self, attack_path):
        self.attacking = True
        self.in_formation = False
        self.path = attack_path
        self.path_index = 0
