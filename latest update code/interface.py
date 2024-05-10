import pygame
from button import Button 



class interface(): 
  def __init__ (self):
    pass


  def main_menu(self):
    # Load images
    self.image = startstatic_img = pygame.image.load('images/start_static.png')
    self.image = starthover_img = pygame.image.load('images/start_hover.png')
    self.image = quitstatic_img = pygame.image.load('images/quit_static.png')
    self.image = quithover_img = pygame.image.load('images/quit_hover.png')
    self.image = optionhover_img = pygame.image.load('images/opt_hover.png')
    self.image = optionstatic_img = pygame.image.load('images/opt_static.png')
    self.background_image = pygame.image.load('images/mane_background1.jpg')
    self.background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))
    self.title_img = pygame.image.load('images/title.png')
    self.title_img = pygame.transform.scale(title_img, (600,350))


    self.image_rect = image.get_rect()
    self.image_x = (SCREEN_HEIGHT - image_rect.width) // 2

    # x = SCREEN_HEIGHT
    # y = SCREEN_WIDTH

    # Main screen
    self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    self.pygame.display.set_caption('platform game')

    #pos of button on 1st menu when entering the game 
    self.start_button = Button(image_x, 400, startstatic_img, starthover_img, (200, 100))
    self.quit_button = Button(image_x, 500, quitstatic_img, quithover_img, (200, 100))
    self.option_button = Button(10, 10, optionstatic_img, optionhover_img, (75, 75))