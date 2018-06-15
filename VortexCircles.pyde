'''Web/Vortex of Circles
June 14, 2018'''

factor = 1.3

def setup():
    size(600,600)
    noFill()
    stroke(255) #white lines
    
def draw():
    global factor
    background(0)
    #Uncomment to display the value of factor
    '''fill(255,0,0)
    textSize(18)
    text(factor,20,20)'''
    factor -= 0.005
    #move the mouse to vary the factor
    #factor = map(mouseX,0,255,1,1.5)
    translate(width/2,height/2)
    vortex(500,100)
    #uncomment these lines to save screenshots:
    '''saveFrame('####.png')'''
    if factor <= 1.07:
        factor = 1.3 #noLoop() #will stop the loop
    
def vortex(r,level):
    num = 30 #number of circles in one ring
    if level > 0:
        r2 = r/4.0
        for i in range(num):
            pushMatrix()
            rotate(radians(360*i/float(num)))
            translate(r,0)
            st = map(r2,0,100,0,3) #make strokeWeight vary
            strokeWeight(st)
            noFill()
            ellipse(0,0,r2,r2)
            popMatrix()
        rotate(TWO_PI/(2*num))
        

        vortex(r/factor,level-1)#1.065,level-1)
