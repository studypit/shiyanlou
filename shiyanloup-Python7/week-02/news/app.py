#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import json
from flask import Flask, render_template, abort

app = Flask(__name__)

class Files():

    directory = '/home/shiyanlou/news/files'

    def __init__(self):
        # read files
        self._result = {}
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            with open(filepath) as f:
                filedata = json.load(f)
                self._result[filename[:-5]] = filedata

    def get_title_list(self):
        return [item['title'] for item in self._result.values()]

    def get_file(self, filename):
        return self._result[filename]

files = Files()

@app.route('/')
def index():
    title_list = files.get_title_list()
    return render_template('index.html', title_list = title_list )

@app.route('/files/<filename>')
def file(filename):
    file_item = files.get_file(filename)
    if not file_item:
        abort(404)
    return render_template('file.html', file_item = file_item )

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port=3000)
