import pygame 
from support import *

class CameraGroup (pygame.sprite.Group):
  def __init__ (self): 
    super().__init__()
    self.display_surface = pygame.display.get_surface()


    #camera offset
    self.half_w =  self.display_surface.get_size()[0] //2
    self.half_h =  self.display_surface.get_size()[1] //2
    self.offset = pygame.math.Vector2()

    #creating the floor 
    self.floor_surf = pygame.image.load('Data/tmx/maps2.0.png')
    self.floor_rect = self.floor_surf.get_rect (topleft = (0,0))

    #zoom 
    self.zoom_scale = 2.0
    self.internal_surf_size = (1200, 1200)
    self.internal_surf = pygame.Surface (self.internal_surf_size, pygame.SRCALPHA)
    self.internal_rect = self.internal_surf.get_rect (center = (self.half_w, self.half_h))
    self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
    self.internal_offset = pygame.math.Vector2()
    self.internal_offset.x = self.internal_surf_size[0] //2 - self.half_w
    self.internal_offset.y = self.internal_surf_size[1] //2 - self.half_h

  def center_target_camera(self, player): 
    self.offset.x = player.rect.centerx - self.half_w
    self.offset.y = player.rect.centery - self.half_h

  def zoom_keyboard_control(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
      self.zoom_scale += 0.05
    if keys[pygame.K_e]:
      self.zoom_scale -= 0.05

  def custom_draw(self, player): 

    self.center_target_camera(player)
    #self.zoom_keyboard_control()
    self.internal_surf.fill('#2D99E2')


    #drawing floor 
    floor_offset_pos = self.floor_rect.topleft - self.offset + self.internal_offset
    self.internal_surf.blit (self.floor_surf, floor_offset_pos)


    for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): 
      offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
      self.internal_surf.blit (sprite.image, offset_pos)

    scaled_surf = pygame.transform.smoothscale(self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
    scaled_rect = scaled_surf.get_rect(center = (self.half_w, self.half_h))
  
    self.display_surface.blit (scaled_surf, scaled_rect)

  def npc_update(self, player):
      npc_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'npc']
      for npcs in npc_sprites: 
        npcs.npc_update (player) 

  # def loveletter_update(self, player):
  #     loveletter_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'loveletter']
  #     for loveletter in loveletter_sprites:
  #       if hasattr(loveletter, 'loveletter_update'):
  #         loveletter.loveletter_update(player)


  def loveletter_update(self, player):
      # Filter the sprites to only include those with the sprite_type 'loveletter'
      loveletter_sprites = [sprite for sprite in self.sprites() if getattr(sprite, 'sprite_type', None) == 'loveletter']
      
      # Call the loveletter_update method on each loveletter sprite
      for loveletter in loveletter_sprites:
          loveletter.loveletter_update(player)


