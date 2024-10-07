import pygame
import math
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

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
    elif pattern_type == 'straight_down':
        # Enters from the top straight to formation position
        for y in range(int(start_pos[1]), int(end_pos[1]), 5):
            path.append((start_pos[0], y))
    # Add more patterns as needed
    return path

def generate_attack_path(start_pos, formation_pos, pattern_type='dive'):
    path = []
    if pattern_type == 'dive':
        # Define the parameters for horizontal movement
        amplitude = random.randint(50, 150)  # Horizontal amplitude
        frequency = random.uniform(0.005, 0.02)  # Frequency of the sine wave
        length = 300  # Length of the dive path
        
        for i in range(length):
            x = start_pos[0] + amplitude * math.sin(frequency * i)
            y = start_pos[1] + i
            path.append((x, y))
        # Continue moving down off-screen
        for y in range(int(path[-1][1]), SCREEN_HEIGHT + 100, 5):
            path.append((path[-1][0], y))
        # Return path from top to formation position
        return_path = generate_entrance_path(
            (formation_pos[0], -100), formation_pos, 'straight_down')
        path.extend(return_path)
    # Add more patterns as needed
    return path
