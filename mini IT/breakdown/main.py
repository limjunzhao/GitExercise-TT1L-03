import pygame
import sys
from npc import NPC, npc_data, handle_npc_interaction
from game_logic import identify_killer, game_over, you_win
from text_rendering import render_typewriter_npc_speech

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FONT = pygame.font.SysFont(None, 24)
SPEECH_FONT = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

player_image = pygame.Surface((50, 50))
player_image.fill(RED)
player_rect = player_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

speech_rect_width = SCREEN_WIDTH - 40
speech_rect_height = SCREEN_HEIGHT // 4
speech_rect = pygame.Rect(20, SCREEN_HEIGHT - speech_rect_height - 20, speech_rect_width, speech_rect_height)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interacting with NPCs")

speech_text = "" 
npc_index = None  
hide_speech = False  
interaction_counts = {npc.name: npc.interaction_count for npc in npc_data}

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a :
                you_win(screen)
            elif event.key in (pygame.K_b, pygame.K_c, pygame.K_d) and hide_speech:
                game_over(screen)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    screen.blit(player_image, player_rect)

    for npc in npc_data:
        npc_rect = pygame.Rect(npc.position[0], npc.position[1], 50, 50)
        pygame.draw.rect(screen, GREEN, npc_rect)  

        if player_rect.colliderect(npc_rect):
            if not hide_speech:
                speech_text = npc.speech
                npc_index = npc_data.index(npc)
                
                render_typewriter_npc_speech(screen, speech_text, BLACK, speech_rect, SPEECH_FONT)
                hide_speech = True  

                interaction_counts[npc.name] += 1

                if all(count > 0 for count in interaction_counts.values()) and npc.name == "Officer Marlowe":
                    identify_killer(screen)

        npc_name_surface = FONT.render(npc.name, True, WHITE)
        npc_name_rect = npc_name_surface.get_rect(center=(npc_rect.centerx + 2, npc_rect.bottom + 20))
        screen.blit(npc_name_surface, npc_name_rect)

    pygame.display.flip()
    clock.tick(60) 

    if npc_index is not None and not player_rect.colliderect(pygame.Rect(npc_data[npc_index].position[0], npc_data[npc_index].position[1], 50, 50)):
        hide_speech = False
