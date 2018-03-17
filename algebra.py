'''From Chapter 4 of Math Adventures with Python'''

from math import sqrt

def equation(a,b,c,d):
    '''solves equations of the
    form ax + b = cx + d'''
    return (d - b)/(a - c)

#print(equation(12, 18,-34, 67))

def quad(a,b,c):
    '''Returns the solutions of an equation
    of the form a*x**2 + b*x + c = 0'''
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2

#print(quad(2,7, -15))

def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x =",x)
        x += 1
    print("done.")

#plug()

'''The guess method'''
def f(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def average(a,b):
    return (a + b)/2

def guess():
    lower = -1
    upper = 0
    for i in range(20):
        midpt = average(lower,upper)
        if f(midpt) == 0:
            return midpt
        elif f(midpt) < 0:
            upper = midpt
        else:
            lower = midpt
    return midpt

x = guess()

print(x, f(x))
