##Евклид в итеративном виде для кольца вычетов


def gcd(a, b):
    x, X, y, Y = 1, 0, 0, 1

    while b:
        q = a // b #Делим нацело коэффициенты
        a, b = b, a % b
        x, X = X, x - X*q
        y, Y = Y, y - Y*q
    return (a, x, y)

print(gcd(5,3))