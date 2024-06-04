import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Press Enter to Show Image and Text')

# Load image
love_letter_image = pygame.image.load('love_letter_image.png')
love_letter_image = pygame.transform.scale(love_letter_image, (1280, 830))
love_letter_image_rect = love_letter_image.get_rect()
love_letter_image_rect.center = (660, 335)

love_letter_icon = pygame.image.load('love_letter_icon.png')
love_letter_icon = pygame.transform.scale(love_letter_icon, (100, 100))


# Font setup
font = pygame.font.Font(None, 60)

# Messages to display
messages = [
    {"text": "lol he cheated on u bruh",
     "color": (0, 0, 0),
     "position": (360,210)},
    {"text": "¯\_(*-*)_/¯ ¯\_(*-*)_/¯ ¯\_(*-*)_/¯¯\_(*-*)_/¯  ",
     "color": (0, 0, 0),
     "position": (310, 300)},
    {"text": "¯\_(*-*)_/¯ ¯\_(*-*)_/¯ ¯\_(*-*)_/¯¯\_(*-*)_/¯ ",
     "color": (0, 0, 0),
     "position": (310, 400)},
    {"text": "¯\_(*-*)_/¯ ¯\_(*-*)_/¯ ¯\_(*-*)_/¯¯\_(*-*)_/¯ ",
     "color": (0, 0, 0),
     "position": (310, 500)}
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
