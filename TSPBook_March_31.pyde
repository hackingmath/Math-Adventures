#travelingSalesperson.pyde

import random

N_CITIES = 100

class City:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.number = num #identifying number
        
    def display(self):
        fill(0,255,255) #sky blue
        ellipse(self.x,self.y,10,10)
        textSize(20)
        text(self.number,self.x-10,self.y-10)
        noFill()

class Organism:
    def __init__(self):
        self.distance = 0
        #put cities in a list in numList order:
        self.genes = random.sample(list(range(N_CITIES)),N_CITIES)
        
    def display(self):
        strokeWeight(3)
        stroke(255,0,255) #purple
        beginShape()
        for i in self.genes:
            vertex(cities[i].x,cities[i].y)
            #then display the cities and their numbers
            cities[i].display()
        endShape(CLOSE)

    def calcLength(self):
        self.distance = 0
        for i in range(N_CITIES):
        # find the distance to the previous city
            self.distance += dist(cities[self.genes[i]].x,
                                cities[self.genes[i]].y,
                                cities[self.genes[i-1]].x,
                                cities[self.genes[i-1]].y)
        return self.distance
    
    def mutate(self):
        index1,index2 = random.sample(list(range(N_CITIES)),2)
        self.genes[index1],self.genes[index2] = self.genes[index2],\
        self.genes[index1] #this works!
        
    def mutateN(self,num):
        indices = random.sample(list(range(N_CITIES)),num)
        child = Organism()
        child.genes = self.genes[::]
        for i in range(num-1):
            child.genes[indices[i]],child.genes[indices[(i+1)%num]] = \
            child.genes[indices[(i+1)%num]], child.genes[indices[i]]
        return child
    
    def crossover(self,partner):
        '''Splice together genes with partner's genes'''
        child = Organism()
        #randomly choose slice point
        index = random.randint(1, N_CITIES - 2)
        #add numbers up to slice point
        child.genes = self.genes[:index]
        #half the time reverse them
        if random.random()<0.5:
            child.genes = child.genes[::-1]
        #list of numbers not in the slice
        notinslice = [x for x in partner.genes if x not in child.genes]
        #add the numbers not in the slice
        child.genes += notinslice
        return child
'''
cities = [City(387,487,0),
City(674,304,1),
City(167,466,2),
City(592,159,3),
City(609,235,4),
City(664,483,5),
City(145,567,6),
City(660,116,7),
City(688,339,8),
City(306,440,9),
City(564,178,10),
City(265,606,11),
City(539,322,12),
City(169,509,13),
City(267,403,14),
City(570,379,15),
City(653,297,16),
City(344,126,17),
City(669,702,18),
City(196,472,19),
City(153,469,20),
City(99,272,21),
City(399,570,22),
City(357,478,23),
City(262,409,24),
City(437,181,25),
City(550,269,26),
City(235,160,27),
City(378,715,28),
City(132,409,29),
City(422,409,30),
City(517,296,31),
City(371,181,32),
City(392,137,33),
City(385,325,34),
City(485,683,35),
City(490,373,36),
City(693,509,37),
City(387,491,38),
City(478,399,39),
City(634,187,40),
City(617,269,41),
City(146,280,42),
City(584,495,43),
City(284,276,44),
City(196,289,45),
City(156,458,46),
City(645,449,47),
City(560,242,48),
City(418,398,49)]'''
cities = []
population = [] #list for Organisms
POP_N = 10000 #number of Organisms in population

def setup():
    global best, record_distance,first,population
    size(800,800)
    for i in range(N_CITIES):
        cities.append(City(random.randint(80,width-80),
                           random.randint(80,height-80),i))
    '''for city in cities:
        println("City("+str(city.x)+","+str(city.y)+","+str(city.number)+"),")'''
    #put organisms in population list
    for i in range(POP_N):
        population.append(Organism())
    best = random.choice(population)
    record_distance = best.calcLength()
    first = record_distance
    
def draw():
    global best, record_distance,population
    background(0)
    best.display()
    population.sort(key=Organism.calcLength)
    population = population[:POP_N]
    length1 = population[0].calcLength()
    #print("length1:"+str(length1))
    if length1 < record_distance:
        best = population[0]
        record_distance = length1
 
    # now sort it from shortest route to longest route
    
    # the first Organism has the shortest route 
    #org1 = matingPool[0]    
    
    #matingPool = matingPool[:1000]
    
    
    #do crossover on mating pool
    for i in range(POP_N):#len(matingPool)):
        parentA, parentB = random.sample(population,2)

        #reproduce:
        child = parentA.crossover(parentB)
        index = random.randint(0,POP_N-1)
        population.append(child)
        
    for i in range(3,25):
        if i < N_CITIES:
            neworg = population[0].mutateN(i)
            index = random.randint(0,POP_N-1)
            population.append(neworg)
   
    for i in range(3,25):
        if i < N_CITIES:
            #index = random.randint(0,len(matingPool)-1)
            neworg = random.choice(population)
            neworg = neworg.mutateN(i)
            index = random.randint(0,POP_N-1)
            population.append(neworg)
            
            #println("Mutate")
    
    textSize(30)
    text(first,30,50)
    text(record_distance,300,50) 
    
    println(best.genes)
