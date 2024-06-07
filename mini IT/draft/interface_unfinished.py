import pygame

pygame.init()


music_sfx = pygame.mixer.Sound("images/music/music_background.mp3")


vol = 0.1

music_sfx.play(loops = -1)
music_sfx.set_volume(vol)





def adjust_volume(vol_change):
    global vol
    vol += vol_change 
    vol = max(0.0, min(1.0, vol))
    music_sfx.set_volume(vol)




def story_info(): 

    WIDTH, HEIGHT = 1280, 720
    SCREEN_SIZE = (WIDTH, HEIGHT)

    # Set colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Set the text font and size
    FONT_SIZE = 35
    font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)

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


    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Text with Multiple Layers")

    # Main loop
    run = True
    active_message = 0
    layer_counter = 0
    speed = 10  # Adjust the speed of typewriter effect

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and active_message < len(messages) - 1:
                    active_message += 1
                    layer_counter = 0  # Reset the layer counter when changing message

        # Clear the screen
        screen.fill(BLACK)

        # Display messages for the active layer
        for i, layer in enumerate(messages[active_message]):
            text = layer["text"]
            color = layer["color"]
            position = layer["position"]

            if layer_counter < speed * len(text):
                layer_counter += 1

            text_surface = font.render(text[0:layer_counter // speed], True, color)
            screen.blit(text_surface, position)

        pygame.display.flip()



def main_menu():
    SCREEN_HEIGHT = 1280
    SCREEN_WIDTH = 720
 

    # Load images
    image = startstatic_img = pygame.image.load('images/button/start_static.png')
    image = starthover_img = pygame.image.load('images/button/start_hover.png')
    image = quitstatic_img = pygame.image.load('images/button/quit_static.png')
    image = quithover_img = pygame.image.load('images/button/quit_hover.png')
    image = optionhover_img = pygame.image.load('images/button/opt_hover.png')
    image = optionstatic_img = pygame.image.load('images/button/opt_static.png')
    background_image = pygame.image.load('images/background/mane_background1.jpg')
    background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))
    title_img = pygame.image.load('images/title.png')
    title_img = pygame.transform.scale(title_img, (600,350))


    image_rect = image.get_rect()
    image_x = (SCREEN_HEIGHT - image_rect.width) // 2

    # x = SCREEN_HEIGHT
    # y = SCREEN_WIDTH

    # Main screen
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption('platform game')

    # load music
 
    

   
    
    # Class for button
    class Button():
        def __init__(self, x, y, static_image, hover_image, scale):
            self.static_image = pygame.transform.scale(static_image, scale)
            self.hover_image = pygame.transform.scale(hover_image, scale)
            self.image = self.static_image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                self.image = self.hover_image
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            else:
                self.image = self.static_image
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action
    
            

    start_button = Button(image_x, 400, startstatic_img, starthover_img, (200, 100))
    quit_button = Button(image_x, 500, quitstatic_img, quithover_img, (200, 100))
    option_button = Button(10, 10, optionstatic_img, optionhover_img, (75, 75))
    button_sfx = pygame.mixer.Sound("images/music/button_sfx.mp3")
 


    run = True
    while run:
        # screen.fill('grey')
        screen.blit(background_image, (0,0))
        screen.blit(title_img, (400,80))

        

        if start_button.draw():
            button_sfx.play()
            story_info()
          

        if quit_button.draw():
            button_sfx.play()
            pygame.quit()

        if option_button.draw():
            button_sfx.play()
            option()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

def option():
    SCREEN_HEIGHT = 1280
    SCREEN_WIDTH = 720

    # load images
    image = volup_static = pygame.image.load('images/button/vol_up.png')
    image = volup_hover = pygame.image.load('images/button/vol_up-hover.png')
    image = voldown_static = pygame.image.load('images/button/vol_down-static.png')
    image = voldown_hover = pygame.image.load('images/button/vol_down-hover.png')
    image = volmute_static = pygame.image.load('images/button/vol_mute-static.png')
    image = volmute_hover = pygame.image.load('images/button/vol_mute-hover.png')
    image = back_static = pygame.image.load('images/button/back_static.png')
    image = back_hover = pygame.image.load('images/button/back_hover.png')
    background_image = pygame.image.load('images/background/mane_background1.jpg')
    background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))


    # later got img for background alrdt=y put hereeee!!!
    # # background_image = pygame.image.load('background43.jpg')
    # # background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))


    image_rect = image.get_rect()
    image_x = (SCREEN_HEIGHT - image_rect.width) // 2

    # Main screen
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption('platform game')

    # load music
    button_sfx = pygame.mixer.Sound("images/music/button_sfx.mp3")
    

   
    
    # Class for button
    class Button():
        def __init__(self, x, y, static_image, hover_image, scale):
            self.static_image = pygame.transform.scale(static_image, scale)
            self.hover_image = pygame.transform.scale(hover_image, scale)
            self.image = self.static_image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                self.image = self.hover_image
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            else:
                self.image = self.static_image
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action
    
            

    vol_up_button = Button(425, 200, volup_static, volup_hover, (200, 100))
    vol_down_button = Button(625, 200, voldown_static, voldown_hover, (200, 100))
    vol_mute_button = Button(425, 300, volmute_static, volmute_hover, (408, 100))
    back_button = Button( 5, 640, back_static, back_hover, (150, 80))



    run = True
    while run:
        screen.fill('grey')
        screen.blit(background_image, (0,0))
        

        if vol_up_button.draw():
            button_sfx.play()
            adjust_volume(0.1)
          

        if vol_down_button.draw():
            button_sfx.play()
            adjust_volume(-0.1)

        if vol_mute_button.draw():
            button_sfx.play()
            music_sfx.set_volume(0)
        
        if back_button.draw():
            button_sfx.play()
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()



main_menu()



