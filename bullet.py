import pygame

SCREEN_HEIGHT = 800

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load bullet image
        self.image = pygame.image.load('assets/player_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 15))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -8
        try:
            self.sound = pygame.mixer.Sound('assets/shoot.wav')
        except (pygame.error, FileNotFoundError):
            self.sound = None  # Sound file not found, set to None

        # Play sound if it exists
        if self.sound:
            self.sound.play()

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        # Load enemy bullet image
        self.image = pygame.image.load('assets/enemy_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 15))
        self.rect = self.image.get_rect(center=(x, y))
        # Calculate direction towards the target position
        direction = pygame.math.Vector2(target_x - x, target_y - y).normalize()
        self.speed = 4  # Set the desired bullet speed
        self.velocity = direction * self.speed

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        # Remove bullet if it goes off-screen
        if (self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0 or
            self.rect.right < 0 or self.rect.left > SCREEN_WIDTH):
            self.kill()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
