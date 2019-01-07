'''Cloning Roger Antonsen's Rotating Triangles
Sketch 
October 7, 2018
added sliders January 7, 2019'''

from slider import Slider 
   
t = 0 #time variable
NUM_TRIS = 90
slider1 = Slider(0,20,0)
slider2 = Slider(1,120,1)

def setup():
    size(600,600)
    noFill()
    colorMode(HSB)
    strokeWeight(2)
    slider1.position(10,10)
    slider2.position(10,60);

def draw():
    background(255)
    global t
    offset = slider1.value();
    NUM_TRIS = int(slider2.value());
    slider1.label = "offset"
    slider2.label = "number"
    translate(width/2, height/2)
    for i in range(NUM_TRIS):
        rotate(TWO_PI/float(NUM_TRIS))
        pushMatrix() #save this orientation
        if NUM_TRIS != 1:
            translate(200,0)
        rotate(t/5.0+offset*TWO_PI*i/float(NUM_TRIS))#*360/NUM_TRIS))
        stroke(0)#3*i,255,255)
        strokeWeight(2)
        noFill()
        tri(100)
        popMatrix() #return to saved orientation
    t += 0.1
    
def tri(length):
    '''Draws an equilateral triangle
    around center of triangle'''
    triangle(0,-length,
             -length*sqrt(3)/2, length/2.0,
             length*sqrt(3)/2, length/2.0)
