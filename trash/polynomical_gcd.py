from numpy import number
from sympy import *

#Default
def gcd(a, b):
    X = symbols('x')
    x, xx, y, yy = 1, 0, 0, 1

    while b:
        q, r = div(a,b, X) #Делим полиномы. Q - частное, R - остаток
        a, b = b, r
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (a, x, y)

#Recursive
def gcd_recursive(a, b):
    X = symbols('x')
    if not b:
        return (1, 0, a)

    q,r = div(a,b, X)
    y, x, Q = gcd_recursive(b, r)
    return (x, y - q * x, Q)

x = symbols('x')

#a = (x**1 - 1) * (x**1 - 2)
#b = (x**1 - 1)*(x**3)

#a, b = x**3, x**2
#Q, X, Y = gcd(a,b)

#print("a = {0}\nX = {1}\nb = {2}\nY = {3}\ng = {4}".format(a,X,b,Y,Q));

n = (int)(input());
a = (int)(input());

q = 1;

if n:
    while (q < 100000):
        if ((a * q) % n == 1):
            print("Элемент:{0}".format(q))
            break;
        q = q + 1