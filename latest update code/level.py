import pygame 
from settings import *
from tile import Tile
from player import Player
from camera import CameraGroup
from support import *

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = CameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		layout = {
						'boundary': import_csv_layout('../Data/maps csv/ground_Floorblocks.csv'),


		}

		#style is boundary and layout is the csv file we import 
		for style,layout in layout.items():
			#this is to check the row and helps to coordinates the pos.y
			for row_index,row in enumerate(layout):
				#check each of the column elements (x,p or empty) and helps to coordinate pos.x
				for col_index, col in enumerate(row):
					#multiply the col and row with the size of our tile so that it can fit
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites], 'invisible ')

		# 		if col == 'x':
		# 			#check the pos of column and row and group it under the visible_sprites
		# 			#since the rock will have collision with the player, so we also put it under obstacle_sprites
		# 			Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
		# 		if col == 'p':
		# 			self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)
			self.player = Player((500,420),[self.visible_sprites], self.obstacle_sprites)
				

	def run(self):
		# update and draw the game(display)
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()

