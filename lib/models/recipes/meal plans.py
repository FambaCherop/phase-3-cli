# recipes/meal_plans.py
import sqlite3
import random

def create_meal_plan():
    print("Creating meal plan...")
    meals = ["Breakfast", "Lunch", "Dinner"]
    meal_plan = {meal: random.choice(["Spaghetti", "Chicken Salad", "Omelette"]) for meal in meals}
    print("Meal plan created!")
    print("Your meal plan for the day is:")
    for meal, dish in meal_plan.items():
        print(f"{meal}: {dish}")

def add_meal_plan(breakfast, lunch, dinner):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO meal_plans (breakfast, lunch, dinner) VALUES (?, ?, ?)",
                   (breakfast, lunch, dinner))
    
    connection.commit()
    connection.close()

def delete_meal_plan(meal_plan_id):
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM meal_plans WHERE id = ?", (meal_plan_id,))
    
    connection.commit()
    connection.close()
