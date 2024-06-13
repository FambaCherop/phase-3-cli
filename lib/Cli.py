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

def delete_recipe(recipe_id):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    connection.commit()
    connection.close()

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

def add_recipe_ingredient(recipe_id, ingredient_id, quantity):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)", (recipe_id, ingredient_id, quantity))

    connection.commit()
    connection.close()

def view_all_recipes():
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()

    connection.close()

    if recipes:
        print("Recipes:")
        for recipe in recipes:
            print(f"{recipe[0]}. {recipe[1]}")
    else:
        print("No recipes found.")

def view_all_ingredients():
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM ingredients")
    ingredients = cursor.fetchall()

    connection.close()

    if ingredients:
        print("Ingredients:")
        for ingredient in ingredients:
            print(f"{ingredient[0]}. {ingredient[1]}")
    else:
        print("No ingredients found.")

def view_ingredients_of_recipe(recipe_id):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT ingredients.name, recipe_ingredients.quantity
                      FROM recipe_ingredients
                      JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.id
                      WHERE recipe_ingredients.recipe_id = ?''', (recipe_id,))
    ingredients = cursor.fetchall()

    connection.close()

    if ingredients:
        print(f"Ingredients for recipe ID {recipe_id}:")
        for ingredient in ingredients:
            print(f"{ingredient[0]} - {ingredient[1]}")
    else:
        print(f"No ingredients found for recipe ID {recipe_id}.")

def update_recipe_name(recipe_id, new_name):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE recipes SET name = ? WHERE id = ?", (new_name, recipe_id))

    connection.commit()
    connection.close()

def update_ingredient_name(ingredient_id, new_name):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE ingredients SET name = ? WHERE id = ?", (new_name, ingredient_id))

    connection.commit()
    connection.close()

def main():
    create_tables()

    while True:
        print("1. Add recipe")
        print("2. Add ingredient")
        print("3. Add ingredient to recipe")
        print("4. Delete recipe")
        print("5. Delete ingredient")
        print("6. View all recipes")
        print("7. View all ingredients")
        print("8. View ingredients of a recipe")
        print("9. Update recipe name")
        print("10. Update ingredient name")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the recipe: ")
            add_recipe(name)
        elif choice == "2":
            name = input("Enter the name of the ingredient: ")
            add_ingredient(name)
        elif choice == "3":
            recipe_id = int(input("Enter the ID of the recipe: "))
            ingredient_id = int(input("Enter the ID of the ingredient: "))
            quantity = input("Enter the quantity: ")
            add_recipe_ingredient(recipe_id, ingredient_id, quantity)
        elif choice == "4":
            recipe_id = int(input("Enter the ID of the recipe to delete: "))
            delete_recipe(recipe_id)
        elif choice == "5":
            ingredient_id = int(input("Enter the ID of the ingredient to delete: "))
            delete_ingredient(ingredient_id)
        elif choice == "6":
            view_all_recipes()
        elif choice == "7":
            view_all_ingredients()
        elif choice == "8":
            recipe_id = int(input("Enter the ID of the recipe: "))
            view_ingredients_of_recipe(recipe_id)
        elif choice == "9":
            recipe_id = int(input("Enter the ID of the recipe: "))
            new_name = input("Enter the new name of the recipe: ")
            update_recipe_name(recipe_id, new_name)
        elif choice == "10":
            ingredient_id = int(input("Enter the ID of the ingredient: "))
            new_name = input("Enter the new name of the ingredient: ")
            update_ingredient_name(ingredient_id, new_name)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Recipes and ingredients managed successfully!")

if __name__ == "__main__":
    main()
