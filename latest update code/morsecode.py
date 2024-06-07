import pygame
import sys
import random
from settings import *



class Morsecode:
    def __init__ (self): 
      self.display_surface = pygame.display.get_surface()
      self.sprite_type = 'morsecode'



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

            
        
    def running(self):
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
                              pygame.time.wait(2000)
                              running = False

                              return
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

      # Quit Pygame
      pygame.quit()
      sys.exit()

