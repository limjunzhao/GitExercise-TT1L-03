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

pause_font = pygame.font.Font(None, 26)

pause_info = [
    {"text": "Instructions:", "color": (0, 0, 0), "position": (500, 195)},
    {"text": "Graduate from dino school to learn their language ", "color": (0, 0, 0), "position": (500, 225)},
    {"text": "Interact with all the villagers", "color": (0, 0, 0), "position": (500, 255)},
    {"text": "Complete minigames to find clues", "color": (0, 0, 0), "position": (500, 285)},
    {"text": "When you are ready report your case to the officer ", "color": (0, 0, 0), "position": (500, 315)},
    {"text": "Storyline recap:", "color": (0, 0, 0), "position": (500, 365)},
    {"text": "You're a detective teleporting to different time zone to solve mystery cases.", "color": (0, 0, 0), "position": (500, 395)},
    {"text": "You're currently in a small town called 'Arcadia' in the dino-verse trying", "color": (0, 0, 0), "position": (500, 425)},
    {"text": "to solve a grisly murderer case which took place not long ago.", "color": (0, 0, 0), "position": (500, 455)},
    {"text": "It's 7am in the morning when you discovered the victim's dead body", "color": (0, 0, 0), "position": (500, 485)},
    {"text": "outside a house.  The early morning tranquility is shattered by the grim ", "color": (0, 0, 0), "position": (500, 515)},
    {"text": "discovery...", "color": (0, 0, 0), "position": (500, 545)},
]



def draw_rounded_rect(surface, color, rect, corner_radius):
    x, y, w, h = rect
    
    # Ensure the corner radius is not greater than half the width or height
    corner_radius = min(corner_radius, w // 2, h // 2)
    
    # Create a mask to help with the anti-aliasing
    mask = pygame.Surface((w, h), pygame.SRCALPHA)
    
    # Draw the filled rectangle
    pygame.draw.rect(mask, color, (corner_radius, 0, w - 2 * corner_radius, h))
    pygame.draw.rect(mask, color, (0, corner_radius, w, h - 2 * corner_radius))
    
    # Draw the four filled circles for the corners
    pygame.draw.circle(mask, color, (corner_radius, corner_radius), corner_radius)
    pygame.draw.circle(mask, color, (w - corner_radius, corner_radius), corner_radius)
    pygame.draw.circle(mask, color, (corner_radius, h - corner_radius), corner_radius)
    pygame.draw.circle(mask, color, (w - corner_radius, h - corner_radius), corner_radius)
    
    # Blit the mask onto the surface
    surface.blit(mask, (x, y))