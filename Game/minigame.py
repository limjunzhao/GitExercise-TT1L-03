import pygame, sys
from settings import * 
import random
import time 


class Jumbleword:
    def __init__(self):
        # Display
        self.display_surface = pygame.display.get_surface()

        # General setup
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
        self.love_letter_image_rect = self.love_letter_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

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
        self.instruction_rect = self.instruction_surface.get_rect(midtop=(WIDTH / 2, 200))
        box_height = 300  # Height of the semi-transparent box
        self.instruction_rect.y = 30 + (box_height - self.instruction_surface.get_height()) // 2
        self.display_surface.blit(self.instruction_surface, self.instruction_rect)

        self.hint_instruction_surface = instruction_font.render("Press Tab for hint", True, WHITE)
        self.hint_instruction_rect = self.hint_instruction_surface.get_rect(midtop=(WIDTH / 2, 250))
        self.display_surface.blit(self.hint_instruction_surface, self.hint_instruction_rect)

    def new_word(self):
        self.word = random.choice(list(word_hints.keys()))
        self.jumbled_word = ''.join(random.sample(self.word, len(self.word)))

    def check_answer(self, answer):
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
        self.initial_text_rect2 = self.initial_text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
        self.display_surface.blit(self.initial_text2, self.initial_text_rect2)

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
            self.instruction_rect = self.instruction_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 40 + (i * 30)))
            self.display_surface.blit(self.instruction_surface, self.instruction_rect)

        self.start_game_text = instruction_font.render("Press Enter to start the game", True, WHITE)
        self.start_game_rect = self.start_game_text.get_rect(center=(WIDTH / 2, HEIGHT - 100))
        self.display_surface.blit(self.start_game_text, self.start_game_rect)

    def display_hint(self):
        self.hint_text = word_hints[self.word]
        self.hint_surface = instruction_font.render(self.hint_text, True, WHITE)
        self.hint_rect = self.hint_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 120))
        self.display_surface.blit(self.hint_surface, self.hint_rect)

    def run (self): 
        running = True
        self.show_initial_screen = True
        self.show_love_letter = False
        self.hint_active = False

        while running:  
            
            if self.show_initial_screen:
                self.display_initial_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.show_initial_screen = False
                            self.show_instructions_screen = True

            elif self.show_instructions_screen:
                self.display_instructions_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.show_instructions_screen = False
                            
            else:
                self.display_surface.blit(self.background_image, (0, 0))

                # Check for events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return

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
                self.rect = pygame.draw.rect(self.overlay, SEMI_TRANSPARENT_BLACK, (50, 150, WIDTH - 100, 300), border_radius = 10)
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





class Morsecode:
    def __init__ (self): 
      self.display_surface = pygame.display.get_surface()

      # Load the start screen image and scale it to fill the window
      self.start_screen_image = pygame.image.load('images/morsecode_minigame/library.jpeg')
      self.start_screen_image = pygame.transform.scale(self.start_screen_image, (WIDTH, HEIGHT))

      # Game variables
      # Define cursor position variables
      self.cursor_x = NOTES_WIDTH + 20
      self.cursor_y = 220

      # Constants for cursor boundaries
      self.CURSOR_MIN_X = NOTES_WIDTH + 20
      self.CURSOR_MAX_X = NOTES_WIDTH + 260  # Adjust this value to set the maximum x-coordinate

      self.question = ms_questions
      random.shuffle(self.question)
      self.current_question_index = 0
      self.current_question, self.answer = self.question[self.current_question_index]
      self.current_input = ''
      self.correct = None

      self.win_game = False 
    # Function to draw text on the screen
    def draw_text(self, surface, text, position, font, color = BLACK):
        self.text_surface = font_game.render(text, True, color)
        self.display_surface.blit(self.text_surface, position)
        return self.text_surface.get_width()  # Return the width of the rendered text

    # Display instructions to start the game
    def display_start_screen(self):
        waiting_for_start = True
        while waiting_for_start:
            self.display_surface.fill(WHITE)

            # Blit the start screen image
            self.display_surface.blit(self.start_screen_image, (0, 0))

            # Draw the start message in white
            self.draw_text(self.display_surface, 'Press Enter to start the game', (WIDTH // 2 - 110, HEIGHT // 2 + 100), font_game, WHITE)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting_for_start = False
                        return

    # Display instructions screen
    def display_instructions_screen(self):
      waiting_for_instructions = True
      while waiting_for_instructions:
          self.display_surface.fill(WHITE)

          # Blit the start screen image
          self.display_surface.blit(self.start_screen_image, (0, 0))

          # Draw the instructions header
          header = "Instructions:"
          self.draw_text(self.display_surface, header, (WIDTH // 2 - 180, HEIGHT // 2 - 120), font_game, WHITE)

          # Draw semi-transparent black background
          instructions_background_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 100, 400, 240)
          pygame.draw.rect(self.display_surface, (0, 0, 0, 150), instructions_background_rect)

          instructions = [
              "1. Complete this minigame to graduate",
              "2. It's a Morse code-based game",
              "3. Fill up the words with Morse codes"
          ]
          y_offset = HEIGHT // 2 - 80
          for instruction in instructions:
              self.draw_text(self.display_surface, instruction, (WIDTH // 2 - 180, y_offset), font_game, WHITE)
              y_offset += FONT_SIZE_GAME + 10

          # Draw the start message in white
          self.draw_text(self.display_surface, 'Press Enter to continue', (WIDTH // 2 - 100, HEIGHT // 2 + 100), font_game, WHITE)

          pygame.display.flip()

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RETURN:
                      waiting_for_instructions = False
                      return

    def display_note_in_game(self): 
        self.display_surface.fill(WHITE)

        # Draw Morse code notes on the left side with semi-transparent background
        self.notes_rect = pygame.Rect(10, 10, NOTES_WIDTH + 5, HEIGHT - 20)
        pygame.draw.rect(self.display_surface, (200, 200, 200, 150), self.notes_rect)  # Semi-transparent gray background

        y_offset = 20
        x_offset = 20
        self.draw_text(self.display_surface, 'Morse Code Notes:', (x_offset, y_offset), font_game)
        y_offset = FONT_SIZE_GAME + 10
        for letter, morse in MORSE_CODE_DICT.items():
            x_offset = 20
            if letter > 'W':
                x_offset += X_OFFSET_RIGHT

            self.draw_text(self.display_surface, f'{letter}: {morse}', (x_offset, y_offset + 10), font_game)
            y_offset += FONT_SIZE_GAME + 5

            if y_offset > HEIGHT - FONT_SIZE_GAME:
                y_offset = 30

            
        
    def run (self):
        # Display start screen
        self.display_start_screen()

        # Display instructions screen
        self.display_instructions_screen()

        running = True
        while running:
            self.display_note_in_game()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(self.current_input) > 0:
                            self.char_width = font_game.render(self.current_input[-1], True, BLACK).get_width()
                            self.current_input = self.current_input[:-1]
                            self.cursor_x -= self.char_width
                        if self.cursor_x < self.CURSOR_MIN_X:
                            self.cursor_x = self.CURSOR_MIN_X

                    elif event.key == pygame.K_RETURN:
                        self.correct = (self.current_input.strip() == self.answer)
                        if self.correct:
                            # Move to the next question
                            self.current_question_index += 1
                            

                            if self.current_question_index < len(self.question):
                                self.current_question, self.answer = self.question[self.current_question_index]
                                self.current_input = ''
                            else:
                                # If all questions are answered, end the game
                                pygame.time.wait(1000)
                                running = False
                                return 'Complete test'
                                
                        else:
                            self.current_input = ''  # Clear input box on incorrect answer
                        # Reset cursor position
                        self.cursor_x = self.CURSOR_MIN_X

                    elif event.key == pygame.K_ESCAPE:
                        # Quit the game if Escape key is pressed
                        running = False
                        return 

                    else:
                        self.current_input += event.unicode.upper()
                        self.char_width = font_game.render(event.unicode.upper(), True, BLACK).get_width()
                        self.cursor_x += self.char_width
                        if self.cursor_x > self.CURSOR_MAX_X:
                            self.cursor_x = self.CURSOR_MAX_X

            # Draw question on the right side
            self.draw_text(self.display_surface, 'Question:', (NOTES_WIDTH + 20, 20), font_game)
            self.draw_text(self.display_surface, self.current_question, (NOTES_WIDTH + 20, 20 + FONT_SIZE + 5), font_game)
            self.draw_text(self.display_surface, '* make sure to enter space', (NOTES_WIDTH + 20, 20 + FONT_SIZE_GAME + 5 + 30), font_game)

            # Draw user input
            self.draw_text(self.display_surface, 'Your Input:', (NOTES_WIDTH + 20, 200), font_game)

            # Draw line under your input
            pygame.draw.line(self.display_surface, BLACK, (NOTES_WIDTH + 15, 260), (NOTES_WIDTH + 265, 260), 2)
            self.draw_text(self.display_surface, self.current_input, (NOTES_WIDTH + 20, 200 + FONT_SIZE_GAME + 5), font_game)
            
            # Draw cursor
            pygame.draw.line(self.display_surface, BLACK, (self.cursor_x, self.cursor_y), (self.cursor_x, self.cursor_y + FONT_SIZE_GAME), 2)

            # Display correctness
            if self.correct is not None:
                if self.correct:
                    self.draw_text(self.display_surface, 'Correct!', (NOTES_WIDTH + 20, 300), font_game, GREEN)
                    
                else:
                    self.draw_text(self.display_surface, 'Incorrect, try again.', (NOTES_WIDTH + 20, 300), font_game, RED)

            # Update display
            pygame.display.flip()

