import sqlite3
import re

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

def queryID(ID):
    pokemon_info = {}
    pokemondb = sqlite3.connect("pokemon.db")
    cursor = pokemondb.cursor()
    sql = "SELECT * FROM pokemon WHERE ID <= '{}'".format(ID)
    cursor.execute(sql)
    pokemon = cursor.fetchall()
    info_key = ['ID', 'Name', 'Type1', 'Type2', 'HP', 'Attack', 'Defense', 'Sp_Atk',
                'Sp_Def', 'Speed', 'Generation', 'Legendary']

    for i in range(len(pokemon[0])):
        pokemon_info[info_key[i]] = pokemon[0][i]
    return pokemon_info
