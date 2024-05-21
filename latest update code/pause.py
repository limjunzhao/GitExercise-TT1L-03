import pygame
from settings import *

FPS = 60
 
# Create the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pause_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pause_surface.fill((128, 128, 128, 150))  
surface = pygame.Surface((HEIGHT, WIDTH), pygame.SRCALPHA)
