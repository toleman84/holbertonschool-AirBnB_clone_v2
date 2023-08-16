#!/usr/bin/python3
"""doc"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    """used to close the current SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """gets all of the State objects from the storage engine"""
    states = storage.all(State).order_by(State.name)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
