import configparser
import flask
from flask import render_template, g
import sqlite3
from pokemon_query import validName,queryPokemon

app = flask.Flask(__name__)

# def connect_db():
#     return sqlite3.connect("pokemon.db")
#
# @app.before_request
# def before_request():
#     g.db = connect_db()
#
# @app.teardown_request
# def teardowm_request(exception):
#     if hasattr(g, 'db'):
#         g.db.close()

@app.route('/', methods=["GET", "POST"])
def querypage():
    if flask.request.method == 'GET':
        result = {}
        return render_template("querypage.html", result=result)

    elif flask.request.method == 'POST' and flask.request.form.get('query', None) == "query":
        pokemon_name = flask.request.form["Pokemon_name"]
        name = validName(pokemon_name)
        if name != 0:
            result = queryPokemon(name)
            return render_template("querypage.html", result=result)
        else:
            return render_template("querypage.html", warning="Please enter the correct name.")

    # elif flask.request.method == 'POST' and flask.request.form.get('mega', None) == "query mega":
    #     pokemon_name = flask.request.form["Pokemon_name"]
    #     pokemon_name = pokemon_name.strip().lower().capitalize()
    #     name = "Mega "+ pokemon_name
    #     name = validName(name)
    #     if name != 0:
    #         result = queryPokemon(name)
    #         return render_template("querypage.html", result=result)
    #     else:
    #         return render_template("querypage.html", warning="Please enter the correct name.")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4501)