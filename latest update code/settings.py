import pygame
pygame.init()


# game setup
WIDTH    = 1280	
HEIGHT   = 720
FPS      = 60
TILESIZE = 16
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 35
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 24)
SPEECH_FONT = pygame.font.SysFont(None, 28)
speech_text = ""




npc_data = {
    'maria': { "position": (100, 100), "speech": "In the morning, I made breakfast for my husband..." }, 
    #'img':'sprites sheet for maps/sprites/characters/player_single.png'},

    'willie': {"position": (600, 400), "speech": "Breakfast with my wife started the day..."},
    #'img':'sprites sheet for maps/sprites/characters/player_single.png'},
    
    'amber': {"position": (600, 100), "speech": "In the day, I exercised in the park..." },
    #'img':'sprites sheet for maps/sprites/characters/player_single.png'},
    
    'officer': {"position": (100, 400), "speech": "Please help me find the killer before it's too late!" } 
    #'img':'sprites sheet for maps/sprites/characters/player_single.png'}
}



BG = (50, 50, 50)
