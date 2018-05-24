#!/usr/bin/env python3

from flask import Flask
from flask import render_template, abort
from flask import redirect, url_for
from flask import request
from flask import make_response

app = Flask(__name__)
app.config.update({
        'SECRET_KEY': 'a random string'
    })

# request.headers.get('User-Agent')

# page = request.args.get('page')
# per_page = request.args.get('per_page')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

@app.route('/user/<username>')
def user_index(username):
    if username == 'invalid':
        abort(404)
    return render_template('user_index.html', username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

if __name__ == '__main__':
    app.run()
