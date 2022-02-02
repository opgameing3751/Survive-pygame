
import math
import pygame, time, random, sys
mainClock = pygame.time.Clock()

pygame.init()
#jam
wn_width = 600
wn_height = 600
wn = pygame.display.set_mode((wn_width, wn_height))
icon = pygame.image.load("other sprites/xander.png")
pygame.display.set_icon(icon)
pygame.display.set_caption('idk yet')
finished_time = 0


#sprites
bg = pygame.image.load('other sprites/bg.png')
char1 = pygame.image.load('player\Player-main.png')
char = pygame.transform.scale(char1, (50, 50))

left_b = 600
right_b = 600
clockspeed = 60
def gameclockup():
    global clockspeed
    clockspeed = (30 + clockspeed)
def gameclockdown():
    global clockspeed
    clockspeed = (clockspeed - 30)

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
        self.rect.x = self.rect.x - 5000
        self.rect.y = self.rect.y - 5000
    def update(self):
        self.mouse = pygame.mouse.get_pos()
        
      
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = +10
            enemy1X[i] += 15
        elif keystate[pygame.K_d]:
            self.speedx = -10
            enemy1X[i] -= 15
        else:
            self.speedx = 0

        if keystate[pygame.K_w]:
            self.speedy = +10
            enemy1Y[i] += 15

        elif keystate[pygame.K_s]:
            self.speedy = -10
            enemy1Y[i] -= 15
        
        else:
            self.speedy = 0
            


        if keystate[pygame.K_UP]:
            print("game clock up")
            gameclockup()
        if keystate[pygame.K_DOWN]:
            print("game clock down")
            gameclockdown()

        

        
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy


        #if int(self.speedx) < 600:
        #    self.speedx = 600
        #elif int(self.speedy) < 600:
        #    self.speedy = 600
        

#Enemy
alive_enemies = 6
Enemyimg1 = []
enemy1X = []
enemy1Y = []
num_of_enemies = 17

for i in range(num_of_enemies):
    player = Player() 
    Enemyimg1.append(pygame.image.load('badthings that kill/badthing.png'))
    enemy1Y.append(random.randint(-200, 200))
    enemy1X.append(random.randint(-200, 200))
    
    print("enemy spawned")
        
def update_display():
    global end, start
    end = time.time()
    
    finished_time = (end - start)
    wn.blit(bg, (player.rect.x, player.rect.y))
    frametime = font.render(f'Frame time {finished_time}',True,(255, 255, 255))
    wn.blit(text, (0,0))
    wn.blit(coords, (0,20))
    
    wn.blit(frametime, (0,40))
    
    
def enemy(x, y, i):
    for i in range(num_of_enemies):
        wn.blit(Enemyimg1[i], (x, y))
    
def game_loop():
    global clockspeed
    player = Player()

    while True:
        global playerx, playery, text, font, coords, frametime, start
        start = time.time()
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                quit()
        playerx = player.rect.x
        playery = player.rect.y
        player.update()
        font = pygame.font.Font(None,30)
        text = font.render(f'clock speed is {clockspeed}',True,(255, 255, 255))
        coords = font.render(f'Coords x,{player.rect.x} y,{player.rect.y}',True,(255,255,255))
        
        [playercoordsX, playercoordsY] = player.mouse
        
        update_display()
        wn.blit(player.image, (player.mouse))

        for i in range(num_of_enemies):
            if playercoordsX > enemy1X[i]:
                enemy1X[i] += 4
            if playercoordsX < enemy1X[i]:
                enemy1X[i] -= 4
            if playercoordsY > enemy1Y[i]:
                enemy1Y[i] += 4
            if playercoordsY < enemy1Y[i]:
                enemy1Y[i] -= 4
            enemy(enemy1X[i], enemy1Y[i], i)

            if enemy1X[i]
                
        print(enemy1Y[i])
            
        


        #wn.blit(char, (300, 300))
        pygame.display.update()
        #badthings()
        
        
        mainClock.tick(clockspeed)





    




game_loop()
