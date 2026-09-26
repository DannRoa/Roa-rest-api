import sqlite3
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = 'pokemon.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db_if_missing():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        with open('schema.sql') as f:
            conn.executescript(f.read())
        conn.close()

init_db_if_missing()

def format_pokemon(row):
    return {
        "id": row["id"],
        "name": row["name"],
        "pokedexNumber": row["pokedex_number"],
        "types": json.loads(row["types"])
    }

@app.route('/api/pokemon', methods=['GET'])
def get_all_pokemon():
    conn = get_db_connection()
    cursor = conn.cursor()
    rows = cursor.execute('SELECT * FROM pokemon').fetchall()
    conn.close()
    return jsonify([format_pokemon(row) for row in rows]), 200

@app.route('/api/pokemon/<int:item_id>', methods=['GET'])
def get_single_pokemon(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM pokemon WHERE id = ?', (item_id,)).fetchone()
    conn.close()

    if row is None:
        return jsonify({"error": "Pokemon not found"}), 404

    return jsonify(format_pokemon(row)), 200

@app.route('/api/pokemon', methods=['POST'])
def create_pokemon():
    data = request.get_json()

    if not data or not all(k in data for k in ("name", "pokedexNumber", "types")):
        return jsonify({"error": "Missing required fields: name, pokedexNumber, and types are required."}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pokemon (name, pokedex_number, types)
        VALUES (?, ?, ?)
    ''', (
        data['name'],
        data['pokedexNumber'],
        json.dumps(data['types'])
    ))
    
    new_id = cursor.lastrowid
    conn.commit()
    created_row = cursor.execute('SELECT * FROM pokemon WHERE id = ?', (new_id,)).fetchone()
    conn.close()

    return jsonify(format_pokemon(created_row)), 201

@app.route('/api/pokemon/<int:item_id>', methods=['PUT'])
def update_pokemon(item_id):
    data = request.get_json()

    if not data or not all(k in data for k in ("name", "pokedexNumber", "types")):
        return jsonify({"error": "Validation failed: name, pokedexNumber, and types are required."}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    existing = cursor.execute('SELECT id FROM pokemon WHERE id = ?', (item_id,)).fetchone()
    
    if existing is None:
        conn.close()
        return jsonify({"error": "Pokemon not found"}), 404

    cursor.execute('''
        UPDATE pokemon
        SET name = ?, pokedex_number = ?, types = ?
        WHERE id = ?
    ''', (
        data['name'],
        data['pokedexNumber'],
        json.dumps(data['types']),
        item_id
    ))
    
    conn.commit()
    updated_row = cursor.execute('SELECT * FROM pokemon WHERE id = ?', (item_id,)).fetchone()
    conn.close()

    return jsonify(format_pokemon(updated_row)), 200

@app.route('/api/pokemon/<int:item_id>', methods=['DELETE'])
def delete_pokemon(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    row = cursor.execute('SELECT * FROM pokemon WHERE id = ?', (item_id,)).fetchone()
    if row is None:
        conn.close()
        return jsonify({"error": "Pokemon not found"}), 404

    cursor.execute('DELETE FROM pokemon WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Pokemon successfully deleted", "deletedItem": format_pokemon(row)}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)