import pygame
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("./sprites sheet for maps/sprites/characters/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-48, -48)

        self.import_player_assets()
        self.speed = 3
        self.status = 'down'
        self.animation_speed = 0.5
        self.obstacle_sprites = obstacle_sprites
        self.frame_index = 0

    def import_player_assets(self):
        character_path = "./sprites sheet for maps/sprites/characters/player/"
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 'idle': []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self): 
        running_speed = 5
        current_speed = 3
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT]:
            self.speed = running_speed
        else:
            self.speed = current_speed 

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1 
            self.status = 'up'
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1 
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1 
            self.status = 'left'
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1 
            self.status = 'right'
        else:
            self.direction.x = 0

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            self.status = 'idle'

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)

    def animate_multiple(self, surface):
        positions = {
            'up': (50, 50),
            'down': (150, 50),
            'left': (50, 150),
            'right': (150, 150),
        }

        for status in positions.keys():
            animation = self.animations[status]
            self.frame_index += self.animation_speed
            if self.frame_index >= len(animation):
                self.frame_index = 0

            self.image = animation[int(self.frame_index)]
            position = positions[status]
            surface.blit(self.image, position)
