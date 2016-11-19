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
#factorial
# ------------------

def factorial(num_in):
    if num_in<1:
        return 1
    else:
        return_number=num_in*factorial(num_in-1)
        return return_number

fact_in=input('zadej cislo pro vypocet faktorialu: ')
# print(fact_in)
print(factorial(int(fact_in)))