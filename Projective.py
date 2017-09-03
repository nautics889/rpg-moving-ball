import pygame
from Const import *

class Projective():
    def __init__(self,direction,image_pack):
        self.direction = direction
        self.image = pygame.image.load(image_pack).convert_alpha()
        self.images = []
        self.images.append(self.image.subsurface(0,0,128,128))
        self.images.append(self.image.subsurface(0,0,128,128))
        self.images.append(self.image.subsurface(0,0,128,128))
        self.images.append(self.image.subsurface(0,0,128,128))
    def render(self,screen):
        screen.blit(self.images[self.direction], (self.x, self.y))
    def move(self):
        if self.direction == RIGHT:
            self.x += self.speed
        elif self.direction == DOWN:
            self.y += self.speed
        elif self.direction == LEFT:
            self.x -= self.speed
        else:
            self.y -= self.speed
        
class WaterBall(Projective):
    def __init__(self,x_start,y_start,direction):
        self.x = x_start
        self.y = y_start
        self.image = "data/waterball.png"
        self.speed = 5
        Projective.__init__(self, direction, self.image)