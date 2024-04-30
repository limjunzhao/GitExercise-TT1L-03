import pygame 
from settings import * 

class Tile(pygame.sprite.Sprite):
  def __init__(self, pos, groups):
     super().__init__(groups)
     self.image = pygame.image.load('MyGame/Background/grass.png').convert_alpha()
     self.scale_image = pygame.transform.scale(self.image, (64,64))
     self.rect = self.image.get_rect(topleft= pos)

