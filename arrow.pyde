#arrow.pyde

def setup():
    size(600,600)
    
cols = 20 #number of columns
#scale factors:
xscl = 600/cols
yscl = 600/cols
sz = 6
    
def draw():
    global cols, xscl, yscl
    background(255)
    for x in range(cols):
        for y in range(cols):
            arrow(10+x*xscl,10+y*yscl,sz)
    
def arrow(x,y,sz):
    pushMatrix()
    translate(x,y)
    angle = atan2(mouseY-y,mouseX-x)
    rotate(angle)
    beginShape()
    vertex(0,-sz/2.0)
    vertex(2*sz,-sz/2.0)
    vertex(2*sz,-3*sz/2.0)
    vertex(4*sz,0)
    vertex(2*sz,3*sz/2.0)
    vertex(2*sz,sz/2.0)
    vertex(0,sz/2.0)
    endShape(CLOSE)
    popMatrix()