import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Countdown Timer")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up variables
clock = pygame.time.Clock()
time_remaining = 10
task_completed = False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and time_remaining > 0:
                task_completed = True

    # Update timer
    if not task_completed and time_remaining > 0:
        time_remaining -= clock.get_rawtime() / 1000
        if time_remaining <= 0:
            time_remaining = 0

    # Fill the screen with white
    screen.fill(WHITE)

    # Render the timer text
    timer_text = font.render(f"Time Remaining: {int(time_remaining)} seconds", True, BLACK)
    screen.blit(timer_text, (50, 50))

    # Render the task completion message if applicable
    if task_completed:
        task_complete_text = font.render("Task Completed!", True, BLACK)
        screen.blit(task_complete_text, (WIDTH // 2 - task_complete_text.get_width() // 2, HEIGHT // 2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
