import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Load an example image or draw a scene
background = pygame.Surface((screen_width, screen_height))
background.fill((255, 0, 0))  # Example scene: a red background

# Function to fade out
def fade_out(screen, width, height):
    fade_surface = pygame.Surface((width, height))
    fade_surface = fade_surface.convert()
    fade_surface.fill((0, 0, 0))
    
    
    for alpha in range(0, 256):  # Alpha ranges from 0 (transparent) to 255 (opaque)
        fade_surface.set_alpha(alpha)
        screen.blit(background, (0, 0))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

# Function to fade in
def fade_in(screen, width, height):
    fade_surface = pygame.Surface((width, height))
    fade_surface = fade_surface.convert()
    fade_surface.fill((0, 0, 0))
    
    for alpha in range(255, -1, -1):  # Alpha ranges from 255 (opaque) to 0 (transparent)
        fade_surface.set_alpha(alpha)
        screen.blit(background, (0, 0))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fade_out(screen, screen_width, screen_height)
                pygame.time.delay(1000)  # Wait for 1 second
                fade_in(screen, screen_width, screen_height)

    # Draw the scene
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()