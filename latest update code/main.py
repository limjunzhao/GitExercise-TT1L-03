import pygame, sys
from settings import *
from level import Level 
from camera import CameraGroup
from button import Button 
from pause import *
from npc import Dialogue, Execution, NPC

class Interface:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.button_sfx = pygame.mixer.Sound("images/music/button_sfx.mp3")
        self.font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
        self.music_sfx = pygame.mixer.Sound("images/music/music_background.mp3")
        self.vol = 0.1
        self.music_sfx.play(loops = -1)
        self.music_sfx.set_volume(self.vol)
       
    def main_menu(self):
        # Load images
        startstatic_img = pygame.image.load('images/button/start_static.png')
        starthover_img = pygame.image.load('images/button/start_hover.png')
        quitstatic_img = pygame.image.load('images/button/quit_static.png')
        quithover_img = pygame.image.load('images/button/quit_hover.png')
        optionhover_img = pygame.image.load('images/button/opt_hover.png')
        optionstatic_img = pygame.image.load('images/button/opt_static.png')

        background_image = pygame.image.load('images/background/mane_background1.jpg')
        background_image = pygame.transform.scale(background_image, (WIDTH,HEIGHT))

        title_img = pygame.image.load('images/title.png')
        title_img = pygame.transform.scale(title_img, (600, 350))

        image_rect = startstatic_img.get_rect()
        image_x = (WIDTH - image_rect.width) // 2

        start_button = Button(image_x, 400, startstatic_img, starthover_img, (200, 100))
        quit_button = Button(image_x, 500, quitstatic_img, quithover_img, (200, 100))
        option_button = Button(10, 10, optionstatic_img, optionhover_img, (75, 75))
        
        

        
        while True:
            self.screen.blit(background_image, (0, 0))
            self.screen.blit(title_img, (400, 80))

            """
            If possible, return state = "start" / "quit" / "option" 
            States are very usefull for compelx games btw, learn how to use them more oftenly
            
            """
            if start_button.draw(self.screen):
                self.button_sfx.play()
                self.music_sfx.set_volume(0)
                return "start"
                

            if quit_button.draw(self.screen):
                self.button_sfx.play()
                return "quit"

            if option_button.draw(self.screen):
                self.button_sfx.play()
                return "option"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def option(self):
        # Load images
        volup_static = pygame.image.load('images/button/vol_up.png')
        volup_hover = pygame.image.load('images/button/vol_up-hover.png')
        voldown_static = pygame.image.load('images/button/vol_down-static.png')
        voldown_hover = pygame.image.load('images/button/vol_down-hover.png')
        volmute_static = pygame.image.load('images/button/vol_mute-static.png')
        volmute_hover = pygame.image.load('images/button/vol_mute-hover.png')
        back_static = pygame.image.load('images/button/back_static.png')
        back_hover = pygame.image.load('images/button/back_hover.png')

        background_image = pygame.image.load('images/background/mane_background1.jpg')
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

        vol_up_button = Button(425, 200, volup_static, volup_hover, (200, 100))
        vol_down_button = Button(625, 200, voldown_static, voldown_hover, (200, 100))
        vol_mute_button = Button(425, 300, volmute_static, volmute_hover, (408, 100))
        back_button = Button(5, 640, back_static, back_hover, (150, 80))

        while True:
            self.screen.fill('grey')
            self.screen.blit(background_image, (0, 0))

            if vol_up_button.draw(self.screen):
                self.button_sfx.play()
                self.adjust_volume(0.1)

            if vol_down_button.draw(self.screen):
                self.button_sfx.play()
                self.adjust_volume(-0.1)

            if vol_mute_button.draw(self.screen):
                self.button_sfx.play()
                self.music_sfx.set_volume(0)

            if back_button.draw(self.screen):
                self.button_sfx.play()
                return "back" # name option back button as back 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
    
    def story_info(self):

        # Define messages with multiple layers
        messages = [
            [
                {"text": "In the fog-drenched streets of Arcadia, a series of grisly murder shatters",
                "color": WHITE,
                "position": (25, 250)},
                {"text": "the tranquility of its residents.",
                "color": WHITE,
                "position": (400, 300)},
            ],
            [
                {"text": "Its’s 7am in the morning and you discovered the victim’s body laying",
                "color": WHITE,
                "position": (60, 250)},
                {"text": "(outside a house/bar) and the blood was still damped which means.",
                "color": WHITE,  
                "position": (70, 300)},
                {"text": "the killing happened not long ago",
                "color": WHITE,  
                "position": (380, 350)}
            ],
            [
                {"text": "You, as a seasoned detective, are tasked with unraveling the mystery",
                "color": WHITE,
                "position": (70, 250)},
                {"text": "behind these brutal killings. Come on detective,",
                "color": WHITE,  
                "position": (260, 300)},
                {"text": "let’s not waste any time and find the murderer before it’s too late!",
                "color": WHITE,  
                "position": (100, 350)}
             ]
        ]


        # Main loop
        active_message = 0
        layer_counter = 0
        speed = 10  # Adjust the speed of typewriter effect

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RETURN and active_message < len(messages) - 1:
                        active_message += 1
                        layer_counter = 0  # Reset the layer counter when changing message 
                  elif event.key == pygame.K_RETURN and active_message == len(messages) - 1 and layer_counter >= speed * len(messages[active_message][-1]["text"]):
                        return "start_game"  # Signal to start the game


            # Clear the screen
            self.screen.fill(BLACK)

            # Display messages for the active layer
            for i, layer in enumerate(messages[active_message]):
                text = layer["text"]
                color = layer["color"]
                position = layer["position"]

                if layer_counter < speed * len(text):
                    layer_counter += 1

                text_surface = self.font.render(text[0:layer_counter // speed], True, color)
                self.screen.blit(text_surface, position)

            pygame.display.flip()

    def adjust_volume(self, vol_change):
        self.vol += vol_change 
        self.vol = max(0.0, min(1.0, self.vol))
        self.music_sfx.set_volume(self.vol)


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Mystery Case')
        self.clock = pygame.time.Clock()
        
        # bring the page here
        self.level = Level()
        self.camera_group = CameraGroup()
        self.interface = Interface()
        self.dialogue = Dialogue()
        self.execution = Execution()
        

         # main menu setup
        self.main_menu = self.interface.main_menu()   
        self.music_sfx = pygame.mixer.Sound("images/music/music_background.mp3")
        self.button_sfx = pygame.mixer.Sound("images/music/button_sfx.mp3")
        self.vol = 0.1
        self.music_sfx.play(loops = -1)
        self.music_sfx.set_volume(self.vol)
        
    def run_game(self):
        pause = False 

        while True:
            # events = pygame.event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if all(count>0 for count in NPC.interaction_counts.values()):
                        if event.key == pygame.K_a:
                            self.execution.you_win(self.screen)
                        elif event.key in (pygame.K_b, pygame.K_c, pygame.K_d):
                            self.execution.game_over(self.screen)
                   
                        
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pause = not pause  # Toggle the pause state
                    if not pause:
                        screen.fill(BLACK)  # Clear the screen when unpausing


            if pause:
                screen.blit(pause_surface, (0, 0))
                if vol_up_button.draw(self.screen):
                    self.button_sfx.play()
                    self.adjust_volume(0.1)

                if vol_down_button.draw(self.screen):
                    self.button_sfx.play()
                    self.adjust_volume(-0.1)

                if vol_mute_button.draw(self.screen):
                    self.button_sfx.play()
                    self.music_sfx.set_volume(0)
            else:
                screen.fill('#2D99E2')
                self.level.run()
                self.camera_group.update()


            pygame.display.update()
            clock.tick(FPS)

    def adjust_volume(self, vol_change):
        self.vol += vol_change 
        self.vol = max(0.0, min(1.0, self.vol))
        self.music_sfx.set_volume(self.vol)

    def run_menu(self):
              
        if self.main_menu == "start":
            action = self.interface.story_info()
            if action == "start_game":
                self.run_game()
           
        elif self.main_menu == "quit":
            pygame.quit()
            sys.exit()
        
        elif self.main_menu == "option":
            option_action = self.interface.option()                    
            if option_action == "back":
                self.interface.main_menu ()


if __name__ == '__main__':
            game = Game()
            game.run_menu()
            
else: 
            game = Game()
            game.run_game()


