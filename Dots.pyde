#Dots.pyde
def setup():
    size(600,600)

def draw():
    background(0)
    translate(width/2, height/2)
    for i in range(12):
        ellipse(200,20,15,15)
        rotate(radians(360/12))