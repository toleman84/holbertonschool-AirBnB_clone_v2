#!/usr/bin/python3
"""doc"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    """used to close the current SQLAlchemy session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """doc"""
    states = storage.all(State).order_by(State.name)
    amenities = storage.all(Amenity).order_by(Amenity.name)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
