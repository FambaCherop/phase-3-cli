# recipes/recipe_ingredients.py
import sqlite3

def add_recipe_ingredient(recipe_id, ingredient_id, quantity):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)", (recipe_id, ingredient_id, quantity))

    connection.commit()
    connection.close()
