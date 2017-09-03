# -*- coding: utf-8 -*-

import pygame
import time
import sys
import random

from pygame.locals import *
from Const import *
from Player import *
from pygame.examples.oldalien import PLAYER_SPEED
from Projective import *

pygame.font.init()
window = pygame.display.set_mode((100,100))

class Main():
    def __init__(self,screen):
        self.screen = screen       
        pygame.display.set_caption('Play') 
        self.player = Player('Name')
        self.projective = []
        self.background = pygame.image.load('background.jpg')
        self.running = True
        self.main_loop()

        pass
    
    
    def render(self):
        #прорисовка
        self.screen.blit(self.background,(0,0))
        self.player.render(screen)
        self.player.render_ui(screen)
        for i in self.projective:
            i.render(screen)
        pygame.display.flip()
        
        pass
        
    
    def main_loop(self):
        #основной цикл программы
        pygame.time.set_timer(USEREVENT+1, 100)
        while self.running == True:
            print(pygame.time.get_ticks())
            if self.player.status!=DEAD:
                self.player.move()
            for i in self.projective:
                i.move()
            self.render()
            self.handle_events()

        pass
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # @UndefinedVariable
                self.running = False
            elif event.type == USEREVENT+1:
                self.player.tick()
            #передвижение
            elif event.type == KEYDOWN:# @UndefinedVariable
                if event.key == K_RIGHT:# @UndefinedVariable
                    
                    self.player.moving = [1,0,0,0]
                if event.key == K_DOWN:# @UndefinedVariable
                    
                    self.player.moving = [0,1,0,0]
                if event.key == K_LEFT:# @UndefinedVariable
                    
                    self.player.moving = [0,0,1,0]
                if event.key == K_UP:# @UndefinedVariable
                    
                    self.player.moving = [0,0,0,1]
                if event.key == K_d:
                    if self.player.status != DEAD:
                        self.player.death()
                    else:
                        self.player.status = ALIVE
                if event.key == K_s:
                    if self.player.status != DEAD:
                        if self.player.mp >= FIRST_SKILL and self.player.status != SHOOT:
                            self.player.mp -= FIRST_SKILL
                            self.player.status = SHOOT
                            self.player.casted = pygame.time.get_ticks()
                            if self.player.direction == RIGHT:
                                self.projective.append(WaterBall(self.player.x+12, self.player.y, self.player.direction))
                            elif self.player.direction == DOWN:
                                self.projective.append(WaterBall(self.player.x, self.player.y+12, self.player.direction))
                            elif self.player.direction == LEFT:
                                self.projective.append(WaterBall(self.player.x-12, self.player.y, self.player.direction))
                            elif self.player.direction == UP:
                                self.projective.append(WaterBall(self.player.x, self.player.y-12, self.player.direction))
                if event.key == K_ESCAPE:
                    game.menu()
                    
            elif event.type == KEYUP:# @UndefinedVariable
                if event.key == K_RIGHT:# @UndefinedVariable
                    self.player.moving[RIGHT] = 0
                if event.key == K_DOWN:# @UndefinedVariable
                    self.player.moving[DOWN] = 0
                if event.key == K_LEFT:# @UndefinedVariable
                    self.player.moving[LEFT] = 0
                if event.key == K_UP:# @UndefinedVariable
                    self.player.moving[UP] = 0

        pass

class MainMenu():
    def __init__(self, lists = [250, 250, u'Game', (250,250,30), (250,30,250), 0]):
        self.lists = lists

        
    def render(self, area, font, num_list):
        for i in self.lists:
            if num_list == i[5]:
                area.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                area.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
        
    def menu(self):
        done = True
        font_menu = pygame.font.Font('fonts/TitilliumText22L003.otf', 50)
        list = 0
        
        while done:
            screen.fill((0,100,200))
            mp = pygame.mouse.get_pos()
            
            for i in self.lists:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+55:
                    list = i[5]
                if list == 0:
                    screen.blit(pygame.image.load("data/clicker.png"),(225, 260))
                if list == 1:
                    screen.blit(pygame.image.load("data/clicker.png"),(225, 360))
            self.render(screen, font_menu, list)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        sys.exit()
                    if e.key == 13:
                        if list == 0:
                            done = False
                        if list == 1:
                            sys.exit()
                    if e.key == K_UP:
                        if list > 0:
                            list -= 1
                    if e.key == K_DOWN:
                        if list < len(self.lists)-1:
                            list += 1
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if list == 0 and mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1]-100 and mp[1]<i[1]-55:
                        done = False
                    if list == 1 and mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+55:
                        sys.exit()
                
            window.blit(screen, [0,0])
            pygame.display.flip()
    
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIGHT))
lists = [(250, 250, u'Play', (250,250,30), (250,30,250), 0),
         (250, 350, u'Exit', (250,250,30), (250,30,250), 1)]
game = MainMenu(lists)
game.menu()
gm = Main(screen)
pygame.font.quit()
