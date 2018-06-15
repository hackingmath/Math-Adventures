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
    line(0,ground,width,ground) #line for the "ground"
    noFill()
    ellipse(x,Y,2*r,2*r)
    #calculate position of drawing "dot"
    dot = PVector(x+r*cos(v*TWO_PI*t+PI/2),Y+r*sin(TWO_PI*v*t+PI/2))
    #save that position to the points list, to be drawn later
    points.append(dot)
    line(dot.x,dot.y,x,Y) #radial segment
    fill(255,0,0) #red dot
    ellipse(dot.x,dot.y,10,10)
    #loop through the points list to draw the curve
    for i,pt in enumerate(points):
        if i < len(points) - 2:
            stroke(255,0,0)
            line(pt.x,pt.y,points[i+1].x,points[i+1].y)
    x += TWO_PI*r*dt*v #update x-value by velocity
    if x > width: #when the wheel gets all the way to the right
        #noLoop() # uncomment this out to only run it once
        x = 0.0 # reset position all the way to the left
        points = [] # erase the trail
    #println(x) #just for testing
    #println(dot.x)
    t += dt #increment the time variable
    '''if frameCount % 2 == 0: #This is for saving screenshots to make a .gif
        saveFrame('####.png')'''
    
