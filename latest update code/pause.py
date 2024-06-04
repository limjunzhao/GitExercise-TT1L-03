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
quit_static = pygame.image.load('images/button/quit_static.png')
quit_hover = pygame.image.load('images/button/quit_hover.png')
back_static = pygame.image.load('images/button/back_static.png')
back_hover = pygame.image.load('images/button/back_hover.png')

vol_up_button = Button(200, 175, volup_static, volup_hover, (250, 85))
vol_down_button = Button(200, 255, voldown_static, voldown_hover, (250, 85))
vol_mute_button = Button(200, 335, volmute_static, volmute_hover, (250, 85))
back_button = Button(200, 415, back_static, back_hover, (250, 85))
quit_button = Button(200, 495, quit_static, quit_hover, (250, 85))

font = pygame.font.Font(None, 36)

messages = [
    {"text": "Detective!,", "color": (0, 0, 0), "position": (500, 200)},
    {"text": "you are required to interact with everyone", "color": (0, 0, 0), "position": (500, 230)},
    {"text": "to find clues and most importantly!", "color": (0, 0, 0), "position": (500, 260)},
    {"text": "FIND WHO THE KILLER IS!!!", "color": (0, 0, 0), "position": (500, 290)},
    {"text": "interact with all the npc's and find clue", "color": (0, 0, 0), "position": (500, 320)},
    {"text": "to unlock the ability to report you suspicion to the officer", "color": (0, 0, 0), "position": (500, 350)},
    {"text": "All the best!", "color": (0, 0, 0), "position": (500, 380)},
    {"text": "From HQ,", "color": (0, 0, 0), "position": (500, 410)},
    {"text": "salute*", "color": (0, 0, 0), "position": (500, 440)},
]