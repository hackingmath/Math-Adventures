'''Catenary Question
Length of Chain: 80 m
Height of end poles: 50 m
height of lowest point on chain: 20m from ground.
How far apart are the poles?
July 20, 2018'''

from slider import Slider
from math import cosh


scl = 10 #every x- and y-value will be multiplied by scl
pole_height = 50
vertex_height = 20
diff_height = pole_height - vertex_height

'''Catenary equation is 
y = a * cosh(x/a)
'''

#initialize slider for a
slider1 = Slider(0,30,1) 
points = []
targ,targy = 0,0 #beginning values

def setup():
    size(600,600)
    slider1.position(20,20)
    
def draw():
    global points,targ,targy
    background(255)
    a = slider1.value()
    #translate to the base of the catenary
    translate(width/2,height-50)
    #draw "ground"
    line(-300,0,300,0)
    #map a to the mouse
    #a = map(mouseX,0,600,0.1,20)
    
    slider1.label = 'a'
    #start at left side of screen
    x = -30
    points = [] #empty the points list
    while x < 30: #go up to right side of screen
        y = f(x,a) #calculate y
        points.append([x,y]) #add point to list
        #if the point is at the desired height:
        if abs(diff_height - y) < 0.5:
            targ = x #save that x-value
            targy = y
        x += 0.1
    #graph the catenary
    graphPoints(points)
    
    #draw the poles
    line(targ*scl,0,targ*scl,-targy*scl)
    ellipse(targ*scl,-targy*scl,10,10) #intersection point
    line(-targ*scl,0,-targ*scl,-targy*scl)
    ellipse(-targ*scl,-targy*scl,10,10) #intersection point
    println("distance: "+ str(2*targ))
    println("height: "+str(diff_height+f(0,a)))
    fill(255,0,0)
    textSize(18)
    text(str(2*integral(f,a,targ,100)),-100,-300)
    
def f(x,a):
    try:
        return a * cosh(x/float(a))
    except ZeroDivisionError:
        return a * cosh(x/float(a+0.1))
    
def graphPoints(pointList):
    '''Graphs points in pointList using segments'''
    for i,pt in enumerate(pointList):
        if i<len(pointList)-1:
            line(pt[0]*scl,-pt[1]*scl,pointList[i+1][0]*scl,-pointList[i+1][1]*scl)

def integral(f,a,endingx,number_of_steps):
    '''Returns the arc length between a and b'''
    global targ
    sum_of_length = 0
    step_sz = endingx/float(number_of_steps)
    x = 0
    while x < endingx:
        newlength = dist(x,f(x,a),x+step_sz,f(x+step_sz,a))
        sum_of_length += newlength
        x += step_sz
    return sum_of_length
    
