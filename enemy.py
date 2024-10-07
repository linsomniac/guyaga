import pygame
import random
import math
from bullet import EnemyBullet
from paths import generate_entrance_path, generate_attack_path

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
            # Move along the entrance or return path
            if self.path and self.path_index < len(self.path):
                self.rect.center = self.path[self.path_index]
                self.path_index += 1
            else:
                # Enemy has reached formation
                self.in_formation = True
                self.attacking = False
                self.rect.center = self.formation_pos
        elif self.attacking:
            # Move along the attack path
            if self.path and self.path_index < len(self.path):
                self.rect.center = self.path[self.path_index]
                self.path_index += 1
            else:
                # Prepare to return to formation after attack
                self.attacking = False
                self.in_formation = False
                start_pos = (self.rect.centerx, -100)
                self.path = generate_entrance_path(
                    start_pos, self.formation_pos, 'straight_down')
                self.path_index = 0
        # Enemies stay stationary when in formation

    def shoot(self, target_x, target_y):
        if self.attacking:
            # Check if the enemy is higher than 66% of the screen height
            threshold_y = 0.66 * SCREEN_HEIGHT
            if self.rect.centery <= threshold_y:
                # Calculate the vector from the enemy to the player
                dx = target_x - self.rect.centerx
                dy = target_y - self.rect.centery
                
                # Calculate the angle in degrees between the enemy and the player
                angle_rad = math.atan2(dy, dx)
                angle_deg = math.degrees(angle_rad)
                
                # Normalize angle to range [0, 360)
                if angle_deg < 0:
                    angle_deg += 360
                
                # Check if the angle is within the 90-degree cone beneath the enemy (225 to 315 degrees)
                if 225 <= angle_deg <= 315:
                    # Proceed to shoot with a certain probability
                    if random.randint(1, 100) == 1:
                        bullet = EnemyBullet(self.rect.centerx, self.rect.bottom, target_x, target_y)
                        return bullet
        return None

    def start_attack(self):
        self.attacking = True
        self.in_formation = False
        self.path_index = 0
        self.path = generate_attack_path(self.rect.center, self.formation_pos)
