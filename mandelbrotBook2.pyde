from math import sqrt, degrees,atan2, sin, cos,radians

#set the range of x-values
xmin=-2
xmax=2

#range of y-values
ymin = -2
ymax = 2

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl= rangex/float(width) 
    yscl= rangey/float(height)
    
def draw():
    #origin in center:
    #translate(width/2,height/2)
    #go over all x's and y's on the grid
    for x in range(width):#arange(xmin,xmax,.01):
        for y in range(height):#arange(ymin,ymax,.01):
            z=[xmin+x*xscl,ymin+y*yscl]
            #put it into the mandelbrot function
            col=mandelbrot(z,50)
            #if mandelbrot returns 0
            if col == 50:
                fill(0)
            else:
                c = (10*col+frameCount)%255
                fill(c,255,255)

            rect(x,y,1,1)
    saveFrame("####.png")
    

def mandelbrot(z,num):
    '''runs the process num times
    and returns the diverge count'''
    count=0
    #define z1 as z
    z1=z
    #iterate num times
    while count <= num:
        #check for divergence
        if magnitude(z1) > 2.0:
        #return the step it diverged on
            return count
        #iterate z
        z1=cAdd(cMult(z1,z1),z)
        count+=1
    #if z hasn't diverged by the end
    return num

def arange(start,stop,step):
    '''Returns a list of numbers from 
    start to stop by step '''
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output


def cAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    '''Returns the product of two complex numbers'''
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
 

def theta(z):
    '''Calculates the angle of rotation of a complex number'''
    return degrees(atan2(z[1],z[0]))

def magnitude(z):
    try:
        return sqrt(z[0]**2 + z[1]**2)
    except ValueError:
        return 0
