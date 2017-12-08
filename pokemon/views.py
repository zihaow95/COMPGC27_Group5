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
result = [0,0,0,0,0,0]
name_list = [0,0,0,0,0,0]


@app.route('/', methods=["GET", "POST"])
def querypage():
    if flask.request.method == 'GET':
        result0 = {}
        return render_template("querypage.html", result0=result0)

    elif flask.request.method == 'POST' and flask.request.form.get('query1', None) == "query":
        pokemon_name = flask.request.form["Pokemon_name1"]
        name = validName(pokemon_name)
        if name != 0:
            result1 = queryPokemon(name)
            result[0] = result1
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2])
        else:
            return render_template("querypage.html", result2= result[1], result3=result[2], warning1="Please enter the correct name.")

    elif flask.request.method == 'POST' and flask.request.form.get('query2', None) == 'query':
        pokemon_name = flask.request.form["Pokemon_name2"]
        name = validName(pokemon_name)
        if name != 0:
            result2 = queryPokemon(name)
            result[1]=result2
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2])
        else:
            return render_template("querypage.html", result1=result[0], result3=result[2], warning2="Please enter the correct name.")

    elif flask.request.method == 'POST' and flask.request.form.get('query3', None) == 'query':
        pokemon_name = flask.request.form["Pokemon_name3"]
        name = validName(pokemon_name)
        if name != 0:
            result3 = queryPokemon(name)
            result[2] = result3
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2])
        else:
            return render_template("querypage.html", result1=result[0], result2= result[1],warning3="Please enter the correct name.")

    elif flask.request.method == 'POST' and flask.request.form.get('add1', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name1"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[0] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   addation1="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html",  result2= result[1], result3=result[2],warning1="Please enter the correct name.")

    elif flask.request.method == 'POST' and flask.request.form.get('add2', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name2"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[1] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   addation2="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html", result1=result[0],result3=result[2],warning2="Please enter the correct name.")

    elif flask.request.method == 'POST' and flask.request.form.get('add3', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name3"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[2] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   addation3="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html", result2= result[1], result3=result[2],warning3="Please enter the correct name.")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4501)