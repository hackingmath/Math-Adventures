'''Traveling Salesperson Page Review
July 3, 2018'''

import random

N_CITIES = 100

class City:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.number = num #identifying number
        
    def display(self):
        fill(0,255,255)#sky blue
        ellipse(self.x,self.y,10,10)
        textSize(20)
        text(self.number,self.x-10,self.y-10)
        noFill()
        
class Route:
    def __init__(self):
        self.distance = 0
        #put cities in a list in order:
        self.cityNums = random.sample(list(range(N_CITIES)),N_CITIES)
        
    def display(self):
        strokeWeight(3)
        stroke(255,0,255) #purple
        beginShape()
        for i in self.cityNums:
            vertex(cities[i].x,cities[i].y)
            #then display the cities and their numbers
            cities[i].display()
        endShape(CLOSE)
        
    def calcLength(self):
        self.distance = 0
        for i,num in enumerate(self.cityNums):
            #find the distance from the current city to 
            #the previous city
            self.distance += dist(cities[num].x,
                                  cities[num].y,
                                  cities[self.cityNums[i-1]].x,
                                  cities[self.cityNums[i-1]].y)
        return self.distance
    
    def mutateN(self,num):
        indices = random.sample(list(range(N_CITIES)),num)
        child = Route()
        child.cityNums = self.cityNums[::]
        for i in range(num-1):
            child.cityNums[indices[i]],child.cityNums[indices[(i+1)%num]] = \
            child.cityNums[indices[(i+1)%num]], child.cityNums[indices[i]]
        return child
    
    def crossover(self,partner):
        '''Splice together genes with partner's genes'''
        child = Route()
        #randomly choose slice point
        index = random.randint(1,N_CITIES - 2)
        #add numbers up to slice point
        child.cityNums = self.cityNums[:index]
        #half the time reverse them
        if random.random()<0.5:
            child.cityNums = child.cityNums[::-1]
        #list of numbers not in the slice
        notinslice = [x for x in partner.cityNums if x not in child.cityNums]
        #add the numbers not in the slice
        child.cityNums += notinslice
        return child
    
                                  
        
cities = []
random_improvements = 0
mutated_improvements = 0
population = []
POP_N = 10000 #number of routes
        
def setup():
    global best, record_distance, first, population
    size(1200,1200)
    background(0)
    for i in range(N_CITIES):
        cities.append(City(random.randint(50,width-50),
                           random.randint(50,height-50),i))
    #put organisms in the population list
    for i in range(POP_N):
        population.append(Route())
    best = random.choice(population)
    record_distance = best.calcLength()
    first = record_distance

def draw():
    global best, record_distance, population
    background(0)
    best.display()
    println(record_distance)
    #println(best.cityNums)
    population.sort(key=Route.calcLength)
    population = population[:POP_N] #limit size of population
    length1 = population[0].calcLength()
    if length1 < record_distance:
        record_distance = length1
        best = population[0]
        saveFrame("#####.png")
    
    #do crossover on population
    for i in range(POP_N):
        parentA,parentB = random.sample(population,2)
        #reproduce:
        child = parentA.crossover(parentB)
        population.append(child)
        
    #mutateN the best in the population
    for i in range(3,25):
        if i < N_CITIES:
            new = best.mutateN(i)
            population.append(new)
    
    #mutateN random Routes in the population
    for i in range(3,25):
        if i < N_CITIES:
            new = random.choice(population)
            new = new.mutateN(i)
            population.append(new)
    
