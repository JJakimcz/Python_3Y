import math
def zad13():
    a = 1
    b = 2
    if a == b:
        print("Tak")
    else:
        print("Nie")

def zad14():
    a = 3
    if a % 2 == 0:
        print("Tak")
    else:
        print("Nie")

def zad15():
    a = 1
    print(type(a))

def zad16():
    a = 1
    b = 2

    if a > b:
        print(a)
    else:
        print(b)

def zad17():
    a = 9
    b = 7
    c = 3
    d = 0
    for x in [a, b, c]:
        if x > d:
            d = x
    print(d)

def zad18():
    sigma = [10, 2, 1]
    sigma.sort()
    print(sigma)

def zad19():
    a = 1
    b = 2
    x = -b / a
    print(x)


def zad20():
    a = 1
    b = 2
    c = -3
    d = b*b - 4*a*c
    if d < 0:
        print("Brak rozwiazań")
    elif d == 0:
        print(-b/(2*a))
    else:
        print("X1:", (-b - math.sqrt(d)) / (2 * a), "X2:", (-b + math.sqrt(d)) / (2 * a))

def zad21():
    a = 213
    b = str(a)
    for x in b:
        print(x)

zad13()
zad14()
zad15()
zad16()
zad17()
zad18()
zad19()
zad20()
zad21()