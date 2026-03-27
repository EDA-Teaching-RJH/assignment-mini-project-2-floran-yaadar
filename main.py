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
    # 1. PANCAKES 
    pancake_instr = (
        "1. Sift flour, baking powder, sugar, and salt together in a large bowl. "
        "Make a well in the center and add milk, melted butter, and egg; mix until smooth.\n"
        "2. Heat a lightly oiled griddle or pan over medium-high heat. Pour or scoop the batter "
        "onto the griddle, using approximately 1/4 cup for each pancake; cook until bubbles form "
        "and the edges are dry, about 2 to 3 minutes.\n"
        "3. Flip and cook until browned on the other side. Repeat with remaining batter."
    )
    pancakes = Recipe("Pancakes", 8, [
        Ingredient("flour", 1.5, "cups"),
        Ingredient("baking powder", 3.5, "teaspoons"),
        Ingredient("sugar", 1, "tablespoons"),
        Ingredient("salt", 0.25, "teaspoons"),
        Ingredient("milk", 1.25, "cups"),
        Ingredient("butter", 3, "tablespoons"),
        Ingredient("egg", 1, "")
    ], pancake_instr)

    # 2. CREPES 
    crepe_instr = (
        "FIRST MAKE THE BATTER\n"
        "1. Sift flour into a large mixing bowl. Add sugar and salt, then whisk to combine.\n"
        "2. Make a well in the centre and add the eggs. Whisk gently and only mix in a bit of the flour...\n"
        "3. Gradually add the milk, whisking between each addition to create a smooth batter...\n"
        "4. Whisk in the water and oil until the batter is glossy and pourable.\n"
        "5. Cover and rest for 1 hour at room temperature.\n"
        "COOKING THE CREPES\n"
        "6. Heat a 24cm non-stick crêpe pan over medium-high heat.\n"
        "7. Melt butter, then wipe it off with a paper towel.\n"
        "8. Pour the batter – lift the pan off the heat, ladle batter into the centre, and swirl.\n"
        "9. Cook for 45 seconds to 1 minute until golden, flip and cook for 30 seconds."
    )
    crepes = Recipe("Crepes", 15, [
        Ingredient("flour", 250, "grams"),
        Ingredient("sugar", 40, "grams"),
        Ingredient("salt", 0.25, "teaspoons"),
        Ingredient("eggs", 3, ""),
        Ingredient("milk", 500, "ml"),
        Ingredient("water", 80, "ml"),
        Ingredient("oil", 2, "tablespoons"),
        Ingredient("butter", 45, "tablespoons")
    ], crepe_instr)

    # 3. BREAKFAST HASH 
    hash_instr = (
        "1. Preheat the oven to 200°C / 400°F (180°C fan-forced).\n"
        "2. Toss the potatoes with the oil and seasoning in a bowl. Bake for 15 minutes.\n"
        "3. Capsicum and onion – toss with oil, salt and pepper. Add to tray.\n"
        "4. Sausage & bacon – Squeeze dollops of sausage meat out and dot them on top. Scatter bacon.\n"
        "5. Bake 35 minutes.\n"
        "6. Lower oven to 180°C/350°F.\n"
        "7. Eggs – Push potato aside to make holes. Crack eggs in. Bake for 7 minutes.\n"
        "8. Scatter with parsley."
    )
    hash_recipe = Recipe("Baked Sausage Breakfast Hash", 15, [
        Ingredient("potatoes", 800, "grams"),
        Ingredient("olive oil", 2, "tablespoons"),
        Ingredient("smoked paprika", 0.5, "teaspoons"),
        Ingredient("dried thyme", 0.5, "teaspoons"),
        Ingredient("onion powder", 0.25, "teaspoons"),
        Ingredient("garlic powder", 0.25, "teaspoons"),
        Ingredient("salt", 0.5, "teaspoons"),
        Ingredient("bell pepper", 1, ""),
        Ingredient("red onion", 1, ""),
        Ingredient("bacon", 100, "grams"),
        Ingredient("sausages", 500, "grams"),
        Ingredient("eggs", 1, "count"),
        Ingredient("parsley", 1, "tablespoon")
    ], hash_instr)

    cowsay.fox("Select a recipe:")
    print("1. Pancakes\n2. Crepes\n3. Baked Sausage Breakfast Hash")
    choice = input("> ").strip()


    selected = None
    if choice == "1": selected = pancakes
    elif choice == "2": selected = crepes
    elif choice == "3": selected = hash_recipe

    if selected:
        cowsay.fox(f"How many servings of {selected.name}?")
        try:
            servings = int(input("> "))
            selected.display_scaled(servings) 
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
    cowsay.fox("Awesome! Let's create a new custom recipe.")
    name = input("What is the name of your recipe?\n> ").strip()
    while True:
        try:
            servings = int(input(f"How many people does {name} originally serve?\n> "))
            break
        except ValueError:
            print("Oops! Please enter a whole number (e.g., 4).")

    ingredients_list = []
    cowsay.fox("Enter ingredients one by one (e.g., '1.5 cups flour'). Type 'done' when finished.")
    
    while True:
        line = input("Ingredient: ").strip()
        if line.lower() == 'done':
            if len(ingredients_list) > 0:
                break
            else:
                print("You need to add at least one ingredient!")
                continue
        parsed = parse_line(line) 
        if parsed:
            qty, unit, ing_name = parsed
            ingredients_list.append(Ingredient(ing_name, qty, unit))
            print(f"  [+] Added: {ing_name}")
        else:
            print("  [!] Invalid format. Please use: [Number] [Unit] [Name] (e.g., 200 grams sugar)")

    cowsay.fox("Now, enter the cooking instructions. Type 'done' when finished.")
    instructions_text = ""
    step_num = 1
    
    while True:
        step = input(f"Step {step_num}: ").strip()
        if step.lower() == 'done':
            break
        instructions_text += f"{step_num}. {step}\n" 
        step_num += 1
    new_recipe = Recipe(name, servings, ingredients_list, instructions_text)
    
    save_recipe_to_file(new_recipe)
    
    cowsay.fox(f"Success! '{name}' has been saved to your recipes folder.")
    input("\nPress Enter to return to the main menu...")
    open_menu()
    
    pass

if __name__ == "__main__":
    main()