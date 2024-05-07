import pygame

pygame.init()


music_sfx = pygame.mixer.Sound("music_background.mp3")


vol = 0.1

music_sfx.play(loops = -1)
music_sfx.set_volume(vol)


def adjust_volume(vol_change):
    global vol
    vol += vol_change 
    vol = max(0.0, min(1.0, vol))
    music_sfx.set_volume(vol)




def story_info(): 
    import pygame

    pygame.init()
    enter = "click enter"
    font = pygame.font.Font('freesansbold.ttf', 35)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()
    messages = [
        " In the fog-drenched streets of Arcadia,",
        " a series of grisly murders shatters ",
        "the tranquility of its residents.",
        "It's 7am in the morning and you discovered",
        " the victim's body laying (outside a house/bar)",
        " and the blood was still damp, which means",
        " the killing happened not long ago.",
        "You, as a seasoned detective, are tasked with",
        " unraveling the mystery behind these brutal killings. ",
        " Come on detective, let's not waste any time",
        " find the murderer before it's too late!"
    ]

    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    current_line = 0
    done = False

    def render_message(message_lines, counter, current_line):
        rendered_lines = []
        for i, line in enumerate(message_lines):
            if i < current_line:
                rendered_lines.append(line)
            elif i == current_line:
                rendered_lines.append(line[:counter])
        return '\n'.join(rendered_lines)

    run = True
    while run:
        screen.fill('grey')
        timer.tick(60)

        message_lines = messages[active_message].split('\n')

        if counter < speed * len(message_lines[current_line]):
            counter += 1
        elif counter >= speed * len(message_lines[current_line]):
            if current_line < len(message_lines) - 1:
                current_line += 1
                counter = 0
            else:
                done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    current_line = 0
                    counter = 0
                    done = False

        rendered_message = render_message(message_lines, counter // speed, current_line)
        snip = font.render(rendered_message, True, (0,0,0))
        screen.blit(snip, (300, 310))
        

        pygame.display.flip()

    pygame.quit()



def main_menu():
    SCREEN_HEIGHT = 1280
    SCREEN_WIDTH = 720
 


    font =  pygame.font.Font('freesansbold.ttf', 50)
    screen = pygame.display.set_mode([800, 500])
    timer = pygame.time.Clock()
    message = 'game title !!!'
    snip = font.render('' , True, 'white')
    counter = 0 
    speed = 3
    done = False

    # Load images
    image = startstatic_img = pygame.image.load('start_static.png')
    image = starthover_img = pygame.image.load('start_hover.png')
    image = quitstatic_img = pygame.image.load('quit_static.png')
    image = quithover_img = pygame.image.load('quit_hover.png')
    image = optionhover_img = pygame.image.load('opt_hover.png')
    image = optionstatic_img = pygame.image.load('opt_static.png')
    # # background_image = pygame.image.load('background43.jpg')
    # # background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))


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
    button_sfx = pygame.mixer.Sound("button_sfx.mp3")
 


    run = True
    while run:
        screen.fill('grey')
        # screen.blit(background_image, (0,0))



        
        timer.tick(60)
        pygame.draw.rect(screen, 'black', [500, 50, 350, 150 ])
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (510, 100))
        

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
    image = volup_static = pygame.image.load('vol_up.png')
    image = volup_hover = pygame.image.load('vol_up-hover.png')
    image = voldown_static = pygame.image.load('vol_down-static.png')
    image = voldown_hover = pygame.image.load('vol_down-hover.png')
    image = volmute_static = pygame.image.load('vol_mute-static.png')
    image = volmute_hover = pygame.image.load('vol_mute-hover.png')
    image = back_static = pygame.image.load('back_static.png')
    image = back_hover = pygame.image.load('back_hover.png')


    # later got img for background alrdt=y put hereeee!!!
    # # background_image = pygame.image.load('background43.jpg')
    # # background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))


    image_rect = image.get_rect()
    image_x = (SCREEN_HEIGHT - image_rect.width) // 2

    # Main screen
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption('platform game')

    # load music
    button_sfx = pygame.mixer.Sound("button_sfx.mp3")
    

   
    
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



