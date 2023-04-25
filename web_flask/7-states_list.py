#!/usr/bin/python3
""" This script starts a Flask web application. """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(exception=None):
    """ Removes the current SQLAlchemy Session after each request. """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """ Displays a HTML page with list of all State object. """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
