import cowsay
import sys
from time import sleep
from recipe import Ingredient, Recipe, parse_line, save_recipe_to_file

def main():
    cowsay.fox("Welcome to the recipe scaler")
    sleep(1)
    open_menu()

def open_menu():
    cowsay.fox("Would u like a premade recipe or would you like to create your own?")
    answer = input("[A] Premade  [B] Create Your Own  [Q] Quit\n> ").lower().strip()
    
    if answer == "a":
        recipe_menu()
    elif answer == "b":
        create_recipe()
    elif answer == "q":
        cowsay.fox("Happy cooking! Goodbye!")
        sys.exit()
    else:
        cowsay.fox("Invalid option, try again.")
        open_menu()

def recipe_menu():
    # --- DATA INTEGRATION: YOUR ORIGINAL RECIPES AS OOP OBJECTS ---
    
    # 1. PANCAKES
    pancakes = Recipe(
        "Pancakes", 8, 
        [
            Ingredient("flour", 1.5, "cups"),
            Ingredient("baking powder", 3.5, "teaspoons"),
            Ingredient("sugar", 1, "tablespoons"),
            Ingredient("salt", 0.25, "teaspoons"),
            Ingredient("milk", 1.25, "cups"),
            Ingredient("butter", 3, "tablespoons"),
            Ingredient("egg", 1, "")
        ],
        "1. Sift dry ingredients. 2. Add milk, butter, egg. 3. Fry 2-3 mins per side."
    )

    # 2. CREPES
    crepes = Recipe(
        "Crepes", 15,
        [
            Ingredient("flour", 250, "grams"),
            Ingredient("sugar", 40, "grams"),
            Ingredient("salt", 0.25, "teaspoons"),
            Ingredient("eggs", 3, ""),
            Ingredient("milk", 500, "ml"),
            Ingredient("water", 80, "ml"),
            Ingredient("oil", 2, "tablespoons"),
            Ingredient("butter", 45, "tablespoons")
        ],
        "1. Whisk flour, sugar, salt. 2. Add eggs then liquids gradually. 3. Rest 1hr. 4. Cook thin layers."
    )

    # 3. BREAKFAST HASH
    hash_recipe = Recipe(
        "Baked Sausage Breakfast Hash", 15,
        [
            Ingredient("potatoes", 800, "grams"),
            Ingredient("olive oil", 2, "tablespoons"),
            Ingredient("smoked paprika", 0.5, "teaspoons"),
            Ingredient("bacon", 100, "grams"),
            Ingredient("sausages", 500, "grams"),
            Ingredient("eggs", 1, "count")
        ],
        "1. Bake potatoes with oil/spices (200°C) 15m. 2. Add veg/meat, bake 35m. 3. Add eggs, bake 7m."
    )

    cowsay.fox("Select a recipe:")
    print("1. Pancakes\n2. Crepes\n3. Baked Sausage Breakfast Hash")
    choice = input("> ").strip()

    # Logic to pick the object
    selected = None
    if choice == "1": selected = pancakes
    elif choice == "2": selected = crepes
    elif choice == "3": selected = hash_recipe

    if selected:
        cowsay.fox(f"How many servings of {selected.name}?")
        try:
            servings = int(input("> "))
            selected.display_scaled(servings) # The Class handles the math!
            
            # OPTIONAL: Save the scaled version to a file (Extra File I/O Marks!)
            save_choice = input("Save this scaled version to a file? (y/n): ").lower()
            if save_choice == 'y':
                save_recipe_to_file(selected) 
                
            input("\nPress Enter to return to menu...")
            open_menu()
        except ValueError:
            print("Please enter a valid number.")
            recipe_menu()
    else:
        open_menu()

def create_recipe():
    # ... (Keep the create_recipe code from the previous response) ...
    pass

if __name__ == "__main__":
    main()