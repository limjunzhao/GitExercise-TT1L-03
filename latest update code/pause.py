import pygame
from settings import *
from button import *

pygame.init()

FPS = 60
 
# Create the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pause_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pause_surface.fill((128, 128, 128, 10))  
surface = pygame.Surface((HEIGHT, WIDTH), pygame.SRCALPHA)

volup_static = pygame.image.load('images/button/vol_up.png')
volup_hover = pygame.image.load('images/button/vol_up-hover.png')
voldown_static = pygame.image.load('images/button/vol_down-static.png')
voldown_hover = pygame.image.load('images/button/vol_down-hover.png')
volmute_static = pygame.image.load('images/button/vol_mute-static.png')
volmute_hover = pygame.image.load('images/button/vol_mute-hover.png')

vol_up_button = Button(425, 200, volup_static, volup_hover, (200, 100))
vol_down_button = Button(625, 200, voldown_static, voldown_hover, (200, 100))
vol_mute_button = Button(425, 300, volmute_static, volmute_hover, (408, 100))
