import sqlite3
import re
import numpy as np
import matplotlib.pyplot as plt
from nn import feedforward


def getPokemonNames():
    pokemondb = sqlite3.connect("pokemon.db")
    cursor = pokemondb.cursor()

    cursor.execute("SELECT rename FROM pokemon")
    pokemon_name = cursor.fetchall()

    pokemon_names = []
    for pokemon in pokemon_name:
        name = pokemon[0]
        if name != 'rename':
            pokemon_names.append(name)

    return pokemon_names


def validName(name):
    name = name.replace(" ", "").strip().lower()
    if name in getPokemonNames():
        return name
    else:
        return 0


def queryPokemon(name):
    pokemon_info = {}
    pokemondb = sqlite3.connect("pokemon.db")
    cursor = pokemondb.cursor()
    sql = "SELECT * FROM pokemon WHERE rename = '{}'".format(name)
    cursor.execute(sql)
    pokemon = cursor.fetchall()
    info_key = ['ID', 'Name', 'rename', 'Type1', 'Type2', 'HP', 'Attack', 'Defense', 'Sp_Atk',
                'Sp_Def', 'Speed', 'Generation', 'Legendary']

    for i in range(len(pokemon[0])):
        pokemon_info[info_key[i]] = pokemon[0][i]
    return pokemon_info


def radar(result, string):
    labels = np.array(
        ['   HP', '  Atk', 'Def  ', 'Sp.    \n Atk     ', 'Sp.              \n Def               ',
         '             Speed'])
    dataLength = 6
    data = np.array([result['HP'], result["Attack"], result["Defense"],
                     result["Sp_Atk"], result["Sp_Def"], result["Speed"]])
    angles = np.linspace(0, 2 * np.pi, dataLength, endpoint=False)
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'ro-', linewidth=1)
    ax.fill(angles, data, facecolor='r', alpha=0.25)
    # colour line width, and transparency (alpha) could be changed
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontsize=24, va='bottom')
    ax.set_rlim(0, 255)
    # Max: 255 190 230 194 230 180 --> limit 255
    ax.grid(True)
    plt.savefig("static/images/{}.png".format(string))
    return
