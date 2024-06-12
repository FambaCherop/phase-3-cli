# recipes/recipe.py
import sqlite3

def add_recipe(name):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO recipes (name) VALUES (?)", (name,))
    recipe_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return recipe_id

def delete_recipe(recipe_id):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    connection.commit()
    connection.close()
