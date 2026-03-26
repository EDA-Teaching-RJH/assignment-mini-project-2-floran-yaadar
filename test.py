import cowsay
import re
import sys
import premade_recipe_list
from recipe_utils import Recipe, BakingRecipe, Ingredient, parse_ingredient_input
from time import sleep


def main():
    cowsay.fox("Welcome to the recipe scaler")
    sleep(1)
    open_menu()
def validate_email(email):
    email = input("please enter your email: ")
    if re.search(r".+@.+\.(ac.uk | com)$", email):
        return print (cowsay.fox("Email address is valid"))
    else: 
        return print (cowsay.fox("Sorry, that email address is not valid, please\n try again"))

def open_menu():
    cowsay.fox(" Would u like a premade recipe or would you like to create your own?")
    answer = input("[A] premade.  [B] create your own.  ").lower().strip()
    if answer == "a":
        return recipe_menu()
    elif answer == "b":
        return create_recipe()
    else:
        return cowsay.fox("Sorry that isn't a valid option, please try again.")

    
def recipe_menu():
    cowsay.fox("Here are the premade recipes")
    recipe_select = input("1. Pancakes\n2. Crepes\n3. Baked Sausage breakfast hash   ").strip().lower()
    if recipe_select == "1":
        return premade_recipe_list.pancakes()
    elif recipe_select == "2":
        return premade_recipe_list.crepes()
    elif recipe_select == "3":
        return premade_recipe_list.baked_sausage_breakfast_hash()

    
def create_recipe():
    


main()