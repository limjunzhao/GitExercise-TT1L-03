import pygame
from settings import *
import spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        
        # Load sprite sheet
        sprite_sheet_image = pygame.image.load('dino.png').convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
        
        # Define animation frames
        self.animation_steps = [6, 6, 6]
        self.frame_coords = [
            [(0, 0), (48, 0), (96, 0), (144, 0), (192, 0), (240, 0)],
            [(0, 48), (48, 48), (96, 48), (144, 48), (192, 48), (240, 48)],
            [(0, 96), (48, 96), (96, 96), (144, 96), (192, 96), (240, 96)],
        ]
        self.animation_list = self.load_animation_frames(self.sprite_sheet, self.animation_steps, self.frame_coords, 48, 48, 1, BLACK)

        # Set initial image and rect
        self.action = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 145
        self.image = self.animation_list[self.action][self.frame]
        self.rect = self.image.get_rect(topleft=pos)
        
        # Movement attributes
        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.obstacle_sprites = obstacle_sprites
        
    def load_animation_frames(self, sprite_sheet, animation_steps, frame_coords, frame_width, frame_height, scale, color_key):
        animation_list = []
        for steps, coords in zip(animation_steps, frame_coords):
            temp_image_list = []
            for i in range(steps):
                x, y = coords[i]
                temp_image_list.append(sprite_sheet.get_image(x, y, frame_width, frame_height, scale, color_key))
            animation_list.append(temp_image_list)
        return animation_list
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.action = 1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.action = 2
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.action = 2
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.action = 1
        else:
            self.direction.x = 0
        
        if self.direction.x == 0 and self.direction.y == 0:
            self.action = 0
        
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0
        self.image = self.animation_list[self.action][self.frame]
        
    def update(self):
        self.input()
        self.move(self.speed)
        self.update_animation()

# Pygame initialization and game loop would go here, similar to your second code
