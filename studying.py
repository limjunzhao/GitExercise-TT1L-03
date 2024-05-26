import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game with Pause Functionality')

# Set up the clock
clock = pygame.time.Clock()

# Set up a dummy level class
class Level:
    def run(self):
        # Replace this with actual game logic
        pygame.draw.rect(screen, (0, 255, 0), (100, 100, 50, 50))

# Set up a dummy button class
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        font = pygame.font.Font(None, 36)
        text_surf = font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surf, self.rect.topleft)

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)

# Create instances
self = type('', (), {})()  # Dummy self
self.level = Level()
self.camera_group = type('', (), {})()  # Dummy camera_group
self.camera_group.update = lambda: None

# Create a button instance
vol_up_button = Button(350, 250, 100, 50, 'Vol Up')

# Pause game surface
pause_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pause_surface.fill((0, 0, 0, 180))  # Semi-transparent overlay

pause = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pause = not pause  # Toggle the pause state
            if not pause:
                screen.fill('black')  # Clear the screen when unpausing

        if event.type == pygame.MOUSEBUTTONDOWN and pause:
            if vol_up_button.collidepoint(event.pos):
                print("a")

    if pause:
        screen.blit(pause_surface, (0, 0))
        vol_up_button.draw(screen)
    else:
        screen.fill('black')
        self.level.run()
        self.camera_group.update()

    pygame.display.update()
    clock.tick(FPS)
