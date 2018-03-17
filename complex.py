'''Complex Numbers from the book'''

from math import sqrt, degrees,atan2, sin, cos,radians

def cAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    '''Returns the product of two complex numbers'''
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
 

def theta(z):
    '''Calculates the angle of rotation of a complex number'''
    return degrees(atan2(z[1],z[0]))

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

def power(z,n):
    r = magnitude(z)
    angle = (1/3)*radians(theta(z)+360) 
    return [r**n*cos(n*angle),r**n*sin(n*angle)]

def synthDiv(divisor,dividend):
    '''divides a polynomial by a constant and returns a lower-degree polynomial. Enter divisor as a constant: (x - 3) is 3
    Enter dividend as a list of coefficients:
    x**2 – 5*x + 6 becomes [1,-5,6]'''
    quotient = [] #empty list for coefficients of quotient
    row2 = [0] #start the second row
    for i in range(len(dividend)):
        quotient.append(dividend[i]+row2[i]) #add the ith column
        row2.append(divisor*quotient[i]) #put the new number in row 2
    print(quotient)

def quad(a,b,c): 
    '''Returns the solutions of an equation
    of the form a*x**2 + b*x + c = 0'''
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1,x2

def f(x):
    return x**3 - 15*x - 4

def average(a,b):
    return (a + b) / 2

def guess():
    lower = -3
    upper = -4
    for i in range(20):
        midpt = average(lower,upper)
        if f(midpt) == 0:
            return midpt
        elif f(midpt) < 0:
            upper = midpt
        else:
            lower = midpt
    return midpt

def arange(start,stop,step):
    '''Returns a list of numbers from 
    start to stop by step'''
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output

