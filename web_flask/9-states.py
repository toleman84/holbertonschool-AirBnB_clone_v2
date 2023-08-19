#!/usr/bin/python3
"""doc"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(arg=None):
    """used to close the current SQLAlchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """doc"""
    states = storage.all(State)
    return render_template("9-states.html", states=states.values())


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """doc"""
    state = storage.all(State)
    if state is not None:
        return render_template("9-states.html", state=state.values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
