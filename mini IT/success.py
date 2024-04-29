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
    {"name": "Maria", "position": (100, 100), "speech": "In the morning, I made breakfast for my husband, then proceeded to do house chores until afternoon. After lunch with my husband, I engaged in a pleasant chit-chat with our neighbor, Amber. Later, I eagerly awaited my husband’s return from work, and once he was back, we cooked dinner together and went to sleep afterwards."},
    {"name": "Willie", "position": (600, 100), "speech": "Breakfast with my wife started the day, followed by me heading to work. Proceeds to head to lunch with my wife and returned to work. Finally, I came back home and got the ingredients ready and cooked dinner with my wife. Lastly, we went to bed before 10pm."},
    {"name": "Amber", "position": (100, 400), "speech": "In the day, I exercised in the park. And after that I had my coffee and breakfast. Meanwhile I watched TV for the time to pass. During lunch, I ate my leftover dinner from yesterday as my lunch. After lunch, me and Maria had our usual chit-chat but it was shorter than usual. And we were supposed to get groceries after that. So I went to buy the groceries myself and made dinner. As night falls, I took my dog for a night walk and went to bed."},
    {"name": "Police", "position": (600, 400), "speech": "Please help me find the killer before it's too late!"},
]

# Speech bubble variables
speech_text = ""
speech_rect = pygame.Rect(0, screen_height * 3 // 4, screen_width, screen_height // 4)

# Typewriter effect variables
typing_speed = 50  # Adjust typing speed here
current_char = 0
next_char_time = pygame.time.get_ticks()

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

    # Typewriter effect for speech text
    if speech_text:
        current_time = pygame.time.get_ticks()
        if current_time > next_char_time:
            if current_char < len(speech_text):
                current_char += 1
                next_char_time = current_time + typing_speed

        # Display text up to current character
        text_to_display = speech_text[:current_char]

        # Draw the speech bubble
        pygame.draw.rect(screen, WHITE, speech_rect, 0, 10)
        pygame.draw.rect(screen, BLACK, speech_rect, 2, 10)

        # Draw the speech text
        speech_surface = font.render(text_to_display, True, BLACK)
        speech_text_rect = speech_surface.get_rect(center=speech_rect.center)
        screen.blit(speech_surface, speech_text_rect)

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS
