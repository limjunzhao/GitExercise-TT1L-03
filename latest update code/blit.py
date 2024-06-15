import pygame
from player import Player

# Initialize Pygame and create a screen object
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create an additional surface for the new page
new_page = pygame.Surface((400, 300))

# Create a player instance
player = Player((100, 100), [], [])

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the main screen
    screen.fill((0, 0, 0))

    # Clear the new page surface
    new_page.fill((50, 50, 50))  # Fill with a different color for distinction

    # Update and animate the player on the main screen
    player.update()
    screen.blit(player.image, player.rect.topleft)

    # Animate multiple animations on the new page
    player.animate_multiple(new_page)

    # Blit the new page surface onto the main screen
    screen.blit(new_page, (200, 150))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
