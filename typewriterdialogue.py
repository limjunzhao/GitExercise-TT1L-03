import pygame
import sys

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Typewriter Text")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.SysFont(None, 24)

# Define the typewriter texts
typewriter_texts = [
    "This is the first typewriter text example. Press Enter to continue.",
    "This is the second typewriter text example. Press Enter to continue.",
    "This is the third typewriter text example. Press Enter to continue.",
    "This is the fourth typewriter text example. Press Enter to continue.",
]
text_rect = pygame.Rect(20, screen_height - 100, screen_width - 40, 80)

# Function to render typewriter text
def render_typewriter_text(surface, text, font, color, rect, current_char):
    # Render the text up to the current character
    rendered_text = font.render(text[:current_char], True, color)
    surface.blit(rendered_text, (rect.x, rect.y))

# Main loop
clock = pygame.time.Clock()
current_text_index = 0
current_char_index = 0
typing_speed = 5  # Adjust typing speed (lower is faster)
text_completed = False

while True:
    screen.fill(BLACK)  # Clear the screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Check if the text is fully displayed
                if current_char_index >= len(typewriter_texts[current_text_index]):
                    # Move to the next text
                    current_text_index = (current_text_index + 1) % len(typewriter_texts)
                    current_char_index = 0
                    text_completed = False

    # Render the typewriter text if not completed
    if not text_completed:
        render_typewriter_text(screen, typewriter_texts[current_text_index], font, WHITE, text_rect, current_char_index)
        # Increment the character index to simulate typing effect
        if current_char_index < len(typewriter_texts[current_text_index]):
            current_char_index += 1
        else:
            text_completed = True

    pygame.display.flip()
    clock.tick(20)  # Adjust typing s
