#rotatingTriangles.pyde
#from Chapter 5 of Math Adventures with Python

def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)

t = 0

def draw():
    global t
    background(255)#white
    translate(width/2,height/2)
    for i in range(90):
        #space the triangles evenly
        #around the circle
        rotate(radians(360/90))
        pushMatrix() #save this orientation
        #go to circumference of circle
        translate(200,0)  
        #spin each triangle
        rotate(radians(t + 2*i*360/90))   
        #draw the triangle
        strokeWeight(2)
        stroke(3*i, 255,255)
        tri(100)
        #return to saved orientation
        popMatrix()
    t += 0.5

def tri(length):
    
    noFill() #makes the triangle transparent


    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)