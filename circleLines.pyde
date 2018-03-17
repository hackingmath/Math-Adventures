#circleLines.pyde

def setup():
    size(600,600)
    
def draw():
    background(255)
    translate(width/2,height/2)
    points = []
    num = 24
    for i in range(num):
        x = 250*cos(radians(360.0*i/num))
        y = 250*sin(radians(360.0*i/num))
        #put point in a list
        points.append([x,y])

    for p in points: #from every point
        for other in points: #to every "other" point
            stroke(255,0,0) #red
            line(p[0],p[1],other[0],other[1])