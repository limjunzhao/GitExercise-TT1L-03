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

        self.scale_factor = 3 # Define the scale factor
        self.import_player_assets()
        self.speed = 3
        self.status = 'idle'
        self.animation_speed = 0.04
        self.obstacle_sprites = obstacle_sprites
        self.frame_index = 0

    def import_player_assets(self):
        character_path = "./sprites sheet for maps/sprites/characters/player/"
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            frames = import_folder(full_path)
            scaled_frames = [pygame.transform.scale(frame, (int(frame.get_width() * self.scale_factor), int(frame.get_height() * self.scale_factor))) for frame in frames]
            self.animations[animation] = scaled_frames

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
            'up': (750, 160),
            'down': (750, 240),
            'left': (750, 320),
            'right': (750, 400),
        }

        for status in positions.keys():
            animation = self.animations[status]
            self.frame_index += self.animation_speed
            if self.frame_index >= len(animation):
                self.frame_index = 0

            self.image = animation[int(self.frame_index)]
            position = positions[status]
            surface.blit(self.image, position)