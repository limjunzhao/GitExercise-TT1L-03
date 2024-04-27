import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('MyGame/Character/player_single.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)

		#if we didnt put any argument inside this Vector2(), it will default as (0,0) 
		self.direction = pygame.math.Vector2()
		self.speed = 3
		
		self.obstacle_sprites = obstacle_sprites

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
		
		self.rect.x += self.direction.x * speed 
		#collision check w 'horizontal'
		self.collision('horizontal') 
		self.rect.y += self.direction.y * speed
		self.collision('vertical')
		#self.rect.center *(x,y)tgt* += self.direction * speed



	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				#detect if the obstacles collide w the player
				if sprite.rect.colliderect(self.rect):
					if self.direction.x > 0: #player moving right 
							self.rect.right = sprite.rect.left
					if self.direction.x < 0: #player moving left
							self.rect.left = sprite.rect.right #the rect of player will not overlap w the obstacles sprite

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.y > 0: #player moving down
						self.rect.bottom = sprite.rect.top
					if self.direction.y < 0: #player moving up
						self.rect.top = sprite.rect.bottom

	def update(self):
		self.input()
		#we update the move thingy to main.py and put the self.speed = speed = 5 into argument 
		self.move (self.speed)