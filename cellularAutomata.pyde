# cellularAutomata.pyde


GRID_W = 41
GRID_H = 41

generation = 0

class Cell:
    def __init__(self,r,c,on=0):
        self.c = c
        self.r = r
        self.on = on
        
    def display(self):
        if self.on == 1:
            fill(0) #black
        else:
            fill(255) #white
        rect(SZ*self.r, SZ*self.c, SZ, SZ)
        
    def checkNeighbors(self):
        neighbs = 0  #check the neighbors
        if self.on == 1: return 1
        for dr,dc in [[-1,0], [1,0], [0,-1],[0,1]]:
            try:
                if cellList[self.r + dr][self.c + dc].on == 1:
                    neighbs += 1
            except IndexError:
                continue
        if neighbs in [1,4]:
            return 1
        else:
            return 0



def setup():
    global SZ, cellList
    noStroke()
    size(600,600)
    SZ = width // GRID_W + 1
    cellList = createCellList()
    
def draw():
    global generation,cellList
    frameRate(10)
    cellList = update(cellList)
    for row in cellList:
        for cell in row:
            cell.display()
    generation += 1
    if generation == 30:
        generation = 1
        cellList = createCellList()
        loop()
        
def update(cellList):
    newList = []
    for r,row in enumerate(cellList):
        newList.append([])
        for c,cell in enumerate(row):
            newList[r].append(Cell(r,c,cell.checkNeighbors()))
    return newList[::]
        

def createCellList():
    '''Creates a big list of off cells with
    one on Cell in the center '''
    newList=[]#empty list for cells 
    #populate the initial cell list
    for j in range(GRID_H): 
        newList.append([]) #add empty row 
        for i in range(GRID_W):
            newList [j].append(Cell(i,j,0)) #add off Cells or zeroes 
    #center cell is set to on
    newList [GRID_H//2][GRID_W//2].on = 1 
    return newList
