#Реализуем АЛгоритм для кольца Вычетов
#Пусть даны некоторые целые числа a && b


#Recursive
def gcd(a, b):
    print("gcd({0},{1})".format(a,b))
    if not b:
        return (1, 0, a)

    y, x, g = gcd(b, a % b)
    return (x, y - (a // b) * x, g)


print(gcd(7,3))