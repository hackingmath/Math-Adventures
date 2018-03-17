def setup():
    size(600,600)
    #rectMode(CENTER)
    colorMode(HSB)
    
def draw():
    #set background black
    background(0)
    #translate(5,5)
    for x in range(20):
        for y in range(20):
            d = dist(30*x,30*y,mouseX,mouseY)
            fill(0.5*d,360,360)
            rect(30*x,30*y,25,25)
            
'''def draw():
    #set background white
    background(255)
    translate(20,20)
    textSize(12)
    for i in range(10):
        fill(20*i,255,255)
        rect(31*i,0,25,25)
        fill(0)
        text(str(20*i),31*i+5,50)'''
        

            
        