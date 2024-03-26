#!/usr/bin/python3
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
      /states_list: display a HTML page: list all the states objects
      in file DBStorage
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display the html page: list all the states object in DBStorage"""
    states = storage.all("state")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exec):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
