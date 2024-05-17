import pygame
pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 60

# Player
PLAYER_START_X = 400
PLAYER_START_Y = 500
PLAYER_SIZE = 0.2
PLAYER_SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mystery Case')
clock = pygame.time.Clock()

# Background
background = pygame.transform.scale(pygame.image.load('image/background/plain_white.jpg').convert(), (WIDTH, HEIGHT))

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.transform.rotozoom(pygame.image.load('ghost.png').convert_alpha(), 0, PLAYER_SIZE)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(PLAYER_START_X, PLAYER_START_Y))
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.speed = PLAYER_SPEED

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.velocity_y = -self.speed
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
            self.image = self.original_image  # Reset image to original when moving right
        if keys[pygame.K_DOWN]:
            self.velocity_y = self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
            self.image = pygame.transform.flip(self.original_image, True, False)  # Flip horizontally
            

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
        self.rect.center = self.pos


player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    player.user_input()
    player.move()
    screen.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
