import pygame
from bullet import Bullet

SCREEN_WIDTH = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load player image
        self.image = pygame.image.load('assets/player_ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 20))
        self.speed = 4
        self.lives = 3

    def __init__(self):
        super().__init__()
        # Load player image
        self.image = pygame.image.load('assets/player_ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 2, 580))
        self.speed = 5
        self.lives = 3
        self.velocity = pygame.math.Vector2(0, 0)  # For smooth movement

    def process_input(self, keys_pressed):
        self.velocity.x = 0  # Reset horizontal velocity
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.velocity.x = -self.speed
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.velocity.x = self.speed

    def update(self):
        # Move the player based on velocity
        self.rect.x += self.velocity.x

        # Keep the player within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        return bullet
