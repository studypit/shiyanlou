#!/usr/bin/env python3

import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient('127.0.0.1',27017)
    db = client.shiyanlou

    con_d = {}

    for contest in db.contests.find():
        con_d_k = set(con_d.keys())
        if contest['user_id'] not in con_d_k:
            con_d[contest['user_id']] = [contest['user_id'],contest['score'],contest['submit_time']]
        else:
            con_d[contest['user_id']][1] += contest['score']
            con_d[contest['user_id']][2] += contest['submit_time']

    con_l = []
    for _, a_ in con_d.items():
        con_l.append(a_)

    a = len(con_l)
    for i in range(a):
        ai = a - i
        for x in range(ai):
            ax = a - x - 1
            if con_l[i][1] < con_l[ax][1]:
                con_l[i], con_l[ax] = con_l[ax], con_l[i]
            elif con_l[i][1] == con_l[ax][1]:
                if con_l[i][2] > con_l[ax][2]:
                    con_l[i], con_l[ax] = con_l[ax], con_l[i]

    num = 0
    for i in range(a):
        num += 1
        if user_id == con_l[i][0]:
            result = num, con_l[i][1], con_l[i][2]
            return result

if __name__ == '__main__':
    try:
        s = int(sys.argv[1])
    except:
        print("Parameter Error")
    print(get_rank(s))
