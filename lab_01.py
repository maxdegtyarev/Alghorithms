#   2019, Maxim Degtyarev
#   MAI, Lab-01

from sympy import *

#Итеративный алгоритм Евклида для полиномов
def gcd_polynome_iterative(a, b):
    X = symbols('x')
    x, xx, y, yy = 1, 0, 0, 1

    while b:
        q, r = div(a,b, X) #Делим полиномы. Q - частное, R - остаток
        a, b = b, r
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (a, x, y)

#Рекурсивный алгоритм Евклида для полиномов
def gcd_polynome_recursive(a, b):
    X = symbols('x')
    if not b:
        return (1, 0, a)

    q,r = div(a,b, X)
    y, x, Q = gcd_polynome_recursive(b, r)
    return (x, y - q * x, Q)

#Расширанный алгоритм Евклида
def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = gcd(b % a, a)
        return (g, y - (b // a) * x, x)

#Поиск обратного элемента в кольце вычетов по модулю n
def inverse(b, n):
    g, x, y = gcd(b, n)
    if g == 1:
        return x % n
    else:   #Если нет элемента
        return None