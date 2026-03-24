import cowsay
import re
import sys
import premade_recipe_list

def main():
    open_menu()
def validate_email(email):
    email = input("please enter your email: ")
    if re.search(r".+@.+\.(ac.uk | com)$", email):
        return print (cowsay.fox("Email address is valid"))
    else: 
        return print (cowsay.fox("Sorry, that email address is not valid, please\n try again"))

def open_menu():
    cowsay.fox("Welcome to the recipe scaler")
    cowsay.fox(" Would u like a premade recipe or would you like to create your own?")
    answer = input("[A] premade.  [B] create your own. ").lower().strip()
    if answer == "a":
        return recipe_menu()
    elif answer == "b":
        return create_recipe()
    else:
        return cowsay.fox("Sorry that isn't a valid option, please try again.")
    open_menu()
    
def recipe_menu():
    cowsay.fox("Here are the premade recipes")
    recipe_select = input("1. Pancakes\n2. spaghetti bolognese\n3. garlic butter chicken.")
    if recipe_select == "1":
        return premade_recipe_list.pancakes()

    
def create_recipe():
    pass

main()