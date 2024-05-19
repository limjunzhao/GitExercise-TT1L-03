import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumbled Word Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 48)
instruction_font = pygame.font.Font(None, 32)
score_font = pygame.font.Font(None, 24)

# Game variables
words = ["PYTHON", "JAVASCRIPT", "JAVA", "HTML", "CSS", "RUBY", "PHP"]
word = random.choice(words)
jumbled_word = ''.join(random.sample(word, len(word)))
score = 0
input_text = ""

def display_word():
    text_surface = font.render(jumbled_word, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text_surface, text_rect)

def display_score():
    score_surface = score_font.render("Score: " + str(score), True, BLACK)
    score_rect = score_surface.get_rect(topright=(WIDTH - 20, 20))
    screen.blit(score_surface, score_rect)

def display_instructions():
    instruction_surface = instruction_font.render("Type the correct word and press Enter to submit", True, BLACK)
    instruction_rect = instruction_surface.get_rect(midtop=(WIDTH / 2, 20))
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

# Game loop
running = True
while running:
    screen.fill(WHITE)

    display_instructions()
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
                check_answer(input_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Render input text
    input_surface = font.render(input_text, True, BLACK)
    input_rect = input_surface.get_rect(midtop=(WIDTH / 2, HEIGHT / 2 + 60))
    screen.blit(input_surface, input_rect)

    # Draw line under input text
    pygame.draw.line(screen, BLACK, (input_rect.left, input_rect.bottom + 10), (input_rect.right, input_rect.bottom + 10), 2)

    pygame.display.update()
