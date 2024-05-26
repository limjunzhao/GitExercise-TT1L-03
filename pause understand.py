import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up main game display
width, height = 800, 600
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Function to handle the pause window
def pause_menu():
    # Set up pause window
    pause_window = pygame.Surface((400, 300))
    pause_window.fill(white)
    font = pygame.font.Font(None, 36)
    text = font.render("Paused. Press ENTER to resume.", True, red)
    text_rect = text.get_rect(center=(200, 150))
    pause_window.blit(text, text_rect)

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to resume
                    paused = False
        
        # Draw the pause window on the game window
        game_window.blit(pause_window, ((width - 400) // 2, (height - 300) // 2))
        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Main game loop
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Press 'P' to pause
                paused = True
                pause_menu()

    if not paused:
        # Game logic and drawing here
        game_window.fill(black)
        font = pygame.font.Font(None, 36)
        text = font.render("Main Game. Press 'P' to pause.", True, white)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        game_window.blit(text, text_rect)

        pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
