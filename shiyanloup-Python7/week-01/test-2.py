#!/usr/bin/env python3

from datetime import datetime
from functools import wraps

def log(func):
    @wraps(func)
    def deco(*args, **kwargs):
        print('Function ' + func.__name__ + ' has been called at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args, **kwargs)
    return deco

@log
def add(x,y):
    return x + y

print(add(3,5))
print(add.__name__)
