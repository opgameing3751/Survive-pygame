
from dis import dis
import math
from turtle import distance, up
import pygame, time, random, sys
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry('250x150')
root.title('Widgets Tutorial')

root.mainloop()

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
running = True
mousecodx = 0
mousecody = 0
health = 1000
warn = 0
distanceasto = 600
distance = 600
on_screen_enemy_count = 0
on_screen_astro_count = 0
updatespertick = 0
#sprites
bg = pygame.image.load('other sprites/bg.png')
char1 = pygame.image.load('player\Player-main.png')
char = pygame.transform.scale(char1, (50, 50))
astro1 = pygame.image.load('astros/astro1.png')
astro2 = pygame.image.load('astros/astro2.png')
astro3 = pygame.image.load('astros/astro3.png')
almost_dead_screen = pygame.image.load("other sprites/almost dead screen.png")
startgameimg = pygame.image.load('other sprites\start.png')
left_b = 600
right_b = 600
clockspeed = 60

def gameclockup():
    global clockspeed
    clockspeed = (30 + clockspeed)
def gameclockdown():
    global clockspeed
    clockspeed = (clockspeed - 30)
startgame = True


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
            
            for i in range(num_of_enemies):
                enemy1X[i] += 10
            for i in range(num_of_astro):
                astox[i] += 10
        elif keystate[pygame.K_d]:
            self.speedx = -10
            for i in range(num_of_enemies):
                enemy1X[i] -= 10
            for i in range(num_of_astro):
                astox[i] -= 10
        else:
            self.speedx = 0

        if keystate[pygame.K_w]:
            self.speedy = +10
            for i in range(num_of_enemies):
                enemy1Y[i] += 10
            for i in range(num_of_astro):
                astoy[i] += 10
        elif keystate[pygame.K_s]:
            self.speedy = -10
            for i in range(num_of_enemies):
                enemy1Y[i] -= 10
            for i in range(num_of_astro):
                astoy[i] -= 10
        elif keystate[pygame.K_SPACE]:
            astrospawn()

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
        

#randomobject
astoimg = []
astox = []
astoy = []
distanceasto = []
num_of_astro = 100
def astrospawn():
    
    for i in range(num_of_astro):
        
        astrorand = (random.randint(1, 3))
        if astrorand == 1:
            astoimg.append(astro1)
        elif astrorand == 2:
            astoimg.append(astro2)
        elif astrorand == 3:
            astoimg.append(astro3)
        astox.append(random.randint(-2000, 2500))
        astoy.append(random.randint(-2000, 2500))
        distanceasto.append(0)

#Enemy
alive_enemies = 6
Enemyimg1 = []
enemy1X = []
enemy1Y = []
distance = []
num_of_enemies = 200

for i in range(num_of_enemies):
    player = Player()
    enemyimg = pygame.image.load('badthings that kill/badthing.png').convert_alpha()
    Enemyimg1.append(pygame.transform.scale(enemyimg, (50, 50)))
    enemy1Y.append(random.randint(-2000, 2500))
    enemy1X.append(random.randint(-2000, 2500))
    distance.append(0)
    
    print("enemy spawned")


def update_display():
    global end, start, on_screen_enemy_count, updatespertick
    updatespertick += 1
    health_display = font.render(f'Health: {health}',True,(255,255,255))
    wn.blit(bg, (0,0))
    wn.blit(text, (0,0))
    wn.blit(coords, (0,20))
    wn.blit(mousecoords, (0,40))
    wn.blit(health_display, (0, 120))
    wn.blit(enemyscreen, (0, 80))
    wn.blit(astroscreen, (0,100))
    wn.blit(updates, (0, 140))
    on_screen_enemy_count = 0
    updatespertick = 0
    end = time.time()
    finished_time = (end - start)
    frametime = font.render(f'Frame time {finished_time}',True,(255, 255, 255))
    wn.blit(frametime, (0,60))
    
    
def enemy(x, y, i):
    global updatespertick
    for i in range(num_of_enemies):
        if distance[i] <= 600:
            updatespertick += 1
            wn.blit(Enemyimg1[i], (x, y))

def on_screen_update():
    global on_screen_enemy_count, on_screen_astro_count
    for i in range(num_of_enemies):
        if distance[i] <= 600:
            on_screen_enemy_count += 1
    for i in range(num_of_astro):
        if distanceasto[i] <= 600:
            on_screen_astro_count += 1

def astro_update(x, y, i):
    global updatespertick
    for i in range(num_of_astro):
        if distanceasto[i] <= 600:
            updatespertick += 1
            wn.blit(astoimg[i], (x,y))

def game_over():
    global updatespertick
    updatespertick += 1
    global running
    time.sleep(1)
    running = False
    
def game_loop():
    global clockspeed
    player = Player()
def almost_Dead():
    global updatespertick
    updatespertick += 1
    wn.blit(almost_dead_screen, (0,0))
astrospawn()
while running:
    global playerx, playery, text, font, coords, frametime, start, mousecoords
    
    start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            running = False
    
    playerx = player.rect.x
    playery = player.rect.y
    updatespertick += 1
    player.update()
    font = pygame.font.Font(None,30)
    text = font.render(f'clock speed is {clockspeed}',True,(255, 255, 255))
    coords = font.render(f'Coords x,{player.rect.x} y,{player.rect.y}',True,(255,255,255))
    astroscreen = font.render(f'Astros rendered {on_screen_astro_count}',True,(255,255,255))
    enemyscreen = font.render(f'Enemys rendered {on_screen_enemy_count}',True,(255,255,255))
    updates = font.render(f'updates per game tick {updatespertick}',True,(255,255,255))
    [playercoordsX, playercoordsY] = player.mouse
    mousecodx = playercoordsX - player.rect.x - 300
    mousecody = playercoordsY - player.rect.y - 300
    mousecoords = font.render(f'mouse Coords x,{mousecodx} y,{mousecody}',True,(255,255,255))
        
    
        
    update_display()
    wn.blit(player.image, (player.mouse))

    
    if health <= 0:
        game_over()
    if health <= 30:
        warn = 1
    if warn == 1:
        almost_Dead()

    for i in range(num_of_enemies):
        if playercoordsX > enemy1X[i]:
            enemy1X[i] += 5
        if playercoordsX < enemy1X[i]:
            enemy1X[i] -= 5
        if playercoordsY > enemy1Y[i]:
            enemy1Y[i] += 5
        elif playercoordsY < enemy1Y[i]:
            enemy1Y[i] -= 5

        
       
        enemy(enemy1X[i], enemy1Y[i], i)
        
        distance[i] = math.sqrt ((math.pow(enemy1X[i]-playercoordsX,2)) + (math.pow(enemy1Y[i]-playercoordsY,2)))
        

      
        distanceX = enemy1X[i] - playercoordsX
        distanceY = enemy1Y[i] - playercoordsY
            
        if distance[i] < 35:
            if distanceX < -35:
                enemy1X[i] -= 2
                
            if distanceX < -10:
                enemy1X[i] -= 10
               
            if distanceX > 35:
                enemy1X[i] += 2
                
            if distanceX > 10:
                enemy1X[i] += 10
            if distanceY < -35:
                enemy1Y[i] -= 2
                
            if distanceY < -10:
                enemy1Y[i] -= 10
            if distanceY > 35:
                enemy1Y[i] += 2
                
            if distanceY > 10:
                enemy1Y[i] += 10

        if distance[i] < 35:
            health -= 1
        if distance[i] > 2000:
            enemy1Y[i] = random.randint(-2000, 2000)
            enemy1X[i] = random.randint(-2000, 2000)

    for i in range(num_of_astro):
        astrodisx = astox[i] - playercoordsX
        astrodisy = astoy[i] - playercoordsY
        
        distanceasto[i] = math.sqrt ((math.pow(astox[i]-playercoordsX,2)) + (math.pow(astoy[i]-playercoordsY,2)))    
        if distanceasto[i] < 90:
            updatespertick += 1
            if astrodisx < -75:
                astox[i] -= 2
            if astrodisx < -50:
                astox[i] -= 10
            if astrodisx > 75:
                astox[i] += 2
            if astrodisx > 50:
                astox[i] += 10
            
            if astrodisy < -75:
                astoy[i] -= 2
            if astrodisy < -50:
                astoy[i] -= 10
            if astrodisy > 75:
                astoy[i] += 2
            if astrodisy > 50:
                astoy[i] += 10
        astro_update(astox[i], astoy[i], i)

        
        if distanceasto[i] > 2000:
            astoy[i] = random.randint(-2000, 2000)
            astox[i] = random.randint(-2000, 2000)
            #print(distance)
        
    for i in range(num_of_astro):
        astro_enemy = math.sqrt ((math.pow(astox[i]-enemy1X[i],2)) + (math.pow(astoy[i]-enemy1Y[i],2)))

        astro_enemyX = astox[i] - enemy1X[i]
        astro_enemyY = astoy[i] - enemy1Y[i]
        
        if astro_enemy < 90:
            updatespertick += 1
            if astro_enemyX < -35:
                astox[i] -= 10
                
            if astro_enemyX < -10:
                astox[i] -= 10
               
            if astro_enemyX > 35:
                astox[i] += 2
                
            if astro_enemyX > 10:
                astox[i] += 10


            if astro_enemyY < -35:
                astoy[i] -= 2
                
            if astro_enemyY < -10:
                astoy[i] -= 10

            if astro_enemyY > 35:
                astoy[i] += 2
                
            if astro_enemyY > 10:
                astoy[i] += 10



        #wn.blit(char, (300, 300))
        
    pygame.display.update()
        #badthings()
    on_screen_astro_count = 0
    on_screen_update()
    
    mainClock.tick(clockspeed)
    




    




game_loop()
