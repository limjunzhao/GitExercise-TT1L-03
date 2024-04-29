import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interacting with NPCs")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.SysFont(None, 24)

# Player image
player_image = pygame.Surface((50, 50))
player_image.fill((255, 0, 0))  # Red color for player
player_rect = player_image.get_rect(center=(screen_width // 2, screen_height // 2))

# NPC data (position, name, and speech text)
npc_data = [
    {"name": "Maria", "position": (100, 100), "speech": "Hi there, adventurer!"},
    {"name": "Amber", "position": (600, 100), "speech": "Greetings, traveler!"},
    {"name": "Police", "position": (100, 400), "speech": "Hey, how's it going?"},
    {"name": "Willie", "position": (600, 400), "speech": "Hello, friend!"},
]

# Speech bubble variables
speech_text = ""
speech_rect = pygame.Rect(0, screen_height * 3 // 4, screen_width, screen_height // 4)

# Function to check collision with NPCs
def check_npc_collision(player_rect, npc_rect):
    return player_rect.colliderect(npc_rect)

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)  # Clear the screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # Move the player based on arrow key inputs
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    # Reset speech text if player is not colliding with any NPC
    speech_text = ""

    # Draw the player
    screen.blit(player_image, player_rect)

    # Draw NPCs and handle interactions
    for npc in npc_data:
        npc_rect = pygame.Rect(npc["position"][0], npc["position"][1], 50, 50)
        pygame.draw.rect(screen, (0, 255, 0), npc_rect)  # Green color for NPCs

        # Check for collision with NPCs
        if check_npc_collision(player_rect, npc_rect):
            speech_text = npc["speech"]

        # Draw NPC name below them
        npc_name_surface = font.render(npc["name"], True, WHITE)
        npc_name_rect = npc_name_surface.get_rect(center=(npc_rect.centerx, npc_rect.bottom + 10))
        screen.blit(npc_name_surface, npc_name_rect)

    # Draw the speech bubble if there's text
    if speech_text:
        pygame.draw.rect(screen, WHITE, speech_rect, 0, 10)
        pygame.draw.rect(screen, BLACK, speech_rect, 2, 10)

        # Draw the speech text
        speech_surface = font.render(speech_text, True, BLACK)
        speech_text_rect = speech_surface.get_rect(center=speech_rect.center)
        screen.blit(speech_surface, speech_text_rect)

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS
