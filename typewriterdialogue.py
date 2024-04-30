import pygame
import sys

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Typewriter Text")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.SysFont(None, 24)


typewriter_texts = [
    "This is the first typewriter text example. Press Enter to continue.",
    "This is the second typewriter text example. Press Enter to continue.",
    "This is the third typewriter text example. Press Enter to continue.",
    "This is the fourth typewriter text example. Press Enter to continue.",
]
text_rect = pygame.Rect(20, screen_height - 100, screen_width - 40, 80)


def render_typewriter_text(surface, text, font, color, rect, current_char):
    
    rendered_text = font.render(text[:current_char], True, color)
    surface.blit(rendered_text, (rect.x, rect.y))


clock = pygame.time.Clock()
current_text_index = 0
current_char_index = 0
typing_speed = 5  # Adjust typing speed 
text_completed = False

while True:
    screen.fill(BLACK) 

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                
                if current_char_index >= len(typewriter_texts[current_text_index]):
                   
                    current_text_index = (current_text_index + 1) % len(typewriter_texts)
                    current_char_index = 0
                    text_completed = False

   
    if not text_completed:
        render_typewriter_text(screen, typewriter_texts[current_text_index], font, WHITE, text_rect, current_char_index)
        
        if current_char_index < len(typewriter_texts[current_text_index]):
            current_char_index += 1
        else:
            text_completed = True

    pygame.display.flip()
    clock.tick(20)  # Adjust typing speed
