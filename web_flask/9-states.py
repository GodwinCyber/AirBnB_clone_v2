#!/usr/bin/python3
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
      /states id:  display a HTML page: list all the states objects
      in file DBStorage related to the cities
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Display a HTML page with a list of City objects linked to the
    State sorted by name."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=states)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
