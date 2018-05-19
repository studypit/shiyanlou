#!/usr/bin/env python3

import sys

insur = [0.08,0.02,0.005,0,0,0.06]
taxrate = [0.03,0.1,0.2,0.25,0.3,0.35,0.45]
quick = [0,105,555,1005,2755,5505,13505]

def salf(saln):
    ins = 0
    for a in insur:
        ins += a * saln
    sal = saln -ins
    return sal

def mtax(sal,tr,qui):
    tax = (sal - 3500) * tr - qui
    smt = sal - tax
    return smt

if __name__ == '__main__':
    try:
        s = sys.argv[1:]
        for id_sal in s:
            pias = id_sal.split(':')
            emid = int(pias[0])
            sal = int(float(pias[1]))
            if emid < 0 or sal < 0:
                raise ValueError
            q = salf(sal)
            qo = q - 3500
            if qo <= 0:
                result = q
            elif 0 < qo <= 1500:
                result = mtax(q,taxrate[0],quick[0])
            elif 1500 < qo <= 4500:
                result = mtax(q,taxrate[1],quick[1])
            elif 4500 < qo <= 9000:
                result = mtax(q,taxrate[2],quick[2])
            elif 9000 < qo <= 35000:
                result = mtax(q,taxrate[3],quick[3])
            elif 35000 < qo <= 55000:
                result = mtax(q,taxrate[4],quick[4])
            elif 55000 < qo <= 80000:
                result = mtax(q,taxrate[5],quick[5])
            else:
                result = mtax(q,taxrate[6],quick[6])
            print(emid, end=':')
            print("%.2f"%result)
    except ValueError:
        print("Parameter Error")
