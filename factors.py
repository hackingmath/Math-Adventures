#factors.py

def factors(num):
    '''Returns a list of the factors of num'''
    factorList = []
    for i in range(1,num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList

