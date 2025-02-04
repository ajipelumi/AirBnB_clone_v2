#!/usr/bin/python3
""" This script starts a Flask web application. """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Displays "Hello HBNB!". """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Displays "HBNB". """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Displays "C" followed by the value of the text variable. """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """ Displays "Python" followed by the value of the text variable. """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Displays n only if n is an integer. """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """ Displays a HTML page only if n is an integer. """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """ Displays a HTML page only if n is an integer. """
    if n % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
