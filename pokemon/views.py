import configparser
import flask
from flask import render_template, g
import sqlite3
from pokemon_query import validName,queryPokemon, radar
import numpy as np
import matplotlib.pyplot as plt

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
# user's team
    # query 1st pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('query1', None) == "query":
        pokemon_name = flask.request.form["Pokemon_name1"]
        name = validName(pokemon_name)
        if name != 0:
            result1 = queryPokemon(name)
            result[0] = result1
            radar(result1, 'result1')
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5])
        else:
            return render_template("querypage.html", result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   warning1="Please enter the correct name.")
    # query 2nd pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('query2', None) == 'query':
        pokemon_name = flask.request.form["Pokemon_name2"]
        name = validName(pokemon_name)
        if name != 0:
            result2 = queryPokemon(name)
            result[1]=result2
            radar(result2, 'result2')
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5])
        else:
            return render_template("querypage.html", result1=result[0], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   warning2="Please enter the correct name.")
    # query 3rd pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('query3', None) == 'query':
        pokemon_name = flask.request.form["Pokemon_name3"]
        name = validName(pokemon_name)
        if name != 0:
            result3 = queryPokemon(name)
            result[2] = result3
            radar(result3, 'result3')
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5])
        else:
            return render_template("querypage.html", result1=result[0], result2= result[1],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   warning3="Please enter the correct name.")

    # add 1st pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('add1', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name1"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[0] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   addation1="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html", result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   warning1="Please enter the correct name.")
    # add 2nd pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('add2', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name2"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[1] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   addation2="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html", result1=result[0], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   warning2="Please enter the correct name.")
    # add 3rd pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('add3', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name3"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[2] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   addation3="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html", result1=result[0], result2= result[1],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   warning3="Please enter the correct name.")

# rival's team

# rival's team

# rival's team

# rival's team
    # query 4th pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('query4', None) == 'query':
        pokemon_name = flask.request.form["Pokemon_name4"]
        name = validName(pokemon_name)
        if name != 0:
            result4 = queryPokemon(name)
            result[3]=result4
            radar(result4, 'result4')
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5])
        else:
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result5 = result[4], result6 = result[5],
                                   warning4="Please enter the correct name.")
    # query 5th pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('query5', None) == 'query':
        pokemon_name = flask.request.form["Pokemon_name5"]
        name = validName(pokemon_name)
        if name != 0:
            result5 = queryPokemon(name)
            result[4]=result5
            radar(result5, 'result5')
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5])
        else:
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result6 = result[5],
                                   warning5="Please enter the correct name.")
    # query 6th pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('query6', None) == 'query':
        pokemon_name = flask.request.form["Pokemon_name6"]
        name = validName(pokemon_name)
        if name != 0:
            result6 = queryPokemon(name)
            result[5] = result6
            radar(result6, 'result6')
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5])
        else:
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4],
                                   warning6="Please enter the correct name.")

    # add 4th pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('add4', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name4"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[3] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   addation4="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html", result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   warning4="Please enter the correct name.")
    # add 5th pokrmon
    elif flask.request.method == 'POST' and flask.request.form.get('add5', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name5"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[4] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   addation5="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result6 = result[5],
                                   warning5="Please enter the correct name.")
    # add 6th pokemon
    elif flask.request.method == 'POST' and flask.request.form.get('add6', None) == 'add':
        pokemon_name = flask.request.form["Pokemon_name6"]
        name = validName(pokemon_name)
        if name != 0:
            name_list[5] = (pokemon_name)
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4], result6 = result[5],
                                   addation6="{} added".format(pokemon_name))
        else:
            return render_template("querypage.html", result1=result[0], result2= result[1], result3=result[2],
                                   result4=result[3], result5 = result[4],
                                   warning6="Please enter the correct name.")







if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4501)