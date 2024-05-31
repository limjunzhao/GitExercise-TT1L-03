import pygame 
from settings import * 


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups): 
        super().__init__(groups)
    
    def collision(self,direction):
        if direction == 'horizontal':
          for sprite in self.obstacle_sprites:
            #detect if the obstacles collide w the player
            if sprite.hitbox.colliderect(self.hitbox):
              if self.direction.x > 0: #player moving right 
                  self.hitbox.right = sprite.hitbox.left
              if self.direction.x < 0: #player moving left
                  self.hitbox.left = sprite.hitbox.right #the rect of player will not overlap w the obstacles sprite

        if direction == 'vertical':
          for sprite in self.obstacle_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
              if self.direction.y > 0: #player moving down
                self.hitbox.bottom = sprite.hitbox.top
              if self.direction.y < 0: #player moving up
                self.hitbox.top = sprite.hitbox.bottom
          



