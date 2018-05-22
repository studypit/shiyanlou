#!/usr/bin/env python3

from datetime import datetime

def log(func):
    def deco(*args, **kwargs):
        print('Function ' + func.__name__ + ' has been called at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args, **kwargs)
    return deco

def add(x,y):
    return x + y

add = log(add)
print(add(2,3))

"""
from math import pi

def f(a):
    return lambda: a ** 2 * pi

if __name__ == '__main__':
    print(f(2))
    print(f(2)())
"""

print(add.__name__)
