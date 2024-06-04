import pygame 
from settings import *
from tile import Tile
from player import Player
from camera import CameraGroup
from support import *
from random import choice
from npc import NPC 	

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
            'entities' : import_csv_layout ('Data/maps csv/maps2_players.csv')
        }   
        graphics = {
            'trees': import_folder('sprites sheet for maps/Terrains/object'),
            'houses': import_folder ('sprites sheet for maps/Terrains/buildings'),
            'rocks': import_folder ('sprites sheet for maps/Terrains/rocks_bush'),
            'npcs': import_folder ('sprites sheet for maps/sprites/characters/players sprites')
        }

        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
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
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites],'rock and bushes',random_rock_image)

                        if style == 'house':
                            house_index = int(col) 
                            if 0 <= house_index < len(graphics['houses']):
                                house_img = graphics['houses'][house_index]
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'house',house_img)

                        if style == 'entities': 
                            if col == '771':
                                self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)

                            else: 
                                if col == '0': npc_name = 'maria'
                                elif col == '1': npc_name ='willie'
                                elif col == '2': npc_name = 'amber'
                                else: npc_name = 'officer'
                                NPC(npc_name, (x,y), 'speech', [self.visible_sprites],self.obstacle_sprites)

    def reset_player_position(self, x, y):
        self.player.rect.topleft = (x, y)

    def run(self):
        # update and draw the game(display)
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.npc_update(self.player)
        self.visible_sprites.update()
