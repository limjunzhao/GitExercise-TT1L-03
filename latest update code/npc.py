import pygame 
from settings import *
from entity import Entity
from support import *




class NPC(pygame.sprite,Sprite):
    def __init__(self, name, position, speech, groups):

        #general setup 
        super().__init__(groups)
        # self.sprite_type = 'npc'


        self.name = name
        self.position = position
        self.speech = speech
        self.interaction_count = 0
        
        #graphics setup 
        self.image   = pygame.image.load('sprites sheet for maps/sprites/characters/player_single.png').convert_alpha()
        self.rect = self.image.get_rect ()
        self.hitbox = self.rect.inflate(0,-10)


    def draw(self, surface):
        name_surface = FONT.render(self.name, True, WHITE)
        name_rect = name_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 20))
        surface.blit(self.image, self.rect)
        surface.blit(name_surface, name_rect)


class Dialogue: 
    def __init__(self):
        self.speech_rect_width = WIDTH - 40
        self.speech_rect_height = HEIGHT // 4
        self.speech_rect = pygame.Rect(20, HEIGHT - self.speech_rect_height - 20, self.speech_rect_width, self.speech_rect_height)

    def draw_text(self, surface, text, color, rect, font):
        words = text.split(' ')
        lines = []
        line = ''
        for word in words:
            test_line = line + word + ' '
            if font.size(test_line)[0] < rect.width:
                line = test_line
            else:
                lines.append(line)
                line = word + ' '
        lines.append(line)

        y = rect.top + 10
        for line in lines:
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect(topleft=(rect.left + 5, y))
            surface.blit(text_surface, text_rect)
            y += font.get_linesize()

    def render_typewriter_npc_speech(self, surface, text, color, rect, font):
        for i in range(len(text) + 1):
            pygame.draw.rect(surface, WHITE, rect, 0, 10)
            pygame.draw.rect(surface, BLACK, rect, 2, 10)
            self.draw_text(surface, text[:i], color, rect, font)
            pygame.display.flip()
            clock.tick(20)
        pygame.time.wait(1000)

    def render_typewriter_new_text(self, surface, text, color, rect, font):
        for i in range(len(text) + 1):
            pygame.draw.rect(surface, WHITE, rect, 0, 10)
            pygame.draw.rect(surface, BLACK, rect, 2, 10)
            self.draw_text(surface, text[:i], color, rect, font)
            pygame.display.flip()
            clock.tick(20)
        pygame.time.wait(3000)

class Execution:
    def __init__(self):
        self.dialogue = Dialogue()

    def identify_killer(self):
        new_text = "Who do you think is the killer?\nA. Maria\nB. Willie\nC. Amber\nD. Officer Marlowe"
        self.dialogue.render_typewriter_new_text(screen, new_text, BLACK, self.dialogue.speech_rect, SPEECH_FONT)

    def game_over(self):
        self.dialogue.render_typewriter_new_text(screen, "Incorrect! Game Over.", BLACK, self.dialogue.speech_rect, SPEECH_FONT)
        pygame.quit()
        sys.exit()

    def you_win(self):
        self.dialogue.render_typewriter_new_text(screen, "Congratulations! You've identified the killer!", BLACK, self.dialogue.speech_rect, SPEECH_FONT)
        pygame.quit()
        sys.exit()



# npcs = [NPC(npc["name"], npc["position"], npc["speech"], npc['groups']) for npc in npc_data]
# interaction_counts = {npc["name"]: 0 for npc in npc_data}
# dialogue = Dialogue()
# execution = Execution()

# while True:
#     self.screen.fill(BLACK)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 execution.you_win()
#             elif event.key in (pygame.K_b, pygame.K_c, pygame.K_d) and hide_speech:
#                 execution.game_over()

#     player.update()

#     for i, npc in enumerate(npcs):
#         npc.draw(screen)
#         if player.rect.colliderect(npc.rect):
#             if not hide_speech:
#                 speech_text = npc.speech
#                 npc_index = i
#                 npc.interaction_count += 1
#                 interaction_counts[npc.name] += 1

#                 if npc.name != "Officer Marlowe":
#                     dialogue.render_typewriter_npc_speech(screen, speech_text, BLACK, dialogue.speech_rect, SPEECH_FONT)
#                 else:
#                     if all(count > 0 for count in interaction_counts.values()):
#                         execution.identify_killer()
#                     else:
#                         dialogue.render_typewriter_npc_speech(screen, speech_text, BLACK, dialogue.speech_rect, SPEECH_FONT)

#                 hide_speech = True  

#     screen.blit(player.image, player.rect)
#     pygame.display.flip()
#     clock.tick(60)

#     if npc_index is not None and not player.rect.colliderect(npcs[npc_index].rect):
#         hide_speech = False