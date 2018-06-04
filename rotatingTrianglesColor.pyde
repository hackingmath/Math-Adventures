'''Rotating Triangles
June 3,2018
Thanks to Victoria P. for the color idea'''

t = 0
NUM_TRIS = 90

def setup():
    size(600,600)
    colorMode(HSB)
    noStroke()
    
def draw():
    global t
    background(0)
    translate(width/2,height/2)
    for i in range(NUM_TRIS):
        pushMatrix()
        rotate(radians(360*i/float(NUM_TRIS)))
        translate(200,0)
        #shift = map(mouseX,0,width,0,5.0)
        #println(shift)
        rotate(4.33*(t+i))
        fill(3.5*i,255,255,50)
        tri(100)
        popMatrix()
    t += 0.1
    #The following code saves a set of 
    #screenshots to make into a .gif
    '''saveFrame('####.png')
    if t>TWO_PI:
        noLoop()'''
        
def tri(sz):
    beginShape()
    for i in range(3):
        
        vertex(sz*cos(radians(120*i)),
               sz*sin(radians(120*i)))
    endShape(CLOSE)
    
    
