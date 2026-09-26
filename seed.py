import sqlite3
import json

DATABASE = 'pokemon.db'

initial_pokemon = [
    {"name": "Bulbasaur", "pokedexNumber": 1, "types": ["Grass", "Poison"]},
    {"name": "Charmander", "pokedexNumber": 4, "types": ["Fire"]},
    {"name": "Squirtle", "pokedexNumber": 7, "types": ["Water"]},
    {"name": "Pikachu", "pokedexNumber": 25, "types": ["Electric"]},
    {"name": "Gengar", "pokedexNumber": 94, "types": ["Ghost", "Poison"]},
    {"name": "Scyther", "pokedexNumber": 123, "types": ["Bug", "Flying"]},
    {"name": "Gyarados", "pokedexNumber": 130, "types": ["Water", "Flying"]},
    {"name": "Snorlax", "pokedexNumber": 143, "types": ["Normal"]},
    {"name": "Mewtwo", "pokedexNumber": 150, "types": ["Psychic"]},
    {"name": "Dragonite", "pokedexNumber": 149, "types": ["Dragon", "Flying"]},
    {"name": "Lucario", "pokedexNumber": 448, "types": ["Fighting", "Steel"]},
    {"name": "Garchomp", "pokedexNumber": 445, "types": ["Dragon", "Ground"]},
    {"name": "Gardevoir", "pokedexNumber": 282, "types": ["Psychic", "Fairy"]},
    {"name": "Rayquaza", "pokedexNumber": 384, "types": ["Dragon", "Flying"]},
    {"name": "Umbreon", "pokedexNumber": 197, "types": ["Dark"]}
]

conn = sqlite3.connect(DATABASE)
with open('schema.sql') as f:
    conn.executescript(f.read())

cursor = conn.cursor()
for p in initial_pokemon:
    cursor.execute('''
        INSERT INTO pokemon (name, pokedex_number, types)
        VALUES (?, ?, ?)
    ''', (p['name'], p['pokedexNumber'], json.dumps(p['types'])))

conn.commit()
conn.close()
print("Database initialized and populated successfully.")