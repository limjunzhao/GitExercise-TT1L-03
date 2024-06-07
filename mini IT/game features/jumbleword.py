import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 650, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumbled Word Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SEMI_TRANSPARENT_BLACK = (0, 0, 0, 128)

# Load background image
background_image = pygame.image.load('pixel.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Use default pygame fonts
font = pygame.font.Font(None, 48)
instruction_font = pygame.font.Font(None, 28)
score_font = pygame.font.Font(None, 24)

words = ["MARIA", "WILLIE", "OFFICER", "AMBER", "CSS", "JAVASCRIPT", "RUBY"]
word = random.choice(words)
jumbled_word = ''.join(random.sample(word, len(word)))
score = 0
input_text = ""

def display_word():
    text_surface = font.render(jumbled_word, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text_surface, text_rect)

def display_score():
    score_surface = score_font.render("Score: " + str(score), True, WHITE)
    score_rect = score_surface.get_rect(topright=(WIDTH - 20, 20))
    screen.blit(score_surface, score_rect)

def display_instructions(rect):
    instruction_surface = instruction_font.render("Type the correct word and press Enter to submit", True, WHITE)
    instruction_rect = instruction_surface.get_rect(center=(rect.centerx, rect.top + 30))
    screen.blit(instruction_surface, instruction_rect)

def new_word():
    global word, jumbled_word
    word = random.choice(words)
    jumbled_word = ''.join(random.sample(word, len(word)))

def check_answer(answer):
    global score
    if answer.upper() == word:
        score += 1
        new_word()
        return True
    return False

# Function to display the initial screen
def display_initial_screen():
    screen.blit(background_image, (0, 0))
    initial_text = instruction_font.render("Press Enter to start the game", True, WHITE)
    initial_text_rect = initial_text.get_rect(center=(WIDTH / 2, HEIGHT - 50))
    screen.blit(initial_text, initial_text_rect)
    pygame.display.update()

# Game loop
running = True
show_initial_screen = True

while running:
    if show_initial_screen:
        display_initial_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_initial_screen = False
    else:
        screen.blit(background_image, (0, 0))

        # Draw a semi-transparent box
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        rect = pygame.draw.rect(overlay, SEMI_TRANSPARENT_BLACK, (50, 150, WIDTH - 100, 300), border_radius=10)
        screen.blit(overlay, (0, 0))

        display_instructions(rect)
        display_word()
        display_score()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    if check_answer(input_text):
                        if score >= 5:  # Check if score reaches 5
                            running = False
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Render input text in white
        input_surface = font.render(input_text, True, WHITE)
        input_rect = input_surface.get_rect(midtop=(WIDTH / 2, HEIGHT / 2 + 60))
        screen.blit(input_surface, input_rect)

        # Draw line under input text
        pygame.draw.line(screen, WHITE, (input_rect.left, input_rect.bottom + 10), (input_rect.right, input_rect.bottom + 10), 2)

        pygame.display.update()

# Quit pygame
pygame.quit()
