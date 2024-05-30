import pygame
import sys
from text_rendering import render_typewriter_new_text

def identify_killer(screen, speech_rect, SPEECH_FONT):
    new_text = "Who do you think is the killer?\nA. Maria\nB. Willie\nC. Amber\nD. Officer Marlowe"
    render_typewriter_new_text(screen, new_text, (0, 0, 0), speech_rect, SPEECH_FONT)

def game_over(screen, speech_rect, SPEECH_FONT):
    render_typewriter_new_text(screen, "Incorrect! Game Over.", (0, 0, 0), speech_rect, SPEECH_FONT)
    pygame.quit()
    sys.exit()

def you_win(screen, speech_rect, SPEECH_FONT):
    render_typewriter_new_text(screen, "Congratulations! You've identified the killer!", (0, 0, 0), speech_rect, SPEECH_FONT)
    pygame.quit()
    sys.exit()
