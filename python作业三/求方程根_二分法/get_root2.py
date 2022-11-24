from sympy import *
import numpy
A=3
B=A%3+1
x=sympy.symbols("x")
for i in numpy.linspace(0,2*3.14,100):
    if(math.exp(-i)-sympy.sin(B*i)==0):
        print(i)

