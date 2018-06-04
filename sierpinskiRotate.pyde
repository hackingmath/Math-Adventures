'''Rotating Sierpinski Triangles
https://twitter.com/ulamspiral317/status/1003244152509775872
June 4, 2018'''

t = 0
def setup():
    size(600,600)
    noStroke()
    
def draw():
    global t
    background(0)
    translate(width/2, height/2)
    rotate(radians(90))
    sierp(50,8,t)
    saveFrame('####.png')
    t += 0.1
    if t > TWO_PI:
        noLoop()
    
def sierp(sz,level,t):
    if level > 0:
        fill(255)
    
        tri(sz)
        pushMatrix()
        rotate(radians(60))
        for i in range(3):
            pushMatrix()
            translate(2*sz,0)
            rotate(PI-t)
            translate(sz,0)
            #rotate(PI)
            sierp(sz/2.0,level-1,t)
            popMatrix()
            rotate(radians(120))
        popMatrix()
        
def tri(sz):
    beginShape()
    for i in range(3):
        vertex(sz*cos(radians(120*i)),
               sz*sin(radians(120*i)))
        
    endShape(CLOSE)
