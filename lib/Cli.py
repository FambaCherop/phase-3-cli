# import sqlite3
# import random

# def create_tables():
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT
#                     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT
#                     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS recipe_ingredients (
#                         recipe_id INTEGER,
#                         ingredient_id INTEGER,
#                         quantity TEXT,
#                         FOREIGN KEY(recipe_id) REFERENCES recipes(id),
#                         FOREIGN KEY(ingredient_id) REFERENCES ingredients(id),
#                         PRIMARY KEY (recipe_id, ingredient_id)
#                     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS meal_plans (
#                         id INTEGER PRIMARY KEY,
#                         breakfast TEXT,
#                         lunch TEXT,
#                         dinner TEXT
#                     )''')

#     connection.commit()
#     connection.close()

# def add_recipe(name):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("INSERT INTO recipes (name) VALUES (?)", (name,))
#     recipe_id = cursor.lastrowid

#     connection.commit()
#     connection.close()

#     return recipe_id

# def add_ingredient(name):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("INSERT INTO ingredients (name) VALUES (?)", (name,))
#     ingredient_id = cursor.lastrowid

#     connection.commit()
#     connection.close()

#     return ingredient_id

# def add_recipe_ingredient(recipe_id, ingredient_id, quantity):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)", (recipe_id, ingredient_id, quantity))

#     connection.commit()
#     connection.close()

# def delete_recipe(recipe_id):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
#     connection.commit()
#     connection.close()

# def delete_ingredient(ingredient_id):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("DELETE FROM ingredients WHERE id = ?", (ingredient_id,))
#     connection.commit()
#     connection.close()

# def create_meal_plan():
#     print("Creating meal plan...")
#     # Placeholder meal plan generation logic
#     meals = ["Breakfast", "Lunch", "Dinner"]
#     meal_plan = {meal: random.choice(["Spaghetti", "Chicken Salad", "Omelette"]) for meal in meals}
#     print("Meal plan created!")
#     print("Your meal plan for the day is:")
#     for meal, dish in meal_plan.items():
#         print(f"{meal}: {dish}")

# def add_meal_plan(breakfast, lunch, dinner):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("INSERT INTO meal_plans (breakfast, lunch, dinner) VALUES (?, ?, ?)",
#                    (breakfast, lunch, dinner))
    
#     connection.commit()
#     connection.close()

# def delete_meal_plan(meal_plan_id):
#     connection = sqlite3.connect('recipes.db')
#     cursor = connection.cursor()

#     cursor.execute("DELETE FROM meal_plans WHERE id = ?", (meal_plan_id,))
    
#     connection.commit()
#     connection.close()

# def main():
#     create_tables()

#     while True:
#         print("1. Add recipe")
#         print("2. Add ingredient")
#         print("3. Add ingredient to recipe")
#         print("4. Delete recipe")
#         print("5. Delete ingredient")
#         print("6. Create meal plan")
#         print("7. Add meal plan")
#         print("8. Delete meal plan")
#         print("9. Exit")
        
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Enter the name of the recipe: ")
#             add_recipe(name)
#         elif choice == "2":
#             name = input("Enter the name of the ingredient: ")
#             add_ingredient(name)
#         elif choice == "3":
#             recipe_id = int(input("Enter the ID of the recipe: "))
#             ingredient_id = int(input("Enter the ID of the ingredient: "))
#             quantity = input("Enter the quantity: ")
#             add_recipe_ingredient(recipe_id, ingredient_id, quantity)
#         elif choice == "4":
#             recipe_id = int(input("Enter the ID of the recipe to delete: "))
#             delete_recipe(recipe_id)
#         elif choice == "5":
#             ingredient_id = int(input("Enter the ID of the ingredient to delete: "))
#             delete_ingredient(ingredient_id)
#         elif choice == "6":
#             create_meal_plan()
#         elif choice == "7":
#             breakfast = input("Enter breakfast: ")
#             lunch = input("Enter lunch: ")
#             dinner = input("Enter dinner: ")
#             add_meal_plan(breakfast, lunch, dinner)
#         elif choice == "8":
#             meal_plan_id = int(input("Enter the ID of the meal plan to delete: "))
#             delete_meal_plan(meal_plan_id)
#         elif choice == "9":
#             break
#         else:
#             print("Invalid choice. Please try again.")

#     print("Recipes, ingredients, and meal plans managed successfully!")

# if __name__ == "__main__":
#     main()
