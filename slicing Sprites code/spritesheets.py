import pygame

class SpriteSheets():
    def __init__(self, image):
      self.sheet = image 

    def get_image(self, frame, width, height, scale, colour):
      image = pygame.Surface((width,height)).convert_alpha()
      if 0<= frame <= 5:
          image.blit(self.sheet, (0,0), ((frame*width),0, width, height))
      elif 6<= frame <= 11:
          image.blit(self.sheet, (0,0), ((frame*width),48, width, height))
      else: 
          image.blit(self.sheet, (0,0), ((frame*width),96, width, height))
      image = pygame.transform.scale(image, (width*scale, height*scale))
      image.set_colorkey(colour)

      return image