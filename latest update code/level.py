import pygame 
from settings import *
from tile import Tile
from player import Player


class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YsortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		#this is to check the row and helps to coordinates the pos.y
		for row_index,row in enumerate(WORLD_MAP):
			#check each of the column elements (x,p or empty) and helps to coordinate pos.x
			for col_index, col in enumerate(row):
				#multiply the col and row with the size of our tile so that it can fit
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					#check the pos of column and row and group it under the visible_sprites
					#since the rock will have collision with the player, so we also put it under obstacle_sprites
					Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)
				

	def run(self):
		# update and draw the game(display)
		self.visible_sprites.draw(self.display_surface)
		self.visible_sprites.update()

#function as camera 
class YsortCameraGroup (pygame.sprite.Group):
	def __init__(self):

		#general setup
		super().__init__()