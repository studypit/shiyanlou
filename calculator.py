#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv

class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]

class Config(object):

    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}

class UserData(object):

    def __init__(self):
        self.userdata =  self._read_users_data()

    def _read_users_data(self):
        userdata = []

class IncomeTaxCalculator(object):

    def calc_for_all_userdata(self):

    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open("") as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':

