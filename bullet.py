import pygame

SCREEN_HEIGHT = 600

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load bullet image
        self.image = pygame.image.load('assets/player_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 15))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10
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
    def __init__(self, x, y):
        super().__init__()
        # Load enemy bullet image
        self.image = pygame.image.load('assets/enemy_bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 15))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
