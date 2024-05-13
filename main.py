import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('player.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0,0,0)

# seperate it into a def 
# x y coordinates need to be  changed 
# contoh: called the function , when down pressed insert the coordinates where the sprite sheet starts

animation_list = []
animation_steps = [6]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 145
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_image_list = []
    for _ in range(animation):
        temp_image_list.append(sprite_sheet.get_image( step_counter, 48, 48, 2, BLACK))
        step_counter += 1
    animation_list.append(temp_image_list)

print(animation_list)

    
run = True
while run:

    screen.fill(BG)

    current_time = pygame.time.get_ticks()

    screen.blit(animation_list[action][frame],(0, 0))
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                action = 1
                frame = 0
            if event.key == pygame.K_DOWN:
                action = 2
                frame = 0
    
    pygame.display.update()

pygame.quit()