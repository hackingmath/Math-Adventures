'''Clone of Matt Enlow @CmonMattTHINK
cycloid animation (he did it in Mathematica)'''

t = 0.0 #time
dt = 0.01 #change in time
r = 50 #radius of circle
ground = 250 # y-val of line circle rolls on
x,Y = 0,ground-r #initial location of circle
v = 2.0 #horizontal velocity factor of circle
points = [] #list to store points
        
def setup():
    size(942,300)
    
def draw():
    global t,dt,r,ground,x,y,points
    background(255) #white
    strokeWeight(2)
    stroke(150)
    line(0,ground,width,ground)
    noFill()
    ellipse(x,Y,2*r,2*r)
    dot = PVector(x+r*cos(v*TWO_PI*t+PI/2),Y+r*sin(TWO_PI*v*t+PI/2))
    points.append(dot)
    line(dot.x,dot.y,x,Y)
    fill(255,0,0)
    ellipse(dot.x,dot.y,10,10)
    for i,pt in enumerate(points):
        if i < len(points) - 2:
            stroke(255,0,0)
            line(pt.x,pt.y,points[i+1].x,points[i+1].y)
    x += TWO_PI*r*dt*v #update x-value by velocity
    if x > width:
        noLoop()
        x = 0.0
        points = []
    println(x)
    println(dot.x)
    t += dt
    if frameCount % 2 == 0:
        saveFrame('####.png')
    
