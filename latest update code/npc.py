import pygame , sys
from settings import *
from entity import Entity
from support import * 



class Dialogue(): 
    def __init__(self):
        self.speech_rect_width = WIDTH - 40
        self.speech_rect_height = HEIGHT // 4
        self.speech_rect = pygame.Rect(20, HEIGHT - self.speech_rect_height - 20, self.speech_rect_width, self.speech_rect_height)


        self.line_status = False
        self.all_line_status = False
        self.skip = False


    def escape_dialogue_text_display (self, screen, text, rect, font, color): 
        skip_text = "Press TAB key to escape the dialogue"

        self.text_surface = FONT.render(skip_text, True, BLACK)
        self.text_rect = self.text_surface.get_rect(bottomright = (self.speech_rect.x + 1220, self.speech_rect.y + 170))
        screen.blit(self.text_surface, self.text_rect)

    def display_text(self, surface, text, rect, font, color):
            x_offset = rect[0] + 10
            y_offset = rect[1] + 10

            collection = [word.split(' ') for word in text.splitlines()]
            space = font.size(' ')[0]
            x,y = x_offset, y_offset
            for lines in collection:
                for texts in lines:
                    texts_surface = font.render(texts, True, color)
                    texts_rect = texts_surface.get_rect(topleft=(rect.left + 5, y))
                    texts_width , texts_height = texts_surface.get_size()
                    if x + texts_width >= 1260:
                        x = x_offset
                        y += texts_height

                    surface.blit(texts_surface, (x,y))
                    x += texts_width + space
                x = x_offset
                y += texts_height + 10

    def draw_text(self, surface, text, color, rect, font):

            msgs = text.split(' ')
            lines = []
            line = ''
            for msg in msgs:
                test_line = line + msg + ' '
                if font.size(test_line)[0] < rect.width : #1st row of the dialogue
                    line = test_line
  
                else:
                    lines.append(line) 
                    line = msg + ' '
            lines.append(line) 

            y = rect.top + 10
            for line in lines:
                text_surface = font.render(line, True, color)
                text_rect = text_surface.get_rect(topleft=(rect.left + 10, y))
                surface.blit(text_surface, text_rect)
                y += font.get_linesize()


    def render_instant_npc_speech(self, surface, text, color, rect, font):
            for i in range(len(text) + 1):
                #text bubble
                pygame.draw.rect(surface, WHITE, rect, 0, 10)
                pygame.draw.rect(surface, BLACK, rect, 2, 10) 
                self.escape_dialogue_text_display (surface, text, rect, font, color)
                self.display_text(surface, text, rect, font, color)
                pygame.display.flip()
                clock.tick(30)
            
        

    def render_typewriter_npc_speech(self, surface, text, color, rect, font):
            for i in range(len(text) + 1):
                self.skip = False
                #text bubble
                pygame.draw.rect(surface, WHITE, rect, 0, 10)
                pygame.draw.rect(surface, BLACK, rect, 2, 10)
                self.escape_dialogue_text_display (surface, text, rect, font, color)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.skip = True 
                            self.render_instant_npc_speech(surface, text, color, rect, font)

                            return self.skip 

                else: 
                    self.draw_text(surface, text[:i], color, rect, font)
                    
                pygame.display.flip()
                clock.tick(20)
            
        
        

    def render_typewriter_new_text(self, surface, text, color, rect, font):
        for i in range(len(text) + 1):
            #text bubble
            pygame.draw.rect(surface, WHITE, rect, 0, 10)
            pygame.draw.rect(surface, BLACK, rect, 2, 10)
            self.escape_dialogue_text_display (surface, text, rect, font, color)
            self.draw_text(surface, text[:i], color, rect, font)
            pygame.display.flip()
            clock.tick(20)
        


class Execution():
    def __init__(self):
        self.dialogue = Dialogue()

    def identify_killer(self,screen):
        killer_dialogue = "Who do you think is the killer?\n A. Maria\n B. Willie\n C. Amber\n D. Officer Marlowe"
        self.dialogue.render_instant_npc_speech(screen, killer_dialogue, BLACK, self.dialogue.speech_rect, SPEECH_FONT)

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
        self.greeting = npc_info.get('greeting')
        self.ask_who= npc_info.get('who')
        self.ask_where = npc_info.get('where')
        self.ask_what = npc_info.get('what')
        self.icon = npc_info.get('img')

        self.ques = npc_ques
        self.test = test
       
        self.status = 'idle'
        self.image = pygame.Surface((16,16))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites

        self.speech_shown = False  # Flag to track if speech is currently shown
        self.question = True  # ans will be false 
        self.skip= False
        

    def import_graphic(self, name):
        main_path = f'./sprites sheet for maps/sprites/characters/npc/{name}/'
        self.animations = {'idle':[]}
        for animation in self.animations.keys():
            full_main_path = main_path + animation
            self.animations[animation] = import_folder(full_main_path)
        print(self.animations[animation])
        #graphics setup 

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def draw(self):
            self.name_surface = FONT_NAME.render(self.npc_name, True, WHITE)
            self.name_rect = self.name_surface.get_rect(topleft = (self.dialogue.speech_rect.x + 30, self.dialogue.speech_rect.y - 20))
            self.display_surface.blit(self.name_surface, self.name_rect)

    def image_icon (self, screen, rect):
        self.icon_surface = pygame.image.load(self.icon).convert_alpha()
        # self.icon_enlarge = pygame.transform.scale(self.icon_surface, (45,51))
        self.icon_rect = self.icon_surface.get_rect(topleft = (self.dialogue.speech_rect.x , self.dialogue.speech_rect.y - 20))
        screen.blit(self.icon_surface, self.icon_rect)

    def dialogue_ques (self, screen, rect, font): 
        if self.question: 
            self.dialogue.render_instant_npc_speech(screen, self.ques, BLACK, rect, font)

    def multiple_choice (self, dialogue_where, dialogue_who, dialogue_what, screen, rect, font):   
        self.question = True
        for event in pygame.event.get():
            for name in npc_data: 
                if self.npc_name == name and event.type == pygame.KEYDOWN: 

                    if event.key == pygame.K_a: #ask where
                        self.dialogue.render_typewriter_npc_speech(screen, dialogue_where, BLACK, rect, font)
                        pygame.time.wait(1000)
                    elif event.key == pygame.K_b: #ask who 
                        self.dialogue.render_typewriter_npc_speech(screen, dialogue_who, BLACK, rect, font)
                        pygame.time.wait(1000)   

                    elif event.key == pygame.K_c: #ask what 
                        self.dialogue.render_typewriter_npc_speech(screen, dialogue_what, BLACK, rect, font)
                        pygame.time.wait(1000)    

                    if event.key == pygame.K_TAB: # escape dialogue 
                        self.question = False
                        pygame.time.wait(0) 

                    
                  
    def npc_collision (self, player):
        npc_index = None
        
        for i, npc in enumerate(npc_data): #i represented row of the list 
            if player.hitbox.colliderect (self.rect): 
                if not self.speech_shown:
                        print(NPC.interaction_counts)
                        self.speech_shown = True
                        self.question = True
                        self.skip = False
                        npc_index = i
                        NPC.interaction_counts[self.npc_name] += 1

                        if self.npc_name != "Officer":
                            if self.npc_name != "Professor":
                                #self.image_icon(self.display_surface, self.dialogue.speech_rect)
                                self.draw()  
                                n = 3
                                for i in range(n):
                                    self.dialogue_ques(self.display_surface, self.dialogue.speech_rect, SPEECH_FONT)
                                    self.multiple_choice(self.ask_where, self.ask_who, self.ask_what, self.display_surface, self.dialogue.speech_rect, SPEECH_FONT) 
                                    
                       
                       
                       
                        elif self.npc_name == 'Officer':
                            self.image_icon(self.display_surface, self.dialogue.speech_rect)
                            self.draw()      
                            if all(count > 0 for count in self.interaction_counts.values()):
                                self.execution.identify_killer(self.display_surface)

                            else:
                                self.dialogue.render_typewriter_npc_speech(self.display_surface, self.greeting, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                                pygame.time.wait(1000)  


                        if self.npc_name == 'Professor':
                            self.image_icon(self.display_surface, self.dialogue.speech_rect)
                            self.draw()
                            self.dialogue.render_typewriter_npc_speech(self.display_surface, self.greeting, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                            pygame.time.wait(1000) 
                            
            else:
                self.speech_shown = False  # Reset the flag when the player moves away

    def update(self):
        self.animate()

    def npc_update(self, player): 
        self.npc_collision(player)
