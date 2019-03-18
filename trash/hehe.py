def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def start(b, n):
    g, x, y = gcd(b, n)
    if g == 1:
        return x % n

n = (int)(input())
b = (int)(input())

print(start(b,n))