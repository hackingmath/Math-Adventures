#matrices.pyde

#set the range of x-values
xmin=-5
xmax=5

#range of y-values
ymin = -5
ymax = 5

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin


def setup():
    global xscl, yscl
    size(600,600)
    xscl= width / rangex
    yscl= -height / rangey

def draw():
    global xscl, yscl
    background(0) #0 is black, 255 is white
    translate(width/2,height/2)
    #grid(xscl, yscl)
    '''ang = map(mouseX,0,width,0,TWO_PI)
    rot_matrix = [[cos(ang),-sin(ang)],
                [sin(ang),cos(ang)]]'''
    
    rot = map(mouseX,0,width,0,TWO_PI)
    tilt = map(mouseY,0,height,0,TWO_PI)
    rot_matrix = rottilt(tilt,rot)
    
    newmatrix = multmatrix(fmatrix,rot_matrix)

    noFill()
    strokeWeight(2) #thicker line
    stroke(255,0,0) #red
    graphPoints2(newmatrix,edges)
    
fmatrix = [[0,0,0],[1,0,0],[1,2,0],[2,2,0],[2,3,0],[1,3,0],[1,4,0],
         [3,4,0],[3,5,0],[0,5,0],
    [0,0,1],[1,0,1],[1,2,1],[2,2,1],[2,3,1],[1,3,1],[1,4,1],
         [3,4,1],[3,5,1],[0,5,1]]

#list of points to connect:
edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],
        [7,8],[8,9],[9,0],
        [10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],
        [17,18],[18,19],[19,10],
        [0,10],[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],
        [8,18],[9,19]]

transformation_matrix = [[0,-1],[1,1]]

def graphPoints(matrix):

    #draw line segments between consecutive points
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl,pt[1]*yscl)
    endShape(CLOSE)
    
def multmatrix(a,b):
    '''Returns the product of 
    matrix a and matrix b'''
    newmatrix = []
    for i in range(len(a)):
        row = []
        #for every column in b
        for j in range(len(b[0])):
            sum1 = 0
            #for every element in the column
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix


def rottilt(rot,tilt):
    '''returns the matrix for rotating a number of degrees.'''
    rotmatrix_Y = [[cos(tilt),0.0,sin(tilt)],
                   [0.0,1.0,0.0],
                   [-sin(tilt),0.0,cos(tilt)]]
    rotmatrix_X = [[1.0,0.0,0.0],
                   [0.0,cos(rot),sin(rot)],
                   [0.0,-sin(rot),cos(rot)]]
    return multmatrix(rotmatrix_X,rotmatrix_Y)

def graphPoints2(pointList,edges):
    '''Graphs the points in a list using segments'''
    for e in edges:
        line(pointList[e[0]][0]*xscl,pointList[e[0]][1]*yscl,
            pointList[e[1]][0]*xscl,pointList[e[1]][1]*yscl)

 
def grid(xscl, yscl):
    '''Draws a grid for graphing'''
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax + 1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0, xmax*xscl,0)
