'''Wolfram CA
Zoomable'''

#define constants
BLACK = color(0,0,0)
WHITE = color(255,255,255)
RED = color(255,0,0)
GREEN = color(0,255,0)
BLUE = color(0,0,255)
CYAN = color(0,255,255)
VIOLET = color(148,0,211)

#CA variables
w = 50
rows = 1000
cols = 1000

def ruleNum(num):
    '''converts num to binary list'''
    output = []
    for i in range(7,-1,-1):
        if num // (2**i) == 1:
            output.append(1)
            num -= 2**i
        else:
            output.append(0)
    return output

def ruleNum2(num):
    '''Got this more Pythonic version online'''
    strbinNum = str(dec_to_bin(num))
    output = [int(x) for x in strbinNum]
    if len(output) < 8:
        output = [0]*(8-len(output)) + output
    return output

def dec_to_bin(x):
    bin_int = "{0:08b}".format(x)
    return int(bin_int)#[2:])

def rules(a,b,c):
    return ruleset[7-(4*a+2*b+c)]

def generate():
    for i,row in enumerate(cells): #look at first row
        for j in range(1,len(row)-1):
            left = row[j-1]
            me = row[j]
            right = row[j+1]
            if i < len(cells) - 1:
                cells[i+1][j] = rules(left,me,right)
    return cells

#ruleset = [0,0,0,1,1,1,1,0] # Rule 30
#ruleset = [0,0,1,1,0,1,1,0] # Rule 54
ruleset = ruleNum(30)
#println(ruleset)

def setup():
    global cells
    size(600,600)
    noStroke()
    cells = []
    for r in range(rows):
        cells.append([])
        for c in range(cols):
            cells[r].append(0)
    cells[0][cols//2] = 1
    
    cells = generate()


def draw():
    background(0)
    #cells = generate()
    #draw here
    for i,cell in enumerate(cells): #rows
        for j,v in enumerate(cell): #columns
            if v == 1:
                rect(j*w-(cols*w-width)/2,w*i,w,w)
                
def keyPressed():
    global w
    if key == CODED:
        if keyCode == UP:
            w += 1
        if keyCode == DOWN:
            w -= 1
    
