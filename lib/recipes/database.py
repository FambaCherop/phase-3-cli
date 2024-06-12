# recipes/database.py
import sqlite3

def create_tables():
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS recipe_ingredients (
                        recipe_id INTEGER,
                        ingredient_id INTEGER,
                        quantity TEXT,
                        FOREIGN KEY(recipe_id) REFERENCES recipes(id),
                        FOREIGN KEY(ingredient_id) REFERENCES ingredients(id),
                        PRIMARY KEY (recipe_id, ingredient_id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS meal_plans (
                        id INTEGER PRIMARY KEY,
                        breakfast TEXT,
                        lunch TEXT,
                        dinner TEXT
                    )''')

    connection.commit()
    connection.close()
