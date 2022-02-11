
from dis import dis
from email.mime import image
import math
from turtle import distance, up
import pygame, time, random, sys
from pygame.locals import *
from tkinter import *
from PIL import Image, ImageTk
#import psutil, os

health = 0
num_of_astro = 0
num_of_enemies = 0
running = 0
FOV = 0
SCORE = 0

def startgame():
    global num_of_astro, num_of_enemies, running
    running = 1
    if num_of_astro == 0:
        num_of_astro = 100
    if num_of_enemies == 0:
        num_of_enemies = 500
    if health == 0:
        health == 100
<<<<<<< HEAD
    
=======
    root.quit()
>>>>>>> 00c7b8c9221cd6c953a9f14b5f6bfd38bfa43953

def easy():
    global health, num_of_astro, num_of_enemies, FOV, running, warning
    health = 100
    num_of_astro = 100
    num_of_enemies = 100
    warning = 30
    FOV = 5000
    running = 1
<<<<<<< HEAD
    startgame()
=======
    top.quit()
>>>>>>> 00c7b8c9221cd6c953a9f14b5f6bfd38bfa43953
def normal():
    global health, num_of_astro, num_of_enemies, FOV, running, warning
    health = 200
    num_of_astro = 100
    num_of_enemies = 500
    warning = 50
    FOV = 1000
    running = 1
<<<<<<< HEAD
    startgame()
=======
    top.quit()
>>>>>>> 00c7b8c9221cd6c953a9f14b5f6bfd38bfa43953
def hard():
    global health, num_of_astro, num_of_enemies, FOV, running, warning
    health = 1000
    num_of_astro = 100
    num_of_enemies = 1000
    warning = 300
    FOV = 1000
    running = 1
<<<<<<< HEAD
    startgame()
=======
    top.quit()
>>>>>>> 00c7b8c9221cd6c953a9f14b5f6bfd38bfa43953
def you_dumb():
    global health, num_of_astro, num_of_enemies, FOV, running, warning
    health = 100
    num_of_astro = 100
    num_of_enemies = 5000
    warning = 30
    FOV = 500
    running = 1
<<<<<<< HEAD
    startgame()
=======
    top.quit()
>>>>>>> 00c7b8c9221cd6c953a9f14b5f6bfd38bfa43953
    
def top():
    global top
    top=Toplevel()
    top.geometry('300x250')
    top.title("settings")
    v = StringVar()
    v.set("L")
    choice1 = Radiobutton(top, text='easy', value=1, variable=v, command=easy)
    choice2 = Radiobutton(top, text='normal', value=2, variable=v, command=normal)
    choice3 = Radiobutton(top, text='hard', value=3, variable=v, command=hard)
    choice4 = Radiobutton(top, text='your dumb', value=4, variable=v, command=you_dumb)
    choice1.grid(row=2, column=0)
    choice2.grid(row=3, column=0)
    choice3.grid(row=4, column=0)
    choice4.grid(row=5, column=0)

def dead():
    global SCORE
    pat = Tk()
    pat.geometry('600x600')
    pat.title('Widgets Tutorial')
    dead_screen_png = Image.open("other sprites\you dead screen.png")
    dead_screen = ImageTk.PhotoImage(dead_screen_png)
    dead_screen1 = Label(pat, image=dead_screen)
    dead_screen1.place(x=-2, y=-2)
    scorenum = Label(pat, text=SCORE)
    scorenum.place(x=300, y=300)
    pat.mainloop()
root = Tk()

root.geometry('600x600')
root.title('Widgets Tutorial')
background = PhotoImage(file=r'other sprites\start.png')
background1 = Label(root, image=background)
background1.place(x=-2, y=-2)

startbuttonpng = PhotoImage(file=r'other sprites/playbutton.png')

startbutton = Button(root, image=startbuttonpng, command=top)
startbutton.place(x=68, y=300)



root.mainloop()

mainClock = pygame.time.Clock()

pygame.init()
#jam
wn_width = 1920
wn_height = 1080
wn = pygame.display.set_mode((wn_width, wn_height))
icon = pygame.image.load("other sprites/xander.png")
pygame.display.set_icon(icon)
pygame.display.set_caption('idk yet')
finished_time = 0

mousecodx = 0
mousecody = 0

warn = 0
fps = 0
distanceasto = 600
distance = 600
on_screen_enemy_count = 0
on_screen_astro_count = 0
updatespertick = 0
#sprites
bg = pygame.image.load('other sprites/bg.png').convert()
char1 = pygame.image.load('player\Player-main.png')
char = pygame.transform.scale(char1, (50, 50))
astro1 = pygame.image.load('astros/astro1.png')
astro2 = pygame.image.load('astros/astro2.png')
astro3 = pygame.image.load('astros/astro3.png')
astro4 = pygame.image.load('astros/astro4.png')
astro5 = pygame.image.load('astros/astro5.png')
astro6 = pygame.image.load('astros/astro6.png')
astro7 = pygame.image.load('astros/astro7.png')
astro8 = pygame.image.load('astros/astro8.png')
astro9 = pygame.image.load('astros/astro9.png')
astro10 = pygame.image.load('astros/astro10.png')
astro11 = pygame.image.load('astros/astro11.png')
astro12 = pygame.image.load('astros/astro12.png')
astro13 = pygame.image.load('astros/astro13.png')
astro14 = pygame.image.load('astros/astro14.png')
astro15 = pygame.image.load('astros/astro15.png')
astro16 = pygame.image.load('astros/astro16.png')
almost_dead_screen = pygame.image.load("other sprites/almost dead screen.png").convert_alpha()

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

def astrospawn():
    
    for i in range(num_of_astro):
        
        astrorand = (random.randint(1, 16))
        if astrorand == 1:
            astoimg.append(astro1)
        elif astrorand == 2:
            astoimg.append(astro2)
        elif astrorand == 3:
            astoimg.append(astro3)
        elif astrorand == 4:
            astoimg.append(astro4)
        elif astrorand == 5:
            astoimg.append(astro5)
        elif astrorand == 6:
            astoimg.append(astro6)
        elif astrorand == 7:
            astoimg.append(astro7)
        elif astrorand == 8:
            astoimg.append(astro8)
        elif astrorand == 9:
            astoimg.append(astro9)
        elif astrorand == 10:
            astoimg.append(astro10)
        elif astrorand == 11:
            astoimg.append(astro11)
        elif astrorand == 12:
            astoimg.append(astro12)
        elif astrorand == 13:
            astoimg.append(astro13)
        elif astrorand == 14:
            astoimg.append(astro14)
        elif astrorand == 15:
            astoimg.append(astro15)
        elif astrorand == 16:
            astoimg.append(astro16)
        
        astox.append(random.randint(-2000, 2500))
        astoy.append(random.randint(-2000, 2500))
        distanceasto.append(0)

#Enemy
alive_enemies = 6
Enemyimg1 = []
enemy1X = []
enemy1Y = []
distance = []


for i in range(num_of_enemies):
    player = Player()
    enemyimg = pygame.image.load('badthings that kill/badthing.png').convert_alpha()
    Enemyimg1.append(pygame.transform.scale(enemyimg, (50, 50)))
    enemy1Y.append(random.randint(-4000, 4500))
    enemy1X.append(random.randint(-4000, 4500))
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
    wn.blit(fpsrender, (0, 160))
    on_screen_enemy_count = 0
    updatespertick = 0
    end = time.time()
    finished_time = (end - start)
    frametime = font.render(f'Frame time {finished_time}',True,(255, 255, 255))
    wn.blit(frametime, (0,60))
    
    


def on_screen_update():
    global on_screen_enemy_count, on_screen_astro_count
    for i in range(num_of_enemies):
        if distance[i] <= 600:
            on_screen_enemy_count += 1
    for i in range(num_of_astro):
        if distanceasto[i] <= 600:
            on_screen_astro_count += 1

def game_over():
    global updatespertick
    updatespertick += 1
    global running
    time.sleep(1)
    running = 0
    dead()

    
astrospawn()
while running == 1:
    global playerx, playery, text, font, coords, frametime, start, mousecoords, fpsrender
    fps_start = time.time()
    start = time.time()
    SCORE += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = 0
            print('game quit')
    
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
    fpsrender = font.render(f'FPS {fps}',True,(255,255,255))
    [playercoordsX, playercoordsY] = player.mouse
    mousecodx = playercoordsX - player.rect.x - 300
    mousecody = playercoordsY - player.rect.y - 300
    mousecoords = font.render(f'mouse Coords x,{mousecodx} y,{mousecody}',True,(255,255,255))
    if pygame.mouse.get_visible():
                pygame.mouse.set_visible(False)
    
        
    update_display()
    wn.blit(player.image, (player.mouse))

    
    if health <= 0:
        game_over()
    if health <= warning:
        warn = 1
    if warn == 1:
        updatespertick += 1
        wn.blit(almost_dead_screen, (0,0))

    for i in range(num_of_enemies):
        if playercoordsX > enemy1X[i]:
            enemy1X[i] += 5
        if playercoordsX < enemy1X[i]:
            enemy1X[i] -= 5
        if playercoordsY > enemy1Y[i]:
            enemy1Y[i] += 5
        elif playercoordsY < enemy1Y[i]:
            enemy1Y[i] -= 5

        
       
    
        
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
        if distance[i] > 4000:
            enemy1Y[i] = random.randint(-4000, 4000)
            enemy1X[i] = random.randint(-4000, 4000)
            
        if distance[i] <= FOV:
            updatespertick += 1
            wn.blit(Enemyimg1[i], (enemy1X[i], enemy1Y[i]))



        #enemy(enemy1X[i], enemy1Y[i], i)
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
        #astro_update(astox[i], astoy[i], i)
        if distanceasto[i] <= FOV:
            updatespertick += 1
            wn.blit(astoimg[i], (astox[i],astoy[i]))
        
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
    
    on_screen_astro_count = 0
    on_screen_update()
    fps_s = time.time() - start
    fps = 1. / fps_s
    mainClock.tick(clockspeed)
