import pygame, sys
from settings import *
from level import Level 
from camera import CameraGroup

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

	def run(self):
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



if __name__ == '__main__':
	game = Game()
	game.run()