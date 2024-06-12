# recipes/cli.py
from recipes.database import create_tables
from recipes.recipe import add_recipe, delete_recipe
from recipes.ingredients import add_ingredient, delete_ingredient
from recipes.recipe_ingredients import add_recipe_ingredient
from recipes.meal_plans import create_meal_plan, add_meal_plan, delete_meal_plan

def main():
    create_tables()

    while True:
        print("1. Add recipe")
        print("2. Add ingredient")
        print("3. Add ingredient to recipe")
        print("4. Delete recipe")
        print("5. Delete ingredient")
        print("6. Create meal plan")
        print("7. Add meal plan")
        print("8. Delete meal plan")
        print("9. Exit")
        
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
            create_meal_plan()
        elif choice == "7":
            breakfast = input("Enter breakfast: ")
            lunch = input("Enter lunch: ")
            dinner = input("Enter dinner: ")
            add_meal_plan(breakfast, lunch, dinner)
        elif choice == "8":
            meal_plan_id = int(input("Enter the ID of the meal plan to delete: "))
            delete_meal_plan(meal_plan_id)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Recipes, ingredients, and meal plans managed successfully!")
