#!/usr/bin/env python3

import sys
import csv

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    args = sys.argv[1:]
    index = args.index('-c')
    configfile = args[index+1]
    index = args.index('-d')
    userfile = args[index+1]
    index = args.index('-o')
    outputfile = args[index+1]

class Config(object):
    def __init__(self, configfile):
        self.config = self._read_config()
    def _read_config(self):
        config = {}

class UserData():
    def __init__(self):
        self.userdata = self._read_users_data()
    def _read_users_data(self):
        userdata = []

class IncomeTaxCalculator(object):
    def calc_for_all_userdata(self):
    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open(" ") as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
    
