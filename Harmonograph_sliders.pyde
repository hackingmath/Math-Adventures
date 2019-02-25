from __future__ import division

'''Grid for graphing'''

from slider import Slider
from math import e

#define all the sliders

slider1 = Slider(-6,6,PI/16)
slider2 = Slider(-6,6,3*PI/16)
slider3 = Slider(-6,6,13*PI/16)
slider4 = Slider(-6,6,PI)

slider5 = Slider(0,0.1,0.02)
slider6 = Slider(0,0.1,0.0318)
slider7 = Slider(0,0.1,0.02)
slider8 = Slider(0,0.1,0.02)

slider9 = Slider(1,10,2)
slider10 = Slider(1,10,6)
slider11 = Slider(1,10,1.002)
slider12 = Slider(1,10,3)

def setup():
    size(800,800)
    slider1.position(20,20)
    slider2.position(20,50)
    slider3.position(20,80)
    slider4.position(20,110)
    slider5.position(180,20)
    slider6.position(180,50)
    slider7.position(180,80)
    slider8.position(180,110)
    slider9.position(340,20)
    slider10.position(340,50)
    slider11.position(340,80)
    slider12.position(340,110)
    background(255)
    
rangex = 51
rangey = 51
xscl = 1 #600/rangex
yscl = 1 #-600/rangey
t = 0 

#Harmononograph constants:
p3 = 13*PI/16
p4 = PI

d1 = 0.02
d2 = .0315
d3 = .02
d4 = 0.02

f1 = 2
f2 = 6
f3 = 1.002
f4 = 3
    
def draw():
    #fill(0,10)
    global xscl, yscl,t
    #rect(0,0,width,height)
    background(255)
    p1 = slider1.value()
    p2 = slider2.value()
    p3 = slider3.value()
    p4 = slider4.value()
    
    d1 = slider5.value()
    d2 = slider6.value()
    d3 = slider7.value()
    d4 = slider8.value()
    
    f1 = slider9.value()
    f2 = slider10.value()
    f3 = slider11.value()
    f4 = slider12.value()
    
    #automatically oscillate these values
    f1 = 5 + 5*sin(t)
    f2 = 5 + 5*sin(2*t)
    
    translate(width/2,height/2)
    slider1.label = "p1"
    slider2.label = "p2"
    slider3.label = "p3"
    slider4.label = "p4"
    slider5.label = "d1"
    slider6.label = "d2"
    slider7.label = "d3"
    slider8.label = "d4"
    slider9.label = "f1"
    slider10.label = "f2"
    slider11.label = "f3"
    slider12.label = "f4"
    
    #graphFunction()
    stroke(0,0,255)
    strokeWeight(2)
    
    #fill list with points
    d = [harmo(i,f1,f2,f3,f4,p1,p2,p3,p4,d1,d2,d3,d4) for i in arange(-50,50,0.01)]
    #graph the points:
    graphPoints2(d)
    t += 0.0001 #increment time

    
def harmo(t,f1,f2,f3,f4,p1,p2,p3,p4,d1,d2,d3,d4):
    return [sin(f1*t + p1)*e**(-t*d1) + 100*sin(f2*t + p2)*e**(-t*d2),
        sin(f3*t + p3)*e**(-t*d3) + 100*sin(f4*t + p4)*e**(-t*d4)]

    
def graphPoints2(pointList):
    '''Graphs the points in a list using segments'''
    global xscl, yscl
    for i,p in enumerate(pointList):
        if i<len(pointList)-1:
            line(p[0]*xscl,p[1]*yscl,pointList[i+1][0]*xscl,pointList[i+1][1]*yscl)


def arange(start,stop,step):
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output




    
