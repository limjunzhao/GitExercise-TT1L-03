import pygame

pygame.init()
enter = "click enter"
font = pygame.font.Font('freesansbold.ttf', 35)
screen = pygame.display.set_mode([1280, 720])
timer = pygame.time.Clock()
messages = [
    " In the fog-drenched streets of Arcadia,",
    " a series of grisly murders shatters ",
    "the tranquility of its residents.",
    "It's 7am in the morning and you discovered",
    " the victim's body laying (outside a house/bar)",
    " and the blood was still damp, which means",
    " the killing happened not long ago.",
    "You, as a seasoned detective, are tasked with",
    " unraveling the mystery behind these brutal killings. ",
    " Come on detective, let's not waste any time",
    " find the murderer before it's too late!"
]

snip = font.render('', True, 'white')
counter = 0
speed = 1
active_message = 0
current_line = 0
done = False

def render_message(message_lines, counter, current_line):
    rendered_lines = []
    for i, line in enumerate(message_lines):
        if i < current_line:
            rendered_lines.append(line)
        elif i == current_line:
            rendered_lines.append(line[:counter])
    return '\n'.join(rendered_lines)

run = True
while run:
    screen.fill('grey')
    timer.tick(60)

    message_lines = messages[active_message].split('\n')

    if counter < speed * len(message_lines[current_line]):
        counter += 1
    elif counter >= speed * len(message_lines[current_line]):
        if current_line < len(message_lines) - 1:
            current_line += 1
            counter = 0
        else:
            done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                active_message += 1
                current_line = 0
                counter = 0
                done = False

    rendered_message = render_message(message_lines, counter // speed, current_line)
    snip = font.render(rendered_message, True, (0,0,0))
    screen.blit(snip, (300, 310))
    

    pygame.display.flip()

pygame.quit()
