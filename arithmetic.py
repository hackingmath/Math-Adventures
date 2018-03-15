#arithmetic.py

def average(a,b):
    return (a + b) / 2

def mySum(num):
    running_sum = 0
    for i in range(1,num+1):
        running_sum += i
    return running_sum

#print(mySum(100))

def mySum2(num):
    running_sum = 0
    for i in range(num + 1):
        running_sum += i**2 + 1
    return running_sum

#print(mySum2(20))

def average3(numList):
    return sum(numList)/len(numList)

#print(average3([8,11,15]))

#exercise:
print(average3([53,28,54,84,65,60,22,93,62,27,16,25,74,42,4,42,15,96,11,70,83,97,75]))

#average: 52.08695652173913
