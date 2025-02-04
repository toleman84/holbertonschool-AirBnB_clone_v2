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


@app.route("/states_list")
def states_list():
    """gets all of the State objects from the storage engine"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states.values())


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
