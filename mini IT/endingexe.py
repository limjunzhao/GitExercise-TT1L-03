import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 24)
speech_font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

player_image = pygame.Surface((50, 50))
player_image.fill((255, 0, 0))
player_rect = player_image.get_rect(center=(screen_width // 2, screen_height // 2))

npc_data = [
    {"name": "Maria", "position": (100, 100), "speech": "In the morning, I made breakfast for my husband, then proceeded to do house chores until afternoon. After lunch with my husband, I engaged in a pleasant chit-chat with our neighbor, Amber. Later, I eagerly awaited my husband’s return from work, and once he was back, we cooked dinner together and went to sleep afterwards.", "interaction_count": 0},
    {"name": "Willie", "position": (600, 400), "speech": "Breakfast with my wife started the day, followed by me heading to work. Proceeds to head to lunch with my wife and returned to work. Finally, I came back home and got the ingredients ready and cooked dinner with my wife. Lastly, we went to bed before 10pm.", "interaction_count": 0},
    {"name": "Amber", "position": (600, 100), "speech": "In the day, I exercised in the park. And after that I had my coffee and breakfast. Meanwhile I watched TV for the time to pass. During lunch, I ate my leftover dinner from yesterday as my lunch. After lunch, me and Maria had our usual chit-chat but it was shorter than usual. And we were supposed to get groceries after that. So I went to buy the groceries myself and made dinner. As night falls, I took my dog for a night walk and went to bed.", "interaction_count": 0},
    {"name": "Officer Marlowe", "position": (100, 400), "speech": "Please help me find the killer before it's too late!", "interaction_count": 0}
]

speech_rect_width = screen_width - 40
speech_rect_height = screen_height // 4
speech_rect = pygame.Rect(20, screen_height - speech_rect_height - 20, speech_rect_width, speech_rect_height)

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
        pygame.draw.rect(surface, WHITE, rect, 0, 10)
        pygame.draw.rect(surface, BLACK, rect, 2, 10)
        draw_text(surface, text[:i], BLACK, rect, font)
        pygame.display.flip()
        clock.tick(20)
    pygame.time.wait(1000)

def display_new_text(surface, text, color, rect, font):
    pygame.draw.rect(surface, WHITE, rect, 0, 10)
    pygame.draw.rect(surface, BLACK, rect, 2, 10)
    draw_text(surface, text, BLACK, rect, font)
    pygame.display.flip()
    pygame.time.wait(3000)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interacting with NPCs")

speech_text = "" 
npc_index = None  
hide_speech = False  
interaction_counts = {npc["name"]: npc["interaction_count"] for npc in npc_data}

while True:
    screen.fill(BLACK) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and hide_speech:
                hide_speech = False
            elif event.key in (pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d) and hide_speech:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    screen.blit(player_image, player_rect)

    for i, npc in enumerate(npc_data):
        npc_rect = pygame.Rect(npc["position"][0], npc["position"][1], 50, 50)
        pygame.draw.rect(screen, (0, 255, 0), npc_rect)  

        if player_rect.colliderect(npc_rect):
            if not hide_speech:
                speech_text = npc["speech"]
                npc_index = i
                
                render_typewriter_npc_speech(screen, speech_text, BLACK, speech_rect, speech_font)
                hide_speech = True  

                interaction_counts[npc["name"]] += 1

                if all(count > 0 for count in interaction_counts.values()) and npc["name"] == "Officer Marlowe":
                    new_text = "Who do you think is the killer?\nA. Maria\nB. Willie\nC. Amber\nD. Officer"
                    display_new_text(screen, new_text, BLACK, speech_rect, speech_font)

        npc_name_surface = font.render(npc["name"], True, WHITE)
        npc_name_rect = npc_name_surface.get_rect(center=(npc_rect.centerx + 2, npc_rect.bottom + 20))
        screen.blit(npc_name_surface, npc_name_rect)

    pygame.display.flip()
    clock.tick(60) 

    if npc_index is not None and not player_rect.colliderect(pygame.Rect(npc_data[npc_index]["position"][0], npc_data[npc_index]["position"][1], 50, 50)):
        hide_speech = False
