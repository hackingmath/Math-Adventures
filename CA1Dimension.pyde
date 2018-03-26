width_of_grid = 151

#size of cell
sz = 600//101 + 1
class Cell:
    def __init__(self,c,on):
        self.c = c
        self.on = on
        self.ruleList = [0,0,0,1,1,1,1,0] #Rule 30
        
    def checkNeighbors(self):
        global cellList
        if self.c == 0: #if the cell is in column 0
            left = 0
        else:
            left = cellList[self.c-1].on
        me = self.on
        if self.c == len(cellList)-1:
            right = 0
        else:
            right = cellList[self.c+1].on
        return self.ruleList[7 - (4*left+2*me+right)]


    def update(self):
        if self.on == 1:
            fill(0)
        else:
            fill(255)
        rect(sz*self.c,0,sz,sz)

def createCellList():
    '''Creates a big list of off cells with
    one on Cell in the center'''
    global cellList, level
    cellList=[]#empty list for cells
    
    #populate the initial cell list
    for i in range(width_of_grid):
        cellList.append(Cell(i,0)) #add off Cells or zeroes
    #center cell is set to on
    cellList[width_of_grid//2].on = 1
    level = 0
    return cellList

def generateNewCellList():
    global cellList
    newList = []
    for cell in cellList:
        newList.append(Cell(cell.c,cell.checkNeighbors()))
    return newList


def setup():
    global cellList
    size(600,600)
    cellList = createCellList()
    noStroke()

def draw():
    global cellList,level
    pushMatrix()
    translate(-150,level*sz)
    #draw each cell in the list:
    for cell in cellList:
        cell.update()
    popMatrix()
    level += 1
    cellList = generateNewCellList()
