'''Sheep and Wolves
April 10, 2018'''

import random

WHITE = color(255,255,255)
BLACK = color(0,0,0)
BLUE = color(0,0,255)
RED = color(255,0,0)
GREEN = color(0,102,0)
BROWN = color(102,51,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)

colors = [WHITE,BLUE,RED,YELLOW,PURPLE]

patchSize = 10

class Sheep:
    def __init__(self,col):
        self.x = random.randint(0,600)
        self.y = random.randint(0,600)
        self.col = col
        self.energy = 20
        self.move = 3 #how far they can move
        
    def update(self,sheepList):
        self.x += random.randint(-self.move,self.move)
        self.y += random.randint(-self.move,self.move)
        self.energy -= 1
        patchx, patchy = patchNum(self.x,self.y)
        if not grass[patchx*(600/patchSize)+patchy].eaten:
            grass[patchx*(600/patchSize)+patchy].eaten = True
            self.energy += patch.energy
        #reproduce
        if self.energy >= 50:
            self.energy = 20
            sheepList.append(Sheep(self.col))
        fill(self.col)
        en = map(self.energy,0,100,0,20)
        ellipse(self.x,self.y,en,en)
        
class Patch:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.eaten = False
        self.col = GREEN
        self.energy = 5
        
    def update(self):
        if self.eaten:
            self.col = BROWN
            if random.random()<0.5:
                self.eaten = False
        else:
            self.col=GREEN
        
        fill(self.col)
        rect(self.x,self.y,patchSize,patchSize)
        
def setup():
    global sheepList,grass
    size(600,600)
    noStroke()
    grass = [Patch(x,y) for x in range(0,600,patchSize) \
             for y in range(0,600,patchSize)]
    
    sheepList = []
    for x in range(20):
        col = random.choice(colors)
        sheepList.append(Sheep(col))
    
def draw():
    background(GREEN)
    for patch in grass:
        patch.update()
    for sheep in sheepList:
        sheep.update(sheepList)
        if sheep.energy <= 0: 
            sheepList.remove(sheep)
        
def patchNum(x,y):
    xmult = x // patchSize
    ymult = y // patchSize
    return xmult,ymult