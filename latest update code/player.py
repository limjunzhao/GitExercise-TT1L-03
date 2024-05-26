import pygame 
from settings import *
from entity import Entity

class Player(Entity):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('sprites sheet for maps/sprites/characters/player_single.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)

		#if we didnt put any argument inside this Vector2(), it will default as (0,0) 
		self.direction = pygame.math.Vector2()
		self.speed = 3
		
		self.obstacle_sprites = obstacle_sprites
		pygame.display.update
		
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
		#the reason adding this code is to make sure the character moving in any direction will be the length = 1 (normalize), either up down or diagonal
		#need this if statement bcuz we dont have != 0 it show erro bcuz 0 cannot be normalize 
		if self.direction.magnitude() != 0: 
			self.direction = self.direction.normalize()
		#this is to link to self.rect which is our player.rect so that it will flw the input we give and move 
		
		self.hitbox.x += self.direction.x * speed 
		#collision check w 'horizontal'
		self.collision('horizontal') 
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center

	def update(self):
		self.input()
		#we update the move thingy to main.py and put the self.speed = speed = 5 into argument 
		self.move (self.speed)
	

