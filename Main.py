
from turtle import up
import pygame, time, random, sys
mainClock = pygame.time.Clock()

pygame.init()

wn_width = 600
wn_height = 600
wn = pygame.display.set_mode((wn_width, wn_height))
icon = pygame.image.load("other sprites/xander.png")
pygame.display.set_icon(icon)
pygame.display.set_caption('idk yet')




#sprites
bg = pygame.image.load('other sprites/bg.png')
char1 = pygame.image.load('player\Player-main.png')
char = pygame.transform.scale(char1, (50, 50))

left_b = 600
right_b = 600



class Player:
    def __init__(self):
        self.image = char
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = int(wn_width * 0.5)
        self.rect.y = int(wn_height * 0.5)

        self.speedx = 0
        self.speedy = 0

    def update(self):
        print(self.speedx)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = +10
            
        elif keystate[pygame.K_d]:
            self.speedx = -10
            
        elif keystate[pygame.K_w]:
            self.speedy = +10
        
        elif keystate[pygame.K_s]:
            self.speedy = -10
            if keystate[pygame.K_d]:
                self.speedx = -10
                self.speedy = -10

        else:
            if self.speedy < 0:
                self.speedy = (self.speedy - 1)
            if self.speedx < 0:
                self.speedx = (self.speedx - 1)
            if self.speedy > 0:
                self.speedy = (self.speedy - 1)
            if self.speedx > 0:
                self.speedx = (self.speedx - 1)
            else:
                self.speedx = 0
                self.speedy = 0 


        

        #

        
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy


        #if int(self.speedx) < 600:
        #    self.speedx = 600
        #elif int(self.speedy) < 600:
        #    self.speedy = 600
        

def game_loop():
    
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                quit()
        
        player.update()
        wn.blit(bg, (player.rect.x, player.rect.y))
        wn.blit(player.image, (300,300))
        #wn.blit(char, (300, 300))
        pygame.display.update()
        mainClock.tick(30)
game_loop()
