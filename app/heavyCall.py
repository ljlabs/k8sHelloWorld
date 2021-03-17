from random import randint


def thisIsAHeavyCall():
    s = 1
    for i in range(10000):
        s += randint(10000, 100000)
    return s
