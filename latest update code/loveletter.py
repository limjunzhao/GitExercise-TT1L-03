import pygame
import random
import time

# Initialize Pygame
pygame.init()

# New screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Love Letter Minigame')

# Load background image
background_image = pygame.image.load('images/loveletter/pixel.png').convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load love letter image
love_letter_image = pygame.image.load('images/loveletter/love_letter_image.png').convert_alpha()
love_letter_image = pygame.transform.scale(love_letter_image, (WIDTH, HEIGHT))
love_letter_image_rect = love_letter_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SEMI_TRANSPARENT_BLACK = (0, 0, 0, 128)

# Fonts
font = pygame.font.Font(None, 36)
instruction_font = pygame.font.Font(None, 24)
score_font = pygame.font.Font(None, 24)
cursive_font_path = 'images/loveletter/font/GreatVibes-Regular.ttf'  # Path to the cursive font file
love_letter_font = pygame.font.Font(cursive_font_path, 22)  # Load cursive font

# Messages to display
messages = [
    {"text": "Dearest Willie,", "color": (0, 0, 0), "position": (180, 200)},
    {"text": "In your presence, my heart dances to a melody only you", "color": (0, 0, 0), "position": (180, 230)},
    {"text": "compose. Your laughter is the rhythm that sets my soul", "color": (0, 0, 0), "position": (180, 260)},
    {"text": "alight. With every glance, you paint the canvas of my world", "color": (0, 0, 0), "position": (180, 290)},
    {"text": "with hues of affection. I am but a poet entranced by your", "color": (0, 0, 0), "position": (180, 320)},
    {"text": "verses, lost in the depths of your gaze. In your arms, I find", "color": (0, 0, 0), "position": (180, 350)},
    {"text": "the solace of home, and in your love, I discover the true", "color": (0, 0, 0), "position": (180, 380)},
    {"text": "essence of belonging.", "color": (0, 0, 0), "position": (180, 410)},
    {"text": "Love sidechick,", "color": (0, 0, 0), "position": (180, 440)},
    {"text": "rawr", "color": (0, 0, 0), "position": (180, 470)},
]

# Words for the jumbled word game and their hints
word_hints = {
    "DETECTIVE": "Hint: Someone who solves crimes and investigates mysteries.",
    "LETTER": "Hint: A written thing commonly writing to someone.",
    "ARCADIA": "Hint: The name of the village where the murders took place.",
    "TRANQUILITY": "Hint: A peaceful and calm atmosphere.",
    "MURDER": "Hint: The person responsible for the grisly acts.",
    "GRISLY": "Hint: Something that is horrifying, gruesome.",
    "MYSTERY": "Hint: Something that is difficult or impossible to understand or explain.",
    "DAMPED": "Hint: Slightly wet, often unpleasantly so."
}

# Game variables
word = random.choice(list(word_hints.keys()))
jumbled_word = ''.join(random.sample(word, len(word)))
score = 0
input_text = ""
show_initial_screen = True
show_love_letter = False  # Flag to control when to show the love letter
hint_active = False
hint_start_time = 0

# Functions
def display_word():
    text_surface = font.render(jumbled_word, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text_surface, text_rect)

def display_score():
    score_surface = score_font.render("Score: " + str(score), True, WHITE)
    score_rect = score_surface.get_rect(topright=(WIDTH - 20, 20))
    screen.blit(score_surface, score_rect)

def display_instructions():
    instruction_surface = instruction_font.render("Type the correct word and press Enter to submit", True, WHITE)
    instruction_rect = instruction_surface.get_rect(midtop=(WIDTH / 2, 200))  # Adjusted position
    box_height = 300  # Height of the semi-transparent box
    instruction_rect.y = 30 + (box_height - instruction_surface.get_height()) // 2  # Position significantly higher in the box
    screen.blit(instruction_surface, instruction_rect)
    
    hint_instruction_surface = instruction_font.render("Press Tab for hint", True, WHITE)
    hint_instruction_rect = hint_instruction_surface.get_rect(midtop=(WIDTH / 2, 250))  # Adjusted position
    screen.blit(hint_instruction_surface, hint_instruction_rect)

def new_word():
    global word, jumbled_word
    word = random.choice(list(word_hints.keys()))
    jumbled_word = ''.join(random.sample(word, len(word)))

def check_answer(answer):
    global score
    if answer.upper() == word:
        if score < 5:
            score += 1
        new_word()
        return True
    return False

def display_initial_screen():
    screen.blit(background_image, (0, 0))
    initial_text1 = instruction_font.render("Press Enter to start the game", True, WHITE)
    initial_text_rect1 = initial_text1.get_rect(center=(WIDTH / 2, HEIGHT - 100))
    screen.blit(initial_text1, initial_text_rect1)
    
    initial_text2 = instruction_font.render("Welcome to the Love Letter Minigame!", True, WHITE)
    initial_text_rect2 = initial_text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))  # Adjusted position
    screen.blit(initial_text2, initial_text_rect2)
    
    initial_text3 = instruction_font.render("1. This is a jumbled-word minigame.", True, WHITE)
    initial_text_rect3 = initial_text3.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 40))  # Adjusted position
    screen.blit(initial_text3, initial_text_rect3)
    
    initial_text4 = instruction_font.render("2. Answers can be found in the storyline.", True, WHITE)
    initial_text_rect4 = initial_text4.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 10))  # Adjusted position
    screen.blit(initial_text4, initial_text_rect4)
    
    initial_text5 = instruction_font.render("3. New words will not display until you get it correctly.", True, WHITE)
    initial_text_rect5 = initial_text5.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 20))  # Adjusted position
    screen.blit(initial_text5, initial_text_rect5)
    
    pygame.display.update()

def display_hint():
    hint_text = word_hints[word]
    hint_surface = instruction_font.render(hint_text, True, WHITE)
    hint_rect = hint_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 120))
    screen.blit(hint_surface, hint_rect)

# Main game loop
running = True
while running:
    if show_initial_screen:
        display_initial_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_initial_screen = False
                    # Reset score and show_love_letter flag when starting a new game
                    score = 0
                    show_love_letter = False
    else:
        screen.blit(background_image, (0, 0))

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    if check_answer(input_text):
                        input_text = ""
                        # Check if the score reaches 5 to show the love letter
                        if score == 5:
                            show_love_letter = True
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace to delete characters from input_text
                    input_text = input_text[:-1]
                elif event.key in (pygame.K_SPACE, pygame.K_MINUS):
                    # Handle space and minus key for multi-word inputs
                    input_text += " "
                elif event.key in range(pygame.K_a, pygame.K_z + 1):
                    # Handle typing letters
                    input_text += event.unicode
                elif event.key == pygame.K_TAB:
                    # Activate hint
                    hint_active = True
                    hint_start_time = time.time()

        # Draw a semi-transparent box
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        rect = pygame.draw.rect(overlay, SEMI_TRANSPARENT_BLACK, (50, 150, WIDTH - 100, 300), border_radius=10)
        screen.blit(overlay, (0, 0))

        display_instructions()
        display_word()
        display_score()

        # Render input text in white
        input_surface = font.render(input_text, True, WHITE)
        input_rect = input_surface.get_rect(midtop=(WIDTH / 2, HEIGHT / 2 + 60))
        screen.blit(input_surface, input_rect)

        # Draw line under input text
        pygame.draw.line(screen, WHITE, (input_rect.left, input_rect.bottom + 10), (input_rect.right, input_rect.bottom + 10), 2)

        # Display hint if active
        if hint_active:
            display_hint()
            if time.time() - hint_start_time > 3:
                hint_active = False

        # Display love letter only when score is 5
        if show_love_letter:
            screen.blit(love_letter_image, love_letter_image_rect)
            for message in messages:
                text_surface = love_letter_font.render(message["text"], True, message["color"])
                screen.blit(text_surface, message["position"])

        pygame.display.update()

# Quit pygame
pygame.quit()
