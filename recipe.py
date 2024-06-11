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

    connection.commit()
    connection.close()

def add_recipe(name):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO recipes (name) VALUES (?)", (name,))
    recipe_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return recipe_id

def add_ingredient(name):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO ingredients (name) VALUES (?)", (name,))
    ingredient_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return ingredient_id

def add_recipe_ingredient(recipe_id, ingredient_id, quantity):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)", (recipe_id, ingredient_id, quantity))

    connection.commit()
    connection.close()

def main():
    create_tables()

    # Add recipes
    recipe_id1 = add_recipe("Spaghetti Carbonara")
    recipe_id2 = add_recipe("Chicken Stir-Fry")
    recipe_id3 = add_recipe("Vegetable Soup")

    # Add ingredients
    ingredient_id1 = add_ingredient("Spaghetti")
    ingredient_id2 = add_ingredient("Bacon")
    ingredient_id3 = add_ingredient("Eggs")
    ingredient_id4 = add_ingredient("Parmesan Cheese")
    ingredient_id5 = add_ingredient("Chicken Breast")
    ingredient_id6 = add_ingredient("Vegetables")
    ingredient_id7 = add_ingredient("Chicken Broth")

    # Add recipe ingredients
    add_recipe_ingredient(recipe_id1, ingredient_id1, "200g")
    add_recipe_ingredient(recipe_id1, ingredient_id2, "100g")
    add_recipe_ingredient(recipe_id1, ingredient_id3, "2")
    add_recipe_ingredient(recipe_id1, ingredient_id4, "50g")

    add_recipe_ingredient(recipe_id2, ingredient_id1, "250g")
    add_recipe_ingredient(recipe_id2, ingredient_id5, "300g")
    add_recipe_ingredient(recipe_id2, ingredient_id6, "Assorted")

    add_recipe_ingredient(recipe_id3, ingredient_id6, "Assorted")
    add_recipe_ingredient(recipe_id3, ingredient_id7, "1L")

    print("Recipes and ingredients added successfully!")

if __name__ == "__main__":
    main()
