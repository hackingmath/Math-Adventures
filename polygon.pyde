#polygon.pyde
def setup():
    size(600,600)
    
def draw():
    translate(width/2,height/2)
    polygon(3,100) #3 sides, vertices 100 units from the center
    
def polygon(sides,sz):
    '''draws a polygon given the number
    of sides and length from the center '''
    beginShape()
    for i in range(sides):
        vertex(sz*cos(radians(i*360/sides)),
               sz*sin(radians(i*360/sides)))    
    endShape(CLOSE)