import pygame 
from sys import exit
import math 
from settings import *

pygame.init()
screen = pygame.display.set_mode ((WIDTH , HEIGHT))
pygame.display.set_caption ('Mysetery Case')
clock = pygame.time.Clock()


#Background 
background = pygame.transform.scale(pygame.image.load('MyGame/Bakcground/white.jpeg').convert(), (WIDTH, HEIGHT))


#Player
class Player (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load('MyGame/Character image/ghost.png').convert_alpha(),0, PLAYER_SIZE )
        self.pos = pygame.math.Vector2 (PLAYER_START_X, PLAYER_START_Y)
        self.rect = self.image.get_rect()
        self.speed = PLAYER_SPEED

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0 

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]: 
            self.velocity_y = -self.speed 
        if keys[pygame.K_LEFT]:   
            self.velocity_x = -self.speed 
        if keys[pygame.K_DOWN]: 
            self.velocity_y = self.speed 
        if keys[pygame.K_RIGHT]: 
            self.velocity_x = self.speed 

    def move(self): 
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)


player = Player()

while True: 
    # keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

#     if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:  
#             player.pos[0] -= PLAYER_SPEED
#     if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: 
#             player.pos[0] += PLAYER_SPEED
#     if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
#             player.pos[1] -= PLAYER_SPEED
#     if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: 
#             player.pos[1] += PLAYER_SPEED

    screen.blit (background, (0, 0))
    screen.blit (player.image, player.pos)
    player.user_input()
    player.move ()

    pygame.display.update()
    clock.tick(FPS)
    