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


@app.route("/states", defaults={'id': None})
@app.route("/states/<id>")
def states_id(id=None):
    """doc"""
    states = storage.all(State)
    return render_template("9-states.html", states=states.values(), id=id)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
