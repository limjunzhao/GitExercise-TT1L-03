import pygame , sys
from settings import *
from entity import Entity
from support import * 
from minigame import *
from button import Button
win_game_global = False

class Dialogue(): 
    def __init__(self):
        self.speech_rect_width = WIDTH - 40
        self.speech_rect_height = HEIGHT // 4
        self.speech_rect = pygame.Rect(20, HEIGHT - self.speech_rect_height - 20, self.speech_rect_width, self.speech_rect_height)


        self.line_status = False
        self.all_line_status = False
        self.skip = False


    def escape_dialogue_text_display (self, screen, text, rect, font, color): 
        skip_text = "[TAB] to escape the dialogue"

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
            pygame.time.wait(1000)
        
        

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
        self.display_surface = pygame.display.get_surface()
        self.dialogue = Dialogue()
        self.font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)

        self.button_sfx = pygame.mixer.Sound("images/music/new_button_sfx.mp3")

          # Congratulations message surface
        self.congratulations_surface = pygame.Surface((WIDTH, HEIGHT))
        self.congratulations_image = pygame.image.load('images/background/background.jpg')
        self.congratulations_image = pygame.transform.scale(self.congratulations_image, (WIDTH, HEIGHT))
        self.congratulations_surface.blit(self.congratulations_image, (0, 0))
        self.congratulations_text = self.font.render("Congratulations! You Win!", True, WHITE)
        self.congratulations_rect = self.congratulations_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Game over message surface
        self.game_over_surface = pygame.Surface((WIDTH, HEIGHT))
        self.game_over_image = pygame.image.load('images/background/background.jpg')
        self.game_over_image = pygame.transform.scale(self.game_over_image, (WIDTH, HEIGHT))
        self.game_over_surface.blit(self.game_over_image, (0, 0))
        self.game_over_text = self.font.render("Game Over! You Lose!", True, WHITE)
        self.game_over_rect = self.game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Play again button
        play_again_button_static = pygame.image.load('images/button/play_again.png')
        play_again_button_hover = pygame.image.load('images/button/play_again_hover.png')
        button_x = (WIDTH - play_again_button_static.get_width()) // 2 - 50
        self.game_over_button = Button(button_x, HEIGHT * 0.7, play_again_button_static, play_again_button_hover,(200, 100))

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

    def display_congratulations(self,screen):
        screen.blit(self.congratulations_surface, (0, 0))
        screen.blit(self.congratulations_text, self.congratulations_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()  

    def display_game_over(self,screen):
        while True:
            screen.blit(self.game_over_surface, (0, 0))
            screen.blit(self.game_over_text, self.game_over_rect)
            if self.game_over_button.draw(screen):
                self.button_sfx.play()
                return "play_again"
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    # Function to draw text on the screen
    def draw_text(self, surface, text, position, font, color=BLACK):
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, position)
        return text_surface.get_width()  # Return the width of the rendered text

    # Learning language screen
    def display_learning_screen(self):
        self.display_surface.fill(BLACK)  # Change background to black

        text_base = "Learning Language"
        text = text_base
        max_dots = 5
        clock = pygame.time.Clock()
        dot_count = 0
        running = True
        start_time = time.time()

        while running and time.time() - start_time < 5:  # Display for 5 seconds
            self.display_surface.fill(BLACK)  # Change background to black
            text = text_base + '.' * (dot_count % (max_dots + 1))
            text_width = self.draw_text(self.display_surface, text, ((WIDTH - font_large.size(text)[0]) // 2, HEIGHT // 2), font_large, WHITE)  # Change text to white
            pygame.display.flip()

            dot_count += 1
            clock.tick(2)  # Update every half second

        pygame.display.flip()

class Transition:
    def __init__ (self): 
        self.display_surface = pygame.display.get_surface()
        self.fade_surface = pygame.Surface((WIDTH, HEIGHT)).convert()
        self.fade_surface.fill(BLACK)
    
    def fade_out(self):
        for alpha in range(0, 256, 1):  
            self.fade_surface.set_alpha(alpha)
            self.display_surface.blit(self.fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(3)
        

    # Function to fade in
    def fade_in(self):
        for alpha in range(255, 0, -1):  # Alpha ranges from 255 (opaque) to 0 (transparent)
            self.fade_surface.set_alpha(alpha)
            self.display_surface.blit(self.fade_surface, (0, 0))
            pygame.display.update()

    # Function to fade in
    def fade_in(self):
        pass


class NPC(Entity):
    interaction_counts = {npc: 0 for npc in npc_data}


    def __init__(self, npc_name, pos, speech, groups, obstacle_sprites):
        # General setup
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.sprite_type = 'npc'
        self.import_graphic(npc_name)

        # Import Dialogue and Execution 
        self.dialogue = Dialogue()
        self.execution = Execution()
        self.transition = Transition()
        self.npc_speed = 0.1
        self.morsecode = Morsecode()
        self.jumbleword = Jumbleword()
        
        # Stats  
        self.npc_name = npc_name
        npc_info = npc_data[self.npc_name]
        self.greeting = npc_info.get('greeting')
        self.rawr = npc_info.get('rawr')
        self.ask_who = npc_info.get('who')
        self.ask_where = npc_info.get('where')
        self.ask_what = npc_info.get('what')
        self.icon = npc_info.get('img')
        self.ques = npc_ques
        self.congrats = prof_congrats
       

        self.detective_dialogue = detective_dialogue
        self.rejected_dialogue = rejected_dialogue

        self.status = 'idle'
        self.image = pygame.Surface((16,16))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        self.win_game = False #Check win morsecode minigame 
        self.speech_shown = False  # Flag to track if speech is currently shown
        self.question = True  # ans will be false 
        self.skip = False
        self.show_player = False
        self.show_npc = False
        
        self.font = pygame.font.Font(None, 36)  # Font for interaction message
        self.interaction_radius = 90  # Radius to show interaction message

    def import_graphic(self, name):
        main_path = f'./sprites sheet for maps/sprites/characters/npc/{name}/'
        self.animations = {'idle': []}
        for animation in self.animations.keys():
            full_main_path = main_path + animation
            self.animations[animation] = import_folder(full_main_path)
       
    def animate(self):
        animation = self.animations[self.status]
        # Loop over the frame index
        self.frame_index += self.npc_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        # Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def draw_npc_name_icon(self, screen, rect):

        self.name_surface = FONT_NAME.render(self.npc_name, True, WHITE)
        self.name_rect = self.name_surface.get_rect(topleft = (self.dialogue.speech_rect.x + 50, self.dialogue.speech_rect.y - 20))
        self.display_surface.blit(self.name_surface, self.name_rect)

        self.icon_surface = pygame.image.load(self.icon).convert_alpha()
        self.icon_surface = pygame.transform.scale2x(self.icon_surface)
        self.icon_rect = self.icon_surface.get_rect(topleft = (self.dialogue.speech_rect.x + 10  , self.dialogue.speech_rect.y - 40))
        screen.blit(self.icon_surface, self.icon_rect)

        


    def player_ask (self):
        self.draw_npc_name_icon(self.display_surface, self.dialogue.speech_rect)
        if self.stats == 'first meet':
            self.dialogue.render_typewriter_npc_speech(self.display_surface, self.detective_dialogue, BLACK, self.dialogue.speech_rect, SPEECH_FONT)



        elif self.stats == 'ask ques':
            self.dialogue.render_instant_npc_speech(self.display_surface, self.ques, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
            self.show_player = False


    def npc_ans(self):
        self.draw_npc_name_icon(self.display_surface, self.dialogue.speech_rect)
        self.multiple_choice(self.ask_where, self.ask_who, self.ask_what, self.display_surface, self.dialogue.speech_rect, SPEECH_FONT)


    def multiple_choice(self, dialogue_where, dialogue_who, dialogue_what, screen, rect, font):
        self.question = True
        for event in pygame.event.get():
            for name in npc_data:
                if self.npc_name == name and event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_a:  # Ask where
                        self.dialogue.render_typewriter_npc_speech(screen, dialogue_where, BLACK, rect, font)
                    elif event.key == pygame.K_b:  # Ask who
                        self.dialogue.render_typewriter_npc_speech(screen, dialogue_who, BLACK, rect, font)
                    elif event.key == pygame.K_c:  # Ask what
                        self.dialogue.render_typewriter_npc_speech(screen, dialogue_what, BLACK, rect, font)
                        if self.npc_name == 'Alex': 
                            self.question = False
                            self.transition.fade_out()
                            self.jumbleword.run()
                           
                    if event.key == pygame.K_TAB:  # Escape dialogue
                        self.question = False

    def wait_for_player_response(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        return 'A'
                    elif event.key == pygame.K_b:
                        return 'B'
            pygame.time.wait(100)  # Check input every 100 ms

    def ask_professor_questions(self):
        global win_game_global
        questions = [
            ("Hello there dear treveller, would you likde to learn our language?", ["A: Yes!    B: No.."]),
        ]

        for question, choices in questions:
            self.dialogue.render_typewriter_npc_speech(self.display_surface, question, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
            pygame.time.wait(500)  # Brief pause before showing choices
            
            for choice in choices:
                self.dialogue.render_typewriter_npc_speech(self.display_surface, choice, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                pygame.time.wait(500)  # Brief pause for readability

            # Wait for the player's response
            response = self.wait_for_player_response()

            # Handle the response
            if response == 'A':

                self.question = False
                self.transition.fade_out()
                self.execution.display_learning_screen()
                self.transition.fade_in()
                if self.morsecode.run() == 'Complete test':
                    win_game_global = True
                  
                    return
                self.dialogue.render_instant_npc_speech(self.display_surface, self.congrats, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                
            elif response == 'B':
                self.dialogue.render_instant_npc_speech(self.display_surface, self.reject, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                
                self.question = False
                

            pygame.time.wait(1000)  # Pause to let player read the response

    def display_interaction_message(self,screen):
        font = pygame.font.Font(None, 26)
        interact = [{"text": "PRESS 'E' TO INTERACT", "color": BLACK, "position": (10, 690)}]
        for press in interact:
            text_surface = font.render(press["text"], True, press["color"])
            screen.blit(text_surface, press["position"])

    def npc_collision(self, player):
        global win_game_global
        npc_index = None
        for i, npc in enumerate(npc_data):
            if player.hitbox.colliderect(self.rect):
                keys = pygame.key.get_pressed()
                distance = ((player.hitbox.centerx - self.rect.centerx) ** 2 + (player.hitbox.centery - self.rect.centery) ** 2) ** 0.5
                if distance < self.interaction_radius:
                    self.display_interaction_message(self.display_surface)
                    if keys[pygame.K_e] and not self.speech_shown:
                        self.speech_shown = True
                        self.question = True
                        self.show_player = True 
                        self.show_npc = False
                        self.skip = False
                        npc_index = i
                        NPC.interaction_counts[self.npc_name] += 1
                       

                        if win_game_global:
                            if self.npc_name == "Professor":
                                self.draw_npc_name_icon(self.display_surface, self.dialogue.speech_rect)
                                self.dialogue.render_instant_npc_speech(self.display_surface, self.congrats, BLACK, self.dialogue.speech_rect, SPEECH_FONT)


                            elif self.npc_name != "Officer":
                                #display player dialogue to ask question 
                                self.stats = 'first meet' 
                                self.player_ask()
                               
                                
                                for _ in range(3):
                                    if self.question: 
                                        self.stats = 'ask ques'
                                        self.player_ask()
                                        self.npc_ans()


                            elif self.npc_name == 'Officer':
                               
                                self.draw_npc_name_icon(self.display_surface, self.dialogue.speech_rect)
                                if all(count > 0 for count in self.interaction_counts.values()):
                                    self.execution.identify_killer(self.display_surface)
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if all(count > 0 for count in NPC.interaction_counts.values()):
                                                if event.key == pygame.K_a:
                                                    self.execution.display_congratulations(self.display_surface)
                                                elif event.key in (pygame.K_b, pygame.K_c, pygame.K_d):
                                                    self.execution.display_game_over(self.display_surface)
                                else:
                                    self.dialogue.render_typewriter_npc_speech(self.display_surface, self.greeting, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                                    pygame.time.wait(1000)  

                                

                        else:
                            if self.npc_name == "Professor":
                                self.draw_npc_name_icon(self.display_surface, self.dialogue.speech_rect)
                                self.ask_professor_questions()

                            else:
                                self.dialogue.render_typewriter_npc_speech(self.display_surface, self.rawr, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                                pygame.time.wait(1000)
            else:
                self.speech_shown = False  # Reset the flag when the player moves awaye

    def update(self):
        self.animate()

    def npc_update(self, player):
        self.npc_collision(player)