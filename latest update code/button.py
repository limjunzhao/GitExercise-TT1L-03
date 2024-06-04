import pygame

class Button():
        def __init__(self, x, y, static_image, hover_image, scale):
            
            self.static_image = pygame.transform.scale(static_image, scale)
            self.hover_image = pygame.transform.scale(hover_image, scale)
            self.image = self.static_image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self,screen):
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


        def collidepoint(self, pos):
            return self.rect.collidepoint(pos)


