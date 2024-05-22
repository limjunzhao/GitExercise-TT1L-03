import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FONT = pygame.font.SysFont(None, 24)
SPEECH_FONT = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interacting with NPCs")

speech_text = ""
npc_index = None
hide_speech = False

class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.direction = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.rect.y += self.direction.y * speed

    def update(self):
        self.input()
        self.move(5)

class NPC:
    def __init__(self, name, position, speech):
        self.name = name
        self.position = position
        self.speech = speech
        self.image = pygame.image.load('sprites sheet for maps/sprites/characters/player_single.png').convert_alpha()
        self.rect = self.image.get_rect (topleft = position)
        self.interaction_count = 0

    def draw(self, surface):
        name_surface = FONT.render(self.name, True, WHITE)
        name_rect = name_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 20))
        surface.blit(self.image, self.rect)
        surface.blit(name_surface, name_rect)

class Dialogue:
    def __init__(self):
        self.speech_rect_width = SCREEN_WIDTH - 40
        self.speech_rect_height = SCREEN_HEIGHT // 4
        self.speech_rect = pygame.Rect(20, SCREEN_HEIGHT - self.speech_rect_height - 20, self.speech_rect_width, self.speech_rect_height)

    def draw_text(self, surface, text, color, rect, font):
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
            text_rect = text_surface.get_rect(topleft=(rect.left + 5, y))
            surface.blit(text_surface, text_rect)
            y += font.get_linesize()

    def render_typewriter_npc_speech(self, surface, text, color, rect, font):
        for i in range(len(text) + 1):
            pygame.draw.rect(surface, WHITE, rect, 0, 10)
            pygame.draw.rect(surface, BLACK, rect, 2, 10)
            self.draw_text(surface, text[:i], color, rect, font)
            pygame.display.flip()
            clock.tick(20)
        pygame.time.wait(1000)

    def render_typewriter_new_text(self, surface, text, color, rect, font):
        for i in range(len(text) + 1):
            pygame.draw.rect(surface, WHITE, rect, 0, 10)
            pygame.draw.rect(surface, BLACK, rect, 2, 10)
            self.draw_text(surface, text[:i], color, rect, font)
            pygame.display.flip()
            clock.tick(20)
        pygame.time.wait(3000)

class Execution:
    def __init__(self):
        self.dialogue = Dialogue()

    def identify_killer(self):
        new_text = "Who do you think is the killer?\nA. Maria\nB. Willie\nC. Amber\nD. Officer Marlowe"
        self.dialogue.render_typewriter_new_text(screen, new_text, BLACK, self.dialogue.speech_rect, SPEECH_FONT)

    def game_over(self):
        self.dialogue.render_typewriter_new_text(screen, "Incorrect! Game Over.", BLACK, self.dialogue.speech_rect, SPEECH_FONT)
        pygame.quit()
        sys.exit()

    def you_win(self):
        self.dialogue.render_typewriter_new_text(screen, "Congratulations! You've identified the killer!", BLACK, self.dialogue.speech_rect, SPEECH_FONT)
        pygame.quit()
        sys.exit()

player = Player()
npc_data = [
    {"name": "Maria", "position": (100, 100), "speech": "In the morning, I made breakfast for my husband..."},
    {"name": "Willie", "position": (600, 400), "speech": "Breakfast with my wife started the day..."},
    {"name": "Amber", "position": (600, 100), "speech": "In the day, I exercised in the park..."},
    {"name": "Officer Marlowe", "position": (100, 400), "speech": "Please help me find the killer before it's too late!"}
]
npcs = [NPC(npc["name"], npc["position"], npc["speech"]) for npc in npc_data]
interaction_counts = {npc["name"]: 0 for npc in npc_data}
dialogue = Dialogue()
execution = Execution()

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                execution.you_win()
            elif event.key in (pygame.K_b, pygame.K_c, pygame.K_d) and hide_speech:
                execution.game_over()

    player.update()

    for i, npc in enumerate(npcs):
        npc.draw(screen)
        if player.rect.colliderect(npc.rect):
            if not hide_speech:
                speech_text = npc.speech
                npc_index = i
                npc.interaction_count += 1
                interaction_counts[npc.name] += 1

                if npc.name != "Officer Marlowe":
                    dialogue.render_typewriter_npc_speech(screen, speech_text, BLACK, dialogue.speech_rect, SPEECH_FONT)
                else:
                    if all(count > 0 for count in interaction_counts.values()):
                        execution.identify_killer()
                    else:
                        dialogue.render_typewriter_npc_speech(screen, speech_text, BLACK, dialogue.speech_rect, SPEECH_FONT)

                hide_speech = True  

    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

    if npc_index is not None and not player.rect.colliderect(npcs[npc_index].rect):
        hide_speech = False