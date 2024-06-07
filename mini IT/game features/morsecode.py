import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)  # White background
BLACK = (0, 0, 0)  # Black text
WHITE = (255, 255, 255)  # White text
GREEN = (0, 255, 0)  # Green text for correct!
RED = (255, 0, 0)  # Red text for incorrect
FONT_SIZE = 24
NOTES_WIDTH = 300
X_OFFSET_RIGHT = 160  # Adjust this value to control the right offset for letters T-Z

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
}

# Function to draw text on the screen
def draw_text(surface, text, position, font, color=BLACK):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)
    return text_surface.get_width()  # Return the width of the rendered text

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Morse Code Minigame')
font = pygame.font.Font(None, FONT_SIZE)

# Load the start screen image and scale it to fill the window
start_screen_image = pygame.image.load('images/minigame/library.jpeg')
start_screen_image = pygame.transform.scale(start_screen_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Display instructions to start the game
def display_start_screen():
    waiting_for_start = True
    while waiting_for_start:
        screen.fill(BACKGROUND_COLOR)

        # Blit the start screen image
        screen.blit(start_screen_image, (0, 0))

        # Draw the start message in white
        draw_text(screen, 'Press Enter to start the game', (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 100), font, WHITE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_start = False
                    return

# Display instructions screen
def display_instructions_screen():
    waiting_for_instructions = True
    while waiting_for_instructions:
        screen.fill(BACKGROUND_COLOR)

        # Blit the start screen image
        screen.blit(start_screen_image, (0, 0))

        # Draw the instructions header
        header = "Instructions:"
        draw_text(screen, header, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 - 120), font, WHITE)

        # Draw semi-transparent black background
        instructions_background_rect = pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100, 400, 240)
        pygame.draw.rect(screen, (0, 0, 0, 150), instructions_background_rect)

        instructions = [
            "1. Complete this minigame to graduate",
            "2. It's a Morse code-based game",
            "3. Fill up the words with Morse codes"
        ]
        y_offset = SCREEN_HEIGHT // 2 - 80
        for instruction in instructions:
            draw_text(screen, instruction, (SCREEN_WIDTH // 2 - 180, y_offset), font, WHITE)
            y_offset += FONT_SIZE + 10

        # Draw the start message in white
        draw_text(screen, 'Press Enter to continue', (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100), font, WHITE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_instructions = False
                    return

# Game variables
# Define cursor position variables
cursor_x = NOTES_WIDTH + 20
cursor_y = 220

# Constants for cursor boundaries
CURSOR_MIN_X = NOTES_WIDTH + 20
CURSOR_MAX_X = NOTES_WIDTH + 260  # Adjust this value to set the maximum x-coordinate

questions = [
    ("Translate 'HELLO' to Morse Code", ".... . .-.. .-.. ---"),
    ("Translate 'WORLD' to Morse Code", ".-- --- .-. .-.. -.."),
    ("Translate 'PYTHON' to Morse Code", ".--. -.-- - .... --- -."),
    ("Translate 'GAME' to Morse Code", "--. .- -- ."),
    ("Translate 'OPENAI' to Morse Code", "--- .--. . -. .- ..")
]
random.shuffle(questions)
current_question_index = 0
current_question, answer = questions[current_question_index]
current_input = ''
correct = None

# Display start screen
display_start_screen()

# Display instructions screen
display_instructions_screen()

# Main game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Draw Morse code notes on the left side with semi-transparent background
    notes_rect = pygame.Rect(10, 10, NOTES_WIDTH + 5, SCREEN_HEIGHT - 20)
    pygame.draw.rect(screen, (200, 200, 200, 150), notes_rect)  # Semi-transparent gray background

    y_offset = 20
    draw_text(screen, 'Morse Code Notes:', (20, y_offset), font)
    y_offset += FONT_SIZE + 10
    for letter, morse in MORSE_CODE_DICT.items():
        x_offset = 20
        if letter > 'S':
            x_offset += X_OFFSET_RIGHT
        draw_text(screen, f'{letter}: {morse}', (x_offset, y_offset), font)
        y_offset += FONT_SIZE + 5
        if y_offset > SCREEN_HEIGHT - FONT_SIZE:
            y_offset = 20

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(current_input) > 0:
                    char_width = font.render(current_input[-1], True, BLACK).get_width()
                    current_input = current_input[:-1]
                    cursor_x -= char_width
                if cursor_x < CURSOR_MIN_X:
                    cursor_x = CURSOR_MIN_X
            elif event.key == pygame.K_RETURN:
                correct = (current_input.strip() == answer)
                if correct:
                    # Move to the next question
                    current_question_index += 1
                    if current_question_index < len(questions):
                        current_question, answer = questions[current_question_index]
                        current_input = ''
                    else:
                        # If all questions are answered, end the game
                        pygame.time.wait(2000)
                        running = False
                else:
                    current_input = ''  # Clear input box on incorrect answer
                # Reset cursor position
                cursor_x = CURSOR_MIN_X
            elif event.key == pygame.K_ESCAPE:
                # Quit the game if Escape key is pressed
                pygame.quit()
                sys.exit()
            else:
                current_input += event.unicode.upper()
                char_width = font.render(event.unicode.upper(), True, BLACK).get_width()
                cursor_x += char_width
                if cursor_x > CURSOR_MAX_X:
                    cursor_x = CURSOR_MAX_X

    # Draw question on the right side
    draw_text(screen, 'Question:', (NOTES_WIDTH + 20, 20), font)
    draw_text(screen, current_question, (NOTES_WIDTH + 20, 20 + FONT_SIZE + 5), font)
    draw_text(screen, '* make sure to enter space', (NOTES_WIDTH + 20, 20 + FONT_SIZE + 5 + 30), font)

    # Draw user input
    draw_text(screen, 'Your Input:', (NOTES_WIDTH + 20, 200), font)
    # Draw line under your input
    pygame.draw.line(screen, BLACK, (NOTES_WIDTH + 15, 260), (NOTES_WIDTH + 265, 260), 2)
    draw_text(screen, current_input, (NOTES_WIDTH + 20, 200 + FONT_SIZE + 5), font)
    
    # Draw cursor
    pygame.draw.line(screen, BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + FONT_SIZE), 2)

    # Display correctness
    if correct is not None:
        if correct:
            draw_text(screen, 'Correct!', (NOTES_WIDTH + 20, 300), font, GREEN)
        else:
            draw_text(screen, 'Incorrect, try again.', (NOTES_WIDTH + 20, 300), font, RED)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
