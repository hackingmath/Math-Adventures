#Graphing program from Chapter 4 of Math Adventures with Python

import pygame
import time
from random import randint, uniform
from math import pi, sqrt, cos, sin, atan2

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

width,height = 600,600
#Origin is center of screen by default. Can be changed
origin = [width/2,height/2]

#set the range of x-values
xmin,xmax = -10,10

#set the range of y-values
ymin,ymax = -10,10

#calculate the scale of units in pixels
rangex = xmax - xmin
rangey = ymax - ymin

xscl,yscl = width/rangex, -height/rangey

def convert_coords(x,y):
    """Translates and scales coordinates for plotting"""
    return origin[0]+x*xscl,origin[1]+y*yscl

def draw_grid():
    #blue lines
    for i in range(xmin,xmax+1):
        pygame.draw.line(screen, CYAN, convert_coords(i,ymin),convert_coords(i,ymax),3)
    for j in range(ymin,ymax+1):
        pygame.draw.line(screen, CYAN, convert_coords(xmin,j),convert_coords(xmax,j),3)
    #axes
    pygame.draw.line(screen, BLACK, convert_coords(xmin, 0), convert_coords(xmax, 0), 3)
    pygame.draw.line(screen, BLACK, convert_coords(0,ymin), convert_coords(0,ymax), 3)

def f(x):
    return x**2 - 4

def draw_function(fn = f):
    x = xmin
    while x <= xmax:
        pygame.draw.line(screen, RED, convert_coords(x,fn(x)), convert_coords((x+0.1),fn(x+0.1)), 3)
        x+=0.1

# set up display
pygame.init()
screen = pygame.display.set_mode([width, height])

#in case you use fonts:
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 72)

pygame.display.set_caption('Graphing Functions') #add your own caption!
FPS = 60  # frames per second
clock = pygame.time.Clock()

counter = 0 #frame count

# loop until user clicks the close button
done = False

#Rendering the Game
xpos,ypos = 300,300

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if pygame window is closed by user
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xpos -= 20
    if keys[pygame.K_RIGHT]:
        xpos += 20

    if keys[pygame.K_p]:
        if FPS == 60:
            FPS = 300  #faster display
        else:
            FPS = 60
    # fill the screen with background color
    screen.fill(WHITE)

    draw_grid()
    draw_function()
    #pygame.draw.polygon(screen, WHITE, [(100, 200), (xpos,ypos), (524, 307), (500, 200)], 0)
    # pygame.draw.rect(screen, WHITE, [xpos,ypos, 150,200])
    # pygame.draw.line(screen, GREEN, [100,100],[200,300],3)
    # pygame.draw.circle(screen,RED,[400,100],50)

    counter += 1

    pygame.display.update()

    # for saving screenshots:
    # if counter %5 == 0:
    # capture(screen, 'Capture{}.png'.format(counter), (0, 0), (600, 600))
    clock.tick(FPS)
pygame.quit()
