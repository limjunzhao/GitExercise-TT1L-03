import pygame 
from settings import *
from tile import Tile
from player import Player
from camera import CameraGroup
from support import *
from random import choice
from npc import NPC 	
from minigame import Jumbleword


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
					'rock': import_csv_layout('Data/maps csv/maps2_rock_bush.csv'),
					'entities' : import_csv_layout ('Data/maps csv/maps2_players.csv'),
					'loveletter' : import_csv_layout ('Data/maps csv/maps2_mailbox.csv'),
					'decor': import_csv_layout ('Data/maps csv/maps2_utils.csv')

					
		}	
		graphics = {
					'trees': import_folder('sprites sheet for maps/Terrains/object'),
					'houses': import_folder ('sprites sheet for maps/Terrains/buildings'),
					'rocks': import_folder ('sprites sheet for maps/Terrains/rocks_bush'),
					'npcs': import_folder ('sprites sheet for maps/sprites/characters/players sprites'),
					'decors' : import_folder ('sprites sheet for maps/Terrains/decors')
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
								tree_index = int(col) 
								if 0 <= tree_index < len(graphics['trees']):
									tree_img = graphics['trees'][tree_index]
									Tile((x,y),[self.visible_sprites],'tree',tree_img)

							if style == 'rock':
								random_rock_image = choice(graphics['rocks'])
								

							if style == 'house':
								house_index = int(col) 
								if 0 <= house_index < len(graphics['houses']):
									house_img = graphics['houses'][house_index]
									Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'house',house_img)

							if style == 'decor':
								decor_index = int(col) 
								if 0 <= decor_index < len(graphics['decors']):
									decor_img = graphics['decors'][decor_index]
									Tile((x,y),[self.visible_sprites, self.obstacle_sprites],'decor',decor_img)
					
							
									

							if style == 'entities': 
								if col == '771':
									self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)
								
								elif col == '6': 
									dead_body = pygame.image.load('images/dead_body.png')
									Tile((x,y),[self.visible_sprites],'dead_dino', dead_body)

								else: 
									if col == '0': npc_name = 'Maria'
									elif col == '1': npc_name ='Willie'
									elif col == '2': npc_name = 'Amber'
									elif col == '3': npc_name = 'Officer'
									elif col == '4': npc_name ='Professor'
									elif col == '5': npc_name = 'Alex'
									NPC(npc_name, (x,y), 'speech', [self.visible_sprites],self.obstacle_sprites)
						
				

	def run(self):
		# update and draw the game(display)
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.npc_update(self.player)
		self.visible_sprites.update()

		
		