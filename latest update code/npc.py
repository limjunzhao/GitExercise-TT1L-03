import pygame , sys
from settings import *
from entity import Entity
from support import * 



class Dialogue(): 
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

class Execution():
    def __init__(self):
        self.dialogue = Dialogue()

    def identify_killer(self,screen):
        killer_dialogue = "Who do you think is the killer?\nA. Maria\nB. Willie\nC. Amber\nD. Officer Marlowe"
        self.dialogue.render_typewriter_new_text(screen, killer_dialogue, BLACK, self.dialogue.speech_rect, SPEECH_FONT)

    def game_over(self, screen):
        self.dialogue.render_typewriter_new_text(screen, "Incorrect! Game Over.", BLACK, self.dialogue.speech_rect, SPEECH_FONT)
        pygame.quit()
        sys.exit()

    def you_win(self, screen):
        self.dialogue.render_typewriter_new_text(screen, "Congratulations! You've identified the killer!", BLACK, self.dialogue.speech_rect, SPEECH_FONT)
        pygame.quit()
        sys.exit()


class NPC(Entity):
    interaction_counts = {npc: 0 for npc in npc_data}

    def __init__(self, npc_name, pos, speech, groups, obstacle_sprites):
        
        #general setup 
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.sprite_type = 'npc'
        self.import_graphic(npc_name)
        
        #import Dialogue and Exucution 
        self.dialogue = Dialogue()
        self.execution = Execution()

        #stats  
        self.npc_name = npc_name
        npc_info = npc_data[self.npc_name]
        self.pos = npc_info['position']
        self.speech = npc_info['speech']
        
        self.image = pygame.Surface((16,16))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites

        self.speech_shown = False # Flag to track if speech is currently shown
        

    def import_graphic(self, name):
        self.animations = {'idle':[]}
        main_path = f'..sprites sheet for maps/sprites/characters/npc/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
               
        #graphics setup 
    def draw(self):
            self.name_surface = FONT.render(self.npc_name, True, WHITE)
            self.name_rect = self.name_surface.get_rect(center=(self.rect.centerx, self.rect.top + 20))
            self.display_surface.blit(self.name_surface, self.name_rect)




    def npc_collision (self, player):
        npc_index = None
        
        
        for i, npc in enumerate(npc_data): #i represented row of the list 
            # self.draw()
            if player.rect.colliderect (self.rect): 

                if not self.speech_shown:
                        self.speech_shown = True
                        speech_text = self.speech
                        npc_index = i
                        NPC.interaction_counts[self.npc_name] += 1

                        if self.npc_name != "officer":
                            self.dialogue.render_typewriter_npc_speech(self.display_surface, self.speech, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                        
                        else:
                            if all(count > 0 for count in self.interaction_counts.values()):
                                self.execution.identify_killer(self.display_surface)
                            else:
                                self.dialogue.render_typewriter_npc_speech(self.display_surface, self.speech, BLACK, self.dialogue.speech_rect, SPEECH_FONT)                        
               
            else:
                self.speech_shown = False  # Reset the flag when the player moves away

    def npc_update(self, player): 
        self.npc_collision(player)
