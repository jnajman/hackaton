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
#fibonacci
# ------------------

# def fibo3(num_1,num_2,counter,length):
#     if counter==length:
#         print(num_2)
#         return num_2
#     else:
#         counter+=1
#         return fibo3(num_2,num_1+num_2,counter,length)
#
# fibo_in=input('zadej delku fibonacciho rady (vetsi nez 2): ')
# # print(fact_in)
# fibo3(1,1,2,int(fibo_in))


def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

print(F(8))