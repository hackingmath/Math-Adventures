#wander.py

from turtle import *
from random import randint

speed(0)

def wander():
    while True:
        forward(3)
        if xcor() >= 200 or xcor() <= -200 or ycor() <=-200 or ycor()>=200:
            left(randint(90,180))

wander()            
