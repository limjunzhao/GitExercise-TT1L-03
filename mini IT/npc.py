import pygame, sys

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



class Player(): 
    def __init__(self):
      self.player_image = pygame.Surface((50, 50))
      self.player_image.fill(RED)
      self.rect = self.player_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
      self.direction = pygame.math.Vector2()


    def input(self): 

      keys = pygame.key.get_pressed()

      #control pos.y
      if keys [pygame.K_UP]:
        self.direction.y = -1
      elif keys [pygame.K_DOWN]:
        self.direction.y = 1
      else: 
        self.direction.y = 0

      #control pos.x 
      if keys [pygame.K_LEFT]:
        self.direction.x = -1
      elif keys [pygame.K_RIGHT]:
        self.direction.x = 1
      else:
        self.direction.x = 0

    def move(self, speed):
     
      if self.direction.magnitude() != 0: 
        self.direction = self.direction.normalize()
      
      self.rect.x += self.direction.x * speed 
      #collision check w 'horizontal'
      self.collision('horizontal') 
      self.rect.y += self.direction.y * speed
      self.collision('vertical')

    def update(self):
        self.input()
        self.move(5)
    

class NPC():
  def __init__(self):
     self.player = Player()
     self.dialogue = Dialogue()
     self.execution = Execution()
   
  def npc_info(self):
    npc_data = [
        {"name": "Maria", "position": (100, 100), "speech": "In the morning, I made breakfast for my husband...", "interaction_count": 0},
        {"name": "Willie", "position": (600, 400), "speech": "Breakfast with my wife started the day...", "interaction_count": 0},
        {"name": "Amber", "position": (600, 100), "speech": "In the day, I exercised in the park...", "interaction_count": 0},
        {"name": "Officer Marlowe", "position": (100, 400), "speech": "Please help me find the killer before it's too late!", "interaction_count": 0}
    ]
    

    for i, npc in enumerate(npc_data):
        npc_rect = pygame.Rect(npc["position"][0], npc["position"][1], 50, 50)
        pygame.draw.rect(screen, GREEN, npc_rect) 
        
        interaction_counts = {npc["name"]: npc["interaction_count"] for npc in npc_data}

        if self.player.player_rect.colliderect(self.npc_rect):
            if not hide_speech:
                speech_text = npc["speech"]
                npc_index = i
                interaction_counts[npc["name"]] += 1

                if not npc['name'] == 'Officer Marlowe':
                    self.dialogue.render_typewriter_npc_speech(screen, speech_text, BLACK, self.dialogue.speech_rect, SPEECH_FONT)

                else: #if collide w officer Marlowe 
                    if all(count > 0 for count in interaction_counts.values()) and npc["name"] == "Officer Marlowe":
                        self.execution.identify_killer()

                    else: 
                        self.dialogue.render_typewriter_npc_speech(screen, speech_text, BLACK, self.dialogue.speech_rect, SPEECH_FONT)
                hide_speech = True  

    npc_name_surface = FONT.render(npc["name"], True, WHITE)
    npc_name_rect = npc_name_surface.get_rect(center=(npc_rect.centerx + 2, npc_rect.bottom + 20))


    
    


class Dialogue():
  def __init__(self):
    self.speech_rect_width = SCREEN_WIDTH - 40
    self.speech_rect_height = SCREEN_HEIGHT // 4
    self.speech_rect = pygame.Rect(20, SCREEN_HEIGHT - self.speech_rect_height - 20, self.speech_rect_width, self.speech_rect_height)


  def draw_text(surface, text, color, rect, font):
    words = text.split(' ')
    lines = []
    line = ''

    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(topleft = (rect.left+5 , y))
        surface.blit(text_surface, text_rect)
        y += font.get_linesize()

    for word in words:
        test_line = line + word + ' '
        if font.size(test_line)[0] < rect.width:
            line = test_line
        else:
            lines.append(line)
            line = word + ' '
    lines.append(line)
    y = rect.top + 10

    


  def render_typewriter_npc_speech(surface, text, color, rect, font):
      for i in range(len(text) + 1):
          pygame.draw.rect(surface, WHITE, rect, 0, 10)
          pygame.draw.rect(surface, BLACK, rect, 2, 10)
          draw_text(surface, text[:i], BLACK, rect, font)
          pygame.display.flip()
          clock.tick(20)
      pygame.time.wait(1000)

  #officer marlowe 2nd msg
  def render_typewriter_new_text(surface, text, color, rect, font):
      for i in range(len(text) + 1):
          pygame.draw.rect(surface, WHITE, rect, 0, 10)
          pygame.draw.rect(surface, BLACK, rect, 2, 10)
          draw_text(surface, text[:i], BLACK, rect, font)
          pygame.display.flip()
          clock.tick(20)
      pygame.time.wait(3000)
  

class Execution():
  def __init__(self):
     self.dialogue = Dialogue

  def identify_killer():
      new_text = "Who do you think is the killer?\nA. Maria\nB. Willie\nC. Amber\nD. Officer Marlowe"
      self.dialogue.render_typewriter_new_text(screen, new_text, BLACK, speech_rect, SPEECH_FONT)

  def game_over():
      self.dialogue.render_typewriter_new_text(screen, "Incorrect! Game Over.", BLACK, speech_rect, SPEECH_FONT)
      pygame.quit()
      sys.exit()

  def you_win():
      self.dialogue.render_typewriter_new_text(screen, "Congratulations! You've identified the killer!", BLACK, speech_rect, SPEECH_FONT)
      pygame.quit()
      sys.exit()

npc = NPC()
player = Player()

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a :
                you_win()
            elif event.key in (pygame.K_b, pygame.K_c, pygame.K_d) and hide_speech:
                game_over()
        


    for i, npc in enumerate(npc.npc_info.npc_data):
      screen.blit (npc.npc_image, npc.npc_rect)
      screen.blit (npc.npc_name_surface, npc_name_rect)
      screen.blit(player.player_image, player.player_rect)


    pygame.display.flip()
    clock.tick(60) 

    if npc_index is not None and not player_rect.colliderect(pygame.Rect(npc_data[npc_index]["position"][0], npc_data[npc_index]["position"][1], 50, 50)):
        hide_speech = False