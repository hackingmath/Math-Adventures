'''Cloning Keith Briain's sketch on Instagram
August 16, 2018'''

def setup():
    size(600,600)
    
def draw():
    sz = 100
    background(200)
    translate(width/2,height/2) #go to middle of screen
    #draw central figure
    ang = map(mouseX,0,width,0,PI)
    hex(sz,ang)
    hex_of_circles(sz)
    #outside hexes and spirals
    for k in range(6):
        #save the orientation
        pushMatrix()
        #distance from center
        d = 2*sz*sqrt(3)/2.0
        rotate(k*PI/3.0) #rotate to position
        translate(d,0) #translate to center of hex
        hex(sz)
        popMatrix() #reset orientation
    for m in range(3):
        stroke(10,10,10,50)
        line(-width/2,0,width/2,0)
        line(-width/2,sz*1.5,width/2,sz*1.5)
        rotate(2*PI/3.0)
    
def hex(sz,ang=0):
    '''Draws a hex and the spiral of ellipses'''
    d = 0
    sz2 = 20
    noFill()
    #red circle around hex
    stroke(255,150,150,100)
    ellipse(0,0,2*sz,2*sz)
    
    #arcs
    stroke(100,155,100,100) #green
    pushMatrix()
    rotate(PI/6.0)
    for i in range(6):
        pushMatrix()
        rotate(i*PI/3.0)
        translate(sz,0)
        #rotate(PI/6.0)
        ellipse(0,0,2*sz,2*sz)#,0,PI)
        popMatrix()
    popMatrix()
    stroke(100) #gray
    for j in range(20): #20 hexes
        rotate(PI/6.0) #rotate first
        beginShape() #start drawing polygon
        for i in range(6):
            #position of vertex of hexagon
            vertex(sz*cos(TWO_PI*i/6.0),
                sz*sin(TWO_PI*i/6.0))
        endShape(CLOSE) #end drawing hexagon
        sz *= sqrt(3)/2.0 #make next hexagon smaller
        
    
    stroke(50) #black
    #spiral of ellipses
    for k in range(20):
        #play around with these lines
        rotate(-PI/5.0)
        d += sz2*sqrt(3)/30.0
        ellipse(d,0,sz2,sz2) #draw the ellipse
        sz2 *= 1.9/sqrt(3) #make the size bigger
    
    
        
def hex_of_circles(sz):
    rotate(PI/6.0)
    for i in range(6):
        x = sz*sqrt(3)/2.0
        ellipse(x,0,sz,sz)
        rotate(PI/3.0)
    rotate(PI/6.0)
    
    
