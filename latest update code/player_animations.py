import pygame
from settings import *
from support import import_folder
from entity import Entity

class animation(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("./sprites sheet for maps/sprites/characters/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-48, -48)

        self.import_player_assets()
        self.speed = 3
        self.status = 'idle'
        self.animation_speed = 0.025
        self.obstacle_sprites = obstacle_sprites
        self.frame_index = 0

    def import_player_assets(self):
        character_path = "./sprites sheet for maps/sprites/characters/player/"
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            self.status = 'down'

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)



    def animate_multiple(self, surface):
        positions = {
            'up': (750, 265),
            'down': (750, 295),
            'left': (750, 325),
            'right': (750, 355),
        }

        for status in positions.keys():
            animation = self.animations[status]
            self.frame_index += self.animation_speed
            if self.frame_index >= len(animation):
                self.frame_index = 0

            self.image = animation[int(self.frame_index)]
            position = positions[status]
            surface.blit(self.image, position)
