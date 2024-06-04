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
FONT_NAME = pygame.font.SysFont(None, 30)
SPEECH_FONT = pygame.font.SysFont(None, 28)
speech_text = ""
BG = (50, 50, 50)



npc_data = {
    'Maria': {'who': "In the morning, I made breakfast for my husband...",
                'where' : 'ahdfjkhjksafjkahdf', 
                'what' : ' ajsghdkfjhskfkajsg',
                "greeting":''
            }, 

    'Willie': {'who': "Breakfast with my wife started the day...",
                'where' : 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 
                'what' : ' fffffffffffffffffffffffffffffffff',
                "greeting":''
            },
    
    'Amber': {'who': "In the day, I exercised in the park...",
                'where' : 'In the morning, I made breakfast for my husband...In the morning, I made breakfast for my husband..In the morning, I made breakfast for my husband...In the morning, I made breakfast for my husband..In the morning, I made breakfast for my husband...In the morning, I made breakfast for my husband..', 
                'what' : ' hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',
                "greeting":''
            },
    
    
    'Officer': {'who': '',
                'where' : '', 
                'what' : '',
                "greeting": "Please help me find the killer before it's too late!"
            },

    'Professor':{'who': '',
                'where' : '', 
                'what' : '',
                "greeting": 'Do you wanna come to school and learn our language?'},
        

}

npc_ques =  ' A. Where you at last night? \n B. Who are you, whats your name? \n C. What did you do last night?'
test = 'halo halo halo halo halo halo halo halo halo'



# messages = {
#     {
                
#                 'text' : {
#                     "In the fog-drenched streets of Arcadia, a series of grisly murder shatters", 

#                     "the tranquility of its residents.",

#                     "Its’s 7am in the morning and you discovered the victim’s body laying",

#                     "(outside a house/bar) and the blood was still damped which means.",  

#                     "the killing happened not long ago",

#                     "You, as a seasoned detective, are tasked with unraveling the mystery",  

#                     "behind these brutal killings. Come on detective,",   

#                     "let’s not waste any time and find the murderer before it’s too late!",     
#                 }
#             }




# }