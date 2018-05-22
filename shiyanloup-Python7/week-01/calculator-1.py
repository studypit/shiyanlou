#!/usr/bin/env python3

import sys

quickpass = [0,105,555,1005,2755,5505,13505]
taxrate = [0.03,0.1,0.2,0.25,0.3,0.35,0.45]

try:
    m = int(float(sys.argv[1]))
    s = m - 3500
    if m < 0:
        raise ValueError
    elif s <= 0:
        taxre = 0
    elif 0 < s <= 1500:
        taxre = s * taxrate[0] - quickpass[0]
    elif 1500 < s <= 4500:
        taxre = s * taxrate[1] - quickpass[1]
    elif 4500 < s <= 9000:
        taxre = s * taxrate[2] - quickpass[2]
    elif 9000 < s <= 35000:
        taxre = s * taxrate[3] - quickpass[3]
    elif 35000 < s <= 55000:
        taxre = s * taxrate[4] - quickpass[4]
    elif 55000 < s <= 80000:
        taxre = s * taxrate[5] - quickpass[5]
    else:
        taxre = s * taxrate[6] - quickpass[6]
    print("%.2f"%taxre)
except ValueError:
    print("Parameter Error")
