#!/usr/bin/python3
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
      /city by state: display a HTML page: list all the states objects
      in file DBStorage related to the cities
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display the html page: list all state related to cities"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
