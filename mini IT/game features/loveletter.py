import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Press Enter to Show Image and Text')

# Load image
love_letter_image = pygame.image.load('love_letter_image.png')
love_letter_image = pygame.transform.scale(love_letter_image, (900, 830))
love_letter_image_rect = love_letter_image.get_rect()
love_letter_image_rect.center = (660, 335)

love_letter_icon = pygame.image.load('love_letter_icon.png')
love_letter_icon = pygame.transform.scale(love_letter_icon, (100, 100))


# Font setup
font = pygame.font.Font(None, 24)

# Messages to display
messages = [
    {"text": "Dearest Willie,",
     "color": (0, 0, 0),
     "position": (410, 200)},
    {"text": "In your presence, my heart dances to a melody only you   ",
     "color": (0, 0, 0),
     "position": (410, 280)},
    {"text": "compose. Your laughter is the rhythm that sets my soul ",
     "color": (0, 0, 0),
     "position": (410, 310)},
    {"text": "alight. With every glance, you paint the canvas of my world",
     "color": (0, 0, 0),
     "position": (410, 340)},
    {"text": "with hues of affection. I am but a poet entranced by your",
     "color": (0, 0, 0),
     "position": (410, 370)},
    {"text": "verses, lost in the depths of your gaze. In your arms, I find",
     "color": (0, 0, 0),
     "position": (410, 400)},
    {"text": "the solace of home, and in your love, I discover the true",
     "color": (0, 0, 0),
     "position": (410, 430)},
    {"text": "essence of belonging.",
     "color": (0, 0, 0),
     "position": (410, 460)},
    {"text": "Love chick,",
     "color": (0, 0, 0),
     "position": (410, 510)},
     {"text": "rawr",
     "color": (0, 0, 0),
     "position": (410, 530)},
]

# Variables
image_visible = False
text_visible = False

def draw_text(messages):
    for message in messages:
        text_surface = font.render(message["text"], True, message["color"])
        screen.blit(text_surface, message["position"])
       

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                image_visible = not image_visible
                text_visible = not text_visible

    # Clear screen
    screen.fill((255, 255, 255))
    screen.blit(love_letter_icon, (0,0)) #adjust icon poossition here!

    # Draw image if visible
    if image_visible:
        screen.blit(love_letter_image, love_letter_image_rect)

    # Draw text if visible
    if text_visible:
        draw_text(messages)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()