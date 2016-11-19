'''
In this exercise, you'll understand the concepts of recursion using selected programs - Fibonacci sequence, Factorial and others. We will also use Turtle graphics to simulate recursion in graphics.

Factorial
Fibonacci
Greatest common divisor

Once we understand the principles of recursion, we can do fun stuff with Turtle graphics and DRAW:

a square
a nautilus
a spiral
a circles (many circles)
a hexagram
a Koch star
a snowflake
a tree
'''
# ------------------
#turtle
# ------------------

import turtle
from math import cos,sin
from math import radians as deg2rad
from math import degrees as rad2deg

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

m=13
# turtle.shape('turtle')
turtle.forward(F(m))
turtle.left(90)

for j in range(m,0,-1):
    a=F(j)
    zlomy=5
    angle1=90/(zlomy+1)
    d=2*a*sin(deg2rad(angle1/2))
    turn_angle=(angle1/2)


    for i in range(0,zlomy+1):
        turtle.left(turn_angle)
        turtle.forward(d)
        turtle.left(angle1/2)

turtle.exitonclick()



# a=200
# zlomy=20
# angle1=90/(zlomy+1)
# d=2*a*sin(deg2rad(angle1/2))
# turn_angle=(angle1/2)
#
#
# turtle.forward(a)
# turtle.left(90)
#
# for i in range(0,zlomy+1):
#     turtle.left(turn_angle)
#     turtle.forward(d)
#     turtle.left(angle1/2)
#
# # turtle.shape('turtle')
# turtle.exitonclick()
