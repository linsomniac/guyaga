import pygame
import math

def generate_entrance_path(start_pos, end_pos, pattern_type):
    path = []
    # Generate different patterns based on pattern_type
    if pattern_type == 'sinusoidal':
        # Example sinusoidal path
        for t in range(0, 360, 5):
            x = start_pos[0] + (end_pos[0] - start_pos[0]) * t / 360
            y = start_pos[1] + 100 * math.sin(math.radians(t))
            path.append((x, y))
    elif pattern_type == 's_curve':
        # Example S-curve path
        for t in range(0, 360, 5):
            x = start_pos[0] + 100 * math.sin(math.radians(t))
            y = start_pos[1] + (end_pos[1] - start_pos[1]) * t / 360
            path.append((x, y))
    # Add more patterns as needed
    return path

def generate_attack_path(start_pos):
    path = []
    # Define an attack path where the enemy dives towards the player's position
    # For simplicity, we'll make the enemy move straight down and back up
    screen_height = 800
    for y in range(int(start_pos[1]), screen_height + 100, 5):
        path.append((start_pos[0], y))
    for y in range(screen_height + 100, int(start_pos[1]), -5):
        path.append((start_pos[0], y))
    return path
