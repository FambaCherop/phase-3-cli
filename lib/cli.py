# lib/cli.py

# from helpers import (
#     exit_program,
#     helper_1
# )


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()

import click
from .db import Session, Recipe, Ingredient, RecipeIngredient

# Define CLI commands using Click
@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def add_recipe(name):
    session = Session()
    recipe = Recipe(name=name)
    session.add(recipe)
    session.commit()
    click.echo(f"Recipe '{name}' added successfully!")
    session.close()

@cli.command()
@click.argument('name')
def add_ingredient(name):
    session = Session()
    ingredient = Ingredient(name=name)
    session.add(ingredient)
    session.commit()
    click.echo(f"Ingredient '{name}' added successfully!")
    session.close()

@cli.command()
@click.argument('recipe_id', type=int)
@click.argument('ingredient_id', type=int)
@click.argument('quantity')
def add_recipe_ingredient(recipe_id, ingredient_id, quantity):
    session = Session()
    recipe = session.query(Recipe).get(recipe_id)
    ingredient = session.query(Ingredient).get(ingredient_id)
    if recipe and ingredient:
        recipe_ingredient = RecipeIngredient(recipe_id=recipe_id, ingredient_id=ingredient_id, quantity=quantity)
        session.add(recipe_ingredient)
        session.commit()
        click.echo(f"Ingredient '{ingredient.name}' added to recipe '{recipe.name}' with quantity '{quantity}' successfully!")
    else:
        click.echo("Recipe or ingredient not found!")
    session.close()

if __name__ == '__main__':
    cli()
