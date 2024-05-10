import pygame 
import spritesheets 

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720 

screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption ('sprites sheet')

sprite_sheet_image = pygame.image.load('../sprites sheet for maps/sprites/characters/player.png').convert_alpha()
                #def __init__          (self, image): from spritesheets
sprite_sheet = spritesheets.SpriteSheets(sprite_sheet_image)

BG = (50,50,50)
BLACK = (0,0,0)


        #get_image(sheet,           frame, width, height, scale, colour):
frame_0 = sprite_sheet.get_image(0, 48, 48, 3, BLACK)
frame_1 = sprite_sheet.get_image(1, 48, 48, 3, BLACK)
frame_2 = sprite_sheet.get_image(2, 48, 48, 3, BLACK)
frame_3 = sprite_sheet.get_image(3, 48, 48, 3, BLACK)
frame_4 = sprite_sheet.get_image(4, 48, 48, 3, BLACK)
frame_5 = sprite_sheet.get_image(5, 48, 48, 3, BLACK)
frame_6 = sprite_sheet.get_image(6, 48, 48, 3, BLACK)

run = True
while run:
    #update background
    screen.fill(BG)
    #display image
    #screen.blit(sprite_sheet_image,(0,0))
    screen.blit (frame_0, (0,0))
    screen.blit (frame_1, (48,0))
    screen.blit (frame_2, (96,0))
    screen.blit (frame_3, (144,0))
    screen.blit (frame_4, (192,0))
    screen.blit (frame_5, (240,0))
    screen.blit (frame_6, (0,48))
    # screen.blit (frame_7, (0,96))

    #event handler
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          run = False


    pygame.display.update()
pygame.quit()