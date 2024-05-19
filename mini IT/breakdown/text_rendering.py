import pygame

def draw_text(surface, text, color, rect, font):
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
        text_rect = text_surface.get_rect()
        text_rect.topleft = (rect.left + 5, y)
        surface.blit(text_surface, text_rect)
        y += font.get_linesize()

def render_typewriter_npc_speech(surface, text, color, rect, font):
    for i in range(len(text) + 1):
        pygame.draw.rect(surface, (255, 255, 255), rect, 0, 10)
        pygame.draw.rect(surface, (0, 0, 0), rect, 2, 10)
        draw_text(surface, text[:i], (0, 0, 0), rect, font)
        pygame.display.flip()
        pygame.time.wait(20)

def render_typewriter_new_text(surface, text, color, rect, font):
    for i in range(len(text) + 1):
        pygame.draw.rect(surface, (255, 255, 255), rect, 0, 10)
        pygame.draw.rect(surface, (0, 0, 0), rect, 2, 10)
        draw_text(surface, text[:i], (0, 0, 0), rect, font)
        pygame.display.flip()
        pygame.time.wait(20)
    pygame.time.wait(3000)
