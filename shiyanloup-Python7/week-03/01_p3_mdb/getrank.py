#!/usr/bin/env python3

import sys
from pymongo import MongoClient

def getrank(usr_id):
    client = MongoClient('127.0.0.1',27017)
    db = client.shiyanlou
    con_d = {}
    for contest in db.contests.find():
        for k_, v_ in contest.items():
            if k_ == 'user_id':
                con_s = set(con_d.keys())
                if v_ not in con_s:
                    con_d[v_]=[0,0,0,0]
    for contest in db.contests.find():
        con_d[contest['user_id']][0] += contest['score']
        con_d[contest['user_id']][1] += contest['submit_time']
        con_d[contest['user_id']][2] = contest['user_id']
    con_l = len(con_d)
    for a in range(con_l):
        for x in range(con_l-a-1):
            if con_d[a][0] > con_d[con_l-x][0]:
                continue
            elif con_d[a][0] < con_d[con_l-x][0]:
                con_d[a],con_d[con_l-x] = con_d[con_l-x],con_d[a]
            elif con_d[a][0] == con_d[con_l-x][0]:
                if con_d[a][1] >= con_d[con_l-x][1]:
                    con_d[a], con_d[con_l-x] = con_d[con_l-x], con_d[a]
        con_d[a][3] = a + 1
    for a in range(con_l):
        if con_d[a][2] == usr_id:
            rank_c = con_d[a][3]
            score_c = con_d[a][0]
            submit_time_c = cond[a][1]
            return result = rank_c, score_c, submit_time_c

if __name__ == '__main__':
    try:
        s = int(sys.argv[1])
    except:
        print("Parameter Error")
    print(getrank(s))
