import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Time Code")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Get the current time in milliseconds
    current_time = pygame.time.get_ticks()

    # Convert milliseconds to seconds
    seconds = current_time // 1000

    # Convert seconds to minutes and seconds
    minutes = seconds // 60
    seconds %= 60

    # Render the time on the screen
    font = pygame.font.SysFont(None, 36)
    time_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, BLACK)
    screen.blit(time_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
