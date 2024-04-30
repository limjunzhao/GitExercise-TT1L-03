import pygame 
from player import Player 



# class CameraGroup (pygame.sprite.Group):
#   def __init__ (self): 
#     super().__init__()
#     self.display_surface = pygame.display.get_surface()
#     self.half_w =  self.display_surface.get_size()[0] //2
#     self.half_h =  self.display_surface.get_size()[1] //2
#     self.offset = pygame.math.Vector2()

#   def custom_draw(self, player): 
#     self.offset.x = player.rect.centerx - self.half_w
#     self.offset.y = player.rect.centery - self.half_w

#     for sprite in self.sprites(): 
#       offset_pos = sprite.rect.topleft - self.offset 
#       self.display_surface.blit (sprite_image, offset_pos)

