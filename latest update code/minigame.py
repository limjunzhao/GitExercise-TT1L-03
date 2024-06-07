import pygame 
from settings import * 
import random
import time 
from entity import Entity

class Jumbleword(Entity):
    def __init__ (self, pos, groups, obstacle_sprites): 
        super().__init__(groups)
      #display 
        pygame.init()
        self.display_surface = pygame.display.get_surface()
        

        #general setup
        self.sprite_type = 'loveletter'
        self.image = pygame.image.load('sprites sheet for maps/Terrains/12.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.obstacle_sprites = obstacle_sprites

        self.word = random.choice(list(word_hints.keys()))
        self.jumbled_word = ''.join(random.sample(self.word, len(self.word)))
        self.score = 0
        self.input_text = ""
        self.show_initial_screen = True
        self.show_love_letter = False  # Flag to control when to show the love letter
        self.hint_active = False
        self.hint_start_time = 0
        
        self.background_image = pygame.image.load('images/loveletter/pixel.png').convert()
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Load love letter image
        self.love_letter_image = pygame.image.load('images/loveletter/love_letter_image.png').convert_alpha()
        self.love_letter_image = pygame.transform.scale(self.love_letter_image, (WIDTH, HEIGHT))
        self.love_letter_image_rect = self.love_letter_image.get_rect(center=  (WIDTH // 2, HEIGHT // 2))


    
    # Functions
    def display_word(self):
        self.text_surface = font.render(self.jumbled_word, True, WHITE)
        self.text_rect = self.text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.display_surface.blit(self.text_surface, self.text_rect)

    def display_score(self):
        self.score_surface = score_font.render("Score: " + str(self.score), True, WHITE)
        self.score_rect = self.score_surface.get_rect(topright=(WIDTH - 20, 20))
        self.display_surface.blit(self.score_surface, self.score_rect)

    def display_instructions(self):
        self.instruction_surface = instruction_font.render("Type the correct word and press Enter to submit", True, WHITE)
        self.instruction_rect = self.instruction_surface.get_rect(midtop=(WIDTH / 2, 200))  # Adjusted position
        box_height = 300  # Height of the semi-transparent box
        self.instruction_rect.y = 30 + (box_height - self.instruction_surface.get_height()) // 2  # Position significantly higher in the box
        self.display_surface.blit(self.instruction_surface, self.instruction_rect)
        
        self.hint_instruction_surface = instruction_font.render("Press Tab for hint", True, WHITE)
        self.hint_instruction_rect = self.hint_instruction_surface.get_rect(midtop=(WIDTH / 2, 250))  # Adjusted position
        self.display_surface.blit(self.hint_instruction_surface, self.hint_instruction_rect)

    def new_word(self):
        # global self.word, jumbled_word
        self.word = random.choice(list(word_hints.keys()))
        self.jumbled_word = ''.join(random.sample(self.word, len(self.word)))

    def check_answer(self, answer):
        # global score
        if answer.upper() == self.word:
            if self.score < 5:
                self.score += 1
            self.new_word()
            return True
        return False

    def display_initial_screen(self):
        self.display_surface.blit(self.background_image, (0, 0))
        self.initial_text1 = instruction_font.render("Press Enter to start the game", True, WHITE)
        self.initial_text_rect1 = self.initial_text1.get_rect(center=(WIDTH / 2, HEIGHT - 100))
        self.display_surface.blit(self.initial_text1, self.initial_text_rect1)
        
        self.initial_text2 = instruction_font.render("Welcome to the Love Letter Minigame!", True, WHITE)
        self.initial_text_rect2 = self.initial_text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))  # Adjusted position
        self.display_surface.blit(self.initial_text2, self.initial_text_rect2)

        pygame.display.update()

    def display_instructions_screen(self):
        self.display_surface.blit(self.background_image, (0, 0))
        self.instructions_header = instruction_font.render("Instructions:", True, WHITE)
        self.instructions_header_rect = self.instructions_header.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 80))
        self.display_surface.blit(self.instructions_header, self.instructions_header_rect)

        instruction_text = [
            "1. This is a jumbled-word minigame.",
            "2. Answers can be found in the storyline.",
            "3. New words will not display until you get it correctly."
        ]
        for i, text in enumerate(instruction_text):
            self.instruction_surface = instruction_font.render(text, True, WHITE)
            self.instruction_rect = self.instruction_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 40 + (i * 30)))  # Adjusted position
            self.display_surface.blit(self.instruction_surface, self.instruction_rect)
        
        self.start_game_text = instruction_font.render("Press Enter to start the game", True, WHITE)
        self.start_game_rect = self.start_game_text.get_rect(center=(WIDTH / 2, HEIGHT - 100))
        self.display_surface.blit(self.start_game_text, self.start_game_rect)

        pygame.display.update()

    def display_hint(self):
        self.hint_text = word_hints[self.word]
        self.hint_surface = instruction_font.render(self.hint_text, True, WHITE)
        self.hint_rect = self.hint_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 120))
        self.display_surface.blit(self.hint_surface, self.hint_rect)

    
    def running (self): 
        running = True
        self.show_initial_screen = True
        self.show_love_letter = False
        self.hint_active = False

        while running:  
            
            if self.show_initial_screen:
                self.display_initial_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        # return True

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.show_initial_screen = False
                            self.show_instructions_screen = True

            elif self.show_instructions_screen:
                self.display_instructions_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       running = False
                    #    return True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.show_instructions_screen = False
                            
            else:
                self.display_surface.blit(self.background_image, (0, 0))

                # Check for events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        # return True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            # return True
                        elif event.key == pygame.K_RETURN:
                            if self.check_answer(self.input_text):
                                self.input_text = ""
                                
                                # Check if the score reaches 5 to show the love letter
                                if self.score == 5:
                                    self.show_love_letter = True

                        elif event.key == pygame.K_BACKSPACE:
                            # Handle backspace to delete characters from input_text
                            self.input_text = self.input_text[:-1]
                        elif event.key in (pygame.K_SPACE, pygame.K_MINUS):
                            # Handle space and minus key for multi-word inputs
                            self.input_text += " "
                        elif event.key in range(pygame.K_a, pygame.K_z + 1):
                            # Handle typing letters
                            self.input_text += event.unicode
                        elif event.key == pygame.K_TAB:
                            # Activate hint
                            self.hint_active = True
                            self.hint_start_time = time.time()

                # Draw a semi-transparent box
                self.overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                self.rect = pygame.draw.rect(self.overlay, SEMI_TRANSPARENT_BLACK, (50, 150, WIDTH - 100, 300), border_radius=10)
                self.display_surface.blit(self.overlay, (0, 0))

                self.display_instructions()
                self.display_word()
                self.display_score()

                # Render input text in white
                self.input_surface = font.render(self.input_text, True, WHITE)
                self.input_rect = self.input_surface.get_rect(midtop=(WIDTH / 2, HEIGHT / 2 + 60))
                self.display_surface.blit(self.input_surface, self.input_rect)

                # Draw line under input text
                pygame.draw.line(self.display_surface, WHITE, (self.input_rect.left, self.input_rect.bottom + 10), (self.input_rect.right, self.input_rect.bottom + 10), 2)

                # Display hint if active
                if self.hint_active:
                    self.display_hint()
                    if time.time() - self.hint_start_time > 3:
                        self.hint_active = False

                # Display love letter only when score is 5
                if self.show_love_letter:
                    self.display_surface.blit(self.love_letter_image, self.love_letter_image_rect)
                    for message in messages:
                        self.text_surface = love_letter_font.render(message["text"], True, message["color"])
                        self.display_surface.blit(self.text_surface, message["position"])

                pygame.display.flip()



    def loveletter_collision(self, player): 
      if player.hitbox.colliderect (self.rect): 
        self.running()

        # return True
          


    def loveletter_update(self, player): 
        self.loveletter_collision(player)

    