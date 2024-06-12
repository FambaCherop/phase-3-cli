# recipes/ingredients.py
import sqlite3

def add_ingredient(name):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO ingredients (name) VALUES (?)", (name,))
    ingredient_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return ingredient_id

def delete_ingredient(ingredient_id):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM ingredients WHERE id = ?", (ingredient_id,))
    connection.commit()
    connection.close()
