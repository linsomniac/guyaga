import pygame
import sys
import random
from player import Player
from enemy import Enemy
from bullet import Bullet, EnemyBullet
# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Galaga Clone')

# Create a clock to control frame rate
clock = pygame.time.Clock()
