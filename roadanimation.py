# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
from pygame import mixer
import random
import math
import time

# Initialize game engine
pygame.init()


#MUSIC
#pygame.mixer.music.load('yeet.wav')



# Window
SIZE = (800, 600)
TITLE = "roads"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
BLACK = (0,0,0)
ROAD = (30,30,30)

GRAY = (140,140,140)
GREEN = (50, 125, 50)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)

#PICTURES
house = pygame.transform.scale(pygame.image.load('house.png'),(80,80))
callou = pygame.transform.scale(pygame.image.load('spedcallou.png'),(10,20))
car = pygame.transform.scale(pygame.image.load('car.png'),(20,15))
#roads

def drawroadvert(x,y,height):
    pygame.draw.rect(screen,GRAY,[x-8,y,66,height])
    pygame.draw.rect(screen,ROAD,[x,y,50,height])
    pygame.draw.line(screen,YELLOW,[x +23 ,y],[x+23,y+height])
    pygame.draw.line(screen,YELLOW,[x +25 ,y],[x+25,y+height])
    

def drawroadhor(x,y,length):
    pygame.draw.rect(screen,GRAY,[x,y-8,length,66])
    pygame.draw.rect(screen,ROAD,[x,y,length,50])
    pygame.draw.line(screen,YELLOW,[x ,y + 23],[x+length,y+23])
    pygame.draw.line(screen,YELLOW,[x ,y + 25],[x+length,y+25])


def drawintersection(x,y,corners):
    
    pygame.draw.rect(screen,ROAD,[x,y ,50,50])
    if corners[0]:
        pygame.draw.line(screen,WHITE,[x,y-2],[x+25,y-2],3) #top
    if corners[1]:
        pygame.draw.line(screen,WHITE,[x+51,y],[x+51,y+25],3) #right
    if corners[2]:
        pygame.draw.line(screen,WHITE,[x+23,y+51],[x+49,y+51],3) #bottom
    if corners[3]:
        pygame.draw.line(screen,WHITE,[x-2,y+23],[x-2,y+49],3) #left

def drawculdesac(x,y,side):
    
    startangle = 0
    
    if side == 0:
        pygame.draw.rect(screen,GREEN,[x-8,y-8,66,33])
    elif side == 1:
        startangle = math.pi * 3/2
        pygame.draw.rect(screen,GREEN,[x+25,y-8,33,66])
    elif side == 2:
        startangle = math.pi
        pygame.draw.rect(screen,GREEN,[x-8,y+25,66,33])
    elif side == 3:
        startangle = math.pi / 2
        pygame.draw.rect(screen,GREEN,[x-8,y-8,33,66])

    stopangle = startangle + math.pi
    pygame.draw.arc(screen,GRAY,[x-8,y-8,66,66],startangle,stopangle,8)
    pygame.draw.arc(screen,ROAD,[x,y,50,50],startangle,stopangle,25)
    


    
def drawhouse(x,y):
    hrect = [x,y,10,10]
    screen.blit(house,hrect)

def drawhouses(pts):
    for p in pts:
        drawhouse(p[0],p[1])

def drawperson(x,y):
    hrect = [x,y,10,10]
    screen.blit(callou,hrect)

def drawpeople(pts):
    for p in pts:
        drawperson(p[0],p[1])

def drawcar(x,y):
    hrect = [x,y,10,10]
    screen.blit(car,hrect)

def drawcars(pts):
    for p in pts:
        drawcar(p[0],p[1])


#Classes
path1 = [200,0,200,380] #down left
path2 = [227,380,227,-20] #up left
path3 = [250,430,525,430] #across bottom to right
path4 = [525,405,250,405] #across bottom to left
path5 = [550,200,550,380] #down right side
path6 = [577,380,577,200] #up right side
path7 = [800,152,603,152] #in from right
path8 = [600,177,800,177] #out to right side
path9 = [525,152,400,152] #top culdasac to left
path10 = [400,177,525,177] #top culdasac to right
path11 = [600,430,670,430] #right culdasac to right
path12 = [670,405,600,405] #right culdasac to left
path13 = [105,430,170,430] #left culdasac to right
path14 = [170,405,105,405] #left culdasac to left

paths = [path1,path2,path3,path4,path5,path6,path7,path8,path9,path10,path11,path12,path13,path14]
possiblepaths = [[path14,path3],[path2],[path6,path11],[path2,path14],[path4,path11],[path8,path9],[path9,path5],[path8],[path10],[path8,path5],[path12],[path4,path6],[path2,path3],[path13]]

cars = []
class Car(pygame.sprite.Sprite):
    
    posx = 0
    posy = 0
    path = []
    endroad = False
    makingturn = False
    
    
    def __init__(self, carpath):
        self.path = carpath
        self.posx = carpath[0]
        self.posy = carpath[1]
        
                
    def update(self):
        if not self.makingturn:
            oldx = self.posx
            oldy = self.posy
            if self.path[0] == self.path[2]:
                if self.path[1] > self.path[3]:
                    self.posy -= 5
                else:
                    self.posy += 5

                if self.posy > max(self.path[1],self.path[3]):
                    self.posy = max(self.path[1],self.path[3])
                if self.posy < min(self.path[1],self.path[3]):
                    self.posy = min(self.path[1],self.path[3])
            else:
                if self.path[0] > self.path[2]:
                    self.posx -= 5
                else:
                    self.posx += 5

                if self.posx > max(self.path[0],self.path[2]):
                    self.posx = max(self.path[0],self.path[2])
                if self.posx < min(self.path[0],self.path[2]):
                    self.posx = min(self.path[0],self.path[2])
            
            drawcar(self.posx,self.posy)

            if oldx == self.posx and oldy == self.posy:
                self.endroad = True
                self.changepath()
        else:
            self.posx += (self.path[0] - self.posx) / 6
            self.posy += (self.path[1] - self.posy) / 6
            if abs(self.posx - self.path[0]) < 2 and abs(self.posy - self.path[1]) < 2:
                self.posx = self.path[0]
                self.posy = self.path[1]
                self.makingturn = False
            drawcar(self.posx,self.posy)
            
    def changepath(self):
        if (self.path == path2 or self.path == path8):
            cars.remove(self)
            newcar()
        self.path = possiblepaths[paths.index(self.path)][random.randint(0,len(possiblepaths[paths.index(self.path)]) - 1)]
        self.makingturn = True

def newcar():
    cars.append(Car(paths[random.randint(0,13)]))
    
def makecars():
    cars.clear()
    cars.append(Car(path1))
    cars.append(Car(path3))
    cars.append(Car(path4))
    cars.append(Car(path5))
    cars.append(Car(path6))
    cars.append(Car(path7))
    cars.append(Car(path8))
    cars.append(Car(path9))
    cars.append(Car(path10))
    cars.append(Car(path11))
    cars.append(Car(path12))



        
# Game loop
done = False

makecars()

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

   

    # Drawing code
    ''' sky '''
    screen.fill(GREEN)

    
    
    drawroadhor(100,400,600) #250,400 > 550,450
    drawroadhor(400,150,600)
    drawroadvert(200,0,400) #200,0 > 250,400
    drawroadvert(550,200,200)
    drawintersection(200,400,[True,True,False,True]) #200,400 >250,450
    drawintersection(550,150,[False,True,True,True])
    drawintersection(550,400,[True,True,False,True])
    drawculdesac(100,400,3)
    drawculdesac(650,400,1)
    drawculdesac(400,150,3)


    drawhouses([[100,10],[100,150],[100,290]])
    drawhouses([[10,380],[100,470],[240,470],[380,470],[520,470],[660,470]])
    drawhouses([[710,380],[620,290],[710,220],[710,30],[570,30],[430,30],[430,250],[280,10],[280,150],[280,290]])


    for c in cars:
        c.update()

    

    pressed = pygame.key.get_pressed()
    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]
    space = pressed[pygame.K_SPACE]

    if space:
        makecars()

   
    
   

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
