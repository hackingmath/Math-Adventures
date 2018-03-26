# GameOfLife.pyde

from random import choice

width_of_grid = 41
height_of_grid = 41

#size of cell
sz = 600//width_of_grid + 1

class Cell:
    def __init__(self,c,r,on=0):
        self.c = c
        self.r = r
        self.on = on
        
    def checkNeighbors(self):
        neighbs = 0 #running sum
        #check the neighbors above
        if self.r > 0:
            if cellList[self.r-1][self.c].on == 1:
                neighbs += 1           
            #check the neighbor above and to the left
            if self.c > 0:
                if cellList[self.r-1][self.c-1].on == 1:
                    neighbs += 1
            
            #check the neighbor above and to the right
            if self.c < width_of_grid-1:
                if cellList[self.r-1][self.c+1].on == 1:
                    neighbs += 1

        #check the neighbor below
        if self.r < height_of_grid-1:
            if cellList[self.r+1][self.c].on == 1:
                neighbs += 1
            
            #check the neighbor below and to the left
            if self.c > 0:
                if cellList[self.r+1][self.c-1].on == 1:
                    neighbs += 1
            
            #check the neighbor to the right
            if self.c < width_of_grid-1:
                if cellList[self.r+1][self.c+1].on == 1:
                    neighbs += 1

        #check the neighbor to the left
        if self.c > 0:
            if cellList[self.r][self.c-1].on == 1:
                neighbs += 1

        return neighbs #returns the total number of neighbors

            

    def update(self):
        if self.on == 1:
            fill(0)
        else:
            fill(255)
        rect(sz*self.c,sz*self.r,sz,sz)

    
def setup():
    global cellList
    size(600,600)
    noStroke()
    cellList = createCellList()
    
def draw():
    global cellList,level
    frameRate(10)

    newList = [] #create a new list for the next gen
    for r,row in enumerate(cellList):
        newList.append([]) #add empty row
        for c,cell in enumerate(row):
            if cell.on == 0: #if cell is off
                #check neighbs and append new value
                newList[r].append(Cell(c,r,cell.checkNeighbors()))
            else: #on cells stay on
                newList[r].append(Cell(c,r,1))
    cellList = newList[::]
    level += 1
    for row in cellList:
        for cell in row:
            cell.update()
    if level == 24:
        cellList = createCellList()
    for row in cellList:
        for cell in row:
            cell.update()
    if level == 24:
        cellList = createCellList()


def createCellList():
    '''Creates a big list of off cells with
    one on Cell in the center'''
    global cellList, level
    cellList=[]#empty list for cells

    #populate the initial cell list
    for j in range(height_of_grid):
        cellList.append([]) #add empty row
        for i in range(width_of_grid):
            onoff = choice([0,1]) #randomly on or off
            cellList[j].append(Cell(i,j,onoff))

    level = 0
    return cellList
