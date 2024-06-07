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
BG = (50, 50, 50)



npc_data = {
    'maria': {'who': "my name is Maria.",
                'where' : 'In the morning, I made breakfast for my husband, then proceeded to do house chores until afternoon. After lunch with my husband, I engaged in a pleasant chit-chat with out neighbor, Amber', 
                'what' : 'I eagerly awaited my husband’s return from work, and once he was back, we cooked dinner together and went to sleep afterwards.',
                "greeting":'',
                "rawr": "raaawr rawr"
            }, 

    'willie': {'who': "my name is Willie.",
                'where' : 'I started my day by having breakfast with my wife Maria, followed by me heading to work, I then head to lunch with my wife and returned to work.', 
                'what' : 'I came back home from work and got the ingredients ready and cooked dinner with my wife. After that, we went to bed before 10pm.',
                "greeting":'',
                "rawr": "raaawr rawr"
            },
    
    'amber': {'who': "my name is Amber.",
                'where' : 'In the day, I exercised in the park. And after that I had my coffee and breakfast. Meanwhile I watched TV for the time to pass. During lunch, I ate my leftover dinner from yesterday as my lunch. After lunch, me and Maria had our usual chit-chat but it was shorter than usual. And we were supposed to get groceries after that. So I went to buy the groceries myself and made dinner.', 
                'what' : 'As night falls, I took my dog for a night walk and went to bed.',
                "greeting":'',
                "rawr": "raaawr rawr"
            },
    
    
    'officer': {'who': '',
                'where' : '', 
                'what' : '',
                "greeting": "Please help me find the killer before it's too late!",
                "rawr": "raaawr rawr"
            },

    'professor':{'who': '',
                'where' : '', 
                'what' : '',
                "greeting": 'Hello there dear treveller, would you likde to learn our language?'},
        

}

npc_ques =  ' A. Where were you you yesterday? \n B. Who are you, whats your name? \n C. What did you do last night?'
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