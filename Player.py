# -*- coding: utf-8 -*-'''
import pygame
from Const import *
from pygame.examples.oldalien import PLAYER_SPEED

class Player():
    def __init__(self,name):
        self.status = ALIVE
        self.direction = UP
        self.x = START_X
        self.y = START_Y
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.name = name
        self.image_pack = ['data/pright2.png', 'data/pdown2.png', 'data/pleft2.png', 'data/pup2.png']
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()# @UndefinedVariable
            i = []
            i.append(temp.subsurface(0,0,128,128))
            i.append(temp.subsurface(128,0,128,128))
            i.append(temp.subsurface(256,0,128,128))
            i.append(temp.subsurface(384,0,128,128))
            self.images.append(i)
            
        self.moving = [0,0,0,0]
        
        self.casted = 0
    def move(self):
        if self.moving[RIGHT]==1:
            self.direction=RIGHT
            self.x+=PLAYER_SPEED
        if self.moving[DOWN]==1:
            self.direction=DOWN
            self.y+=PLAYER_SPEED
        if self.moving[LEFT]==1:
            self.direction=LEFT
            self.x-=PLAYER_SPEED
        if self.moving[UP]==1:
            self.direction=UP
            self.y-=PLAYER_SPEED
            
        #границы окна
        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDHT - 128: self.x = SCREEN_WIDHT - 128
        if self.y >= SCREEN_HEIGHT - 128: self.y = SCREEN_HEIGHT - 128
        
        pass
    
    def render(self,screen):
        screen.blit(self.images[self.direction][self.status], (self.x,self.y))
        pass
    
    def render_ui(self,screen):
        screen.blit(pygame.image.load("data/hpbar.png"),(self.x, self.y+128))
        
        m = 0
        z = self.hp // 5
        while m<z:
            if m == 0:
                screen.blit(pygame.image.load("data/hptick.jpg"),(self.x+4+m*6, self.y+132))
            else:
                screen.blit(pygame.image.load("data/hptick.jpg"),(self.x+3+m*6, self.y+132))
            m += 1
        pass
        m = 0
        z = self.mp // 5
        while m<z:
            if m == 0:
                screen.blit(pygame.image.load("data/mtick.jpg"),(self.x+4+m*6, self.y+137))
            else:
                screen.blit(pygame.image.load("data/mtick.jpg"),(self.x+3+m*6, self.y+137))
            m += 1
    
    def death(self):
        self.hp = 0
        self.status = DEAD 
            
    def tick(self):
        if self.status != DEAD:
            self.mp += MP_REG
            self.hp += HP_REG
            if self.mp > MAX_MP:
                self.mp = MAX_MP
            if self.hp > MAX_HP:
                self.hp = MAX_HP
            if pygame.time.get_ticks() >= self.casted + 700 and pygame.time.get_ticks() < self.casted + 1000: 
                self.status = ALMOST_RELOADED
            if pygame.time.get_ticks() >= self.casted + 1000: 
                self.status = ALIVE