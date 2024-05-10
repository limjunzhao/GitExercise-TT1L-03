import pygame, sys
from settings import *
from level import Level 
from camera import CameraGroup
# from interface import *
# from button import Button 

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH), pygame.RESIZABLE)
		pygame.display.set_caption('Mystery Case')
		self.clock = pygame.time.Clock()
		#bring the level page here 
		self.level = Level()
		self.camera_group = CameraGroup()



		#main menu setup
		# self.main_menu = main_menu()
		# self.button = Button()



	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			
			self.screen.fill('black')
			self.level.run()
			self.camera_group.update()
			pygame.display.update()
			self.clock.tick(FPS)
	


	# def run_menu(self):
	# 	run_game() == False
	# 	while True:
	# 				# screen.fill('grey')
	# 			self.screen.blit(background_image, (0,0))
	# 			self.screen.blit(title_img, (400,80))	 


	# 			if start_button.draw():
	# 				pass

	# 			if quit_button.draw():
	# 				pass

	# 			if option_button.draw():
	# 				pass

	# 			pygame.display.update()


if __name__ == '__main__':
	game = Game()
	# game.run_menu()
	game.run_game()