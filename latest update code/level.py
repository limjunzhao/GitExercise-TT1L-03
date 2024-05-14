import pygame 
from settings import *
from tile import Tile
from player import Player
from camera import CameraGroup
from support import *
from random import choice

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
					'boundary': import_csv_layout('Data/maps csv/maps2_Floorblocks.csv'),
					'tree' : import_csv_layout('Data/maps csv/maps2_Tree.csv'),
					'house': import_csv_layout('Data/maps csv/maps2_HouseBuilding.csv'),
					'rock': import_csv_layout('Data/maps csv/maps2_rock_bush.csv')
					
		}	
		graphics = {
					'trees': import_folder('sprites sheet for maps/Terrains/object'),
					'houses': import_folder ('sprites sheet for maps/Terrains/buildings'),
					'rocks': import_folder ('sprites sheet for maps/Terrains/rocks_bush'),
		}

		 
		for style,layout in layout.items(): #style is boundary and layout is the csv file we import
			for row_index,row in enumerate(layout): #this is to check the row and helps to coordinates the pos.y
				for col_index, col in enumerate(row): #check each of the column elements (x,p or empty) and helps to coordinate pos.x
					if col != '-1':
						x = col_index * TILESIZE #multiply the col and row with the size of our tile so that it can fit
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites], 'invisible ')	

						if style == 'tree':
							house_index = int(col) 
							if 0 <= house_index < len(graphics['trees']):
								surf = graphics['trees'][house_index]
								Tile((x,y),[self.visible_sprites],'tree',surf)

						if style == 'rock':
							random_rock_image = choice(graphics['rocks'])
							Tile((x,y),[self.visible_sprites],'rock and bushes',random_rock_image)

						if style == 'house':
							house_index = int(col) 
							if 0 <= house_index < len(graphics['houses']):
								surf = graphics['houses'][house_index]
								Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'house',surf)
						

		
			self.player = Player((500,1420),[self.visible_sprites], self.obstacle_sprites)
				

	def run(self):
		# update and draw the game(display)
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()

