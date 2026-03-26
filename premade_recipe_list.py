import cowsay
import anyio
from time import sleep
import sys

def pancakes():
    pancake_ingredients = ["flour", "baking powder", "sugar", "salt", "milk", "butter", "egg"]
    pancake_measurments = ["1.5", "3.5", "1", "0.25", "1.25", "3", "1"]
    pancake_scale = ["cups", "teaspoons", "tablespoons", "teaspoons", "cups", "tablespoons", ""]
    original_servings = 8
    cowsay.fox("how many servings would you like to make?")
    servings = int(input())
    pancake_measuremnts = [float(i)/original_servings for i in pancake_measurments]
    new_measurments = [i * servings for i in pancake_measuremnts]
    cowsay.fox(f"here are the ingredients for panckes\n {servings} servings ")
    for i in range(len(pancake_ingredients)):
        print (f"{pancake_ingredients[i]} {new_measurments[i]} {pancake_scale[i]} ")
    pancakes_continue_recipe()
    
def pancakes_continue_recipe():
    cowsay.fox("Would you like to to make this? ")
    continue_answer = input("[Y]es or [N]o  ").lower().strip()
    if continue_answer == "y":
        return pancakes_instructions()
    elif continue_answer == "n":
        cowsay.fox("okay, here are some of our other recipes!")
        from test import recipe_menu
        return recipe_menu()
    else:
        cowsay.fox("please enter a valid option")
        return pancakes_continue_recipe()
def pancakes_instructions():
    print("1.Sift flour, baking powder, sugar, and salt together in a large bowl. Make a well in the center and add milk, melted butter, and egg; mix until smooth.\n2. Heat a lightly oiled griddle or pan over medium-high heat. Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake; cook until bubbles form and the edges are dry, about 2 to 3 minutes.\n3. Flip and cook until browned on the other side. Repeat with remaining batter.")
    sleep(1)
    cowsay.fox("serve and ENJOY!!")
    xz = input("press enter to continue...").strip().lower()
    if xz == "a":
        return end()
    else:
        return end()
def end():
    cowsay.fox("would you like to make another recipe?")
    end_answer = input("[Y]es or [N]o").lower().strip()
    if end_answer == "y":
        from test import open_menu
        return open_menu()
    elif end_answer == "n":
        cowsay.fox("okay have a nice day! ")
    else:
        cowsay.fox("please enter a valid option")
        return end()
    
def crepes():
    crepe_ingredients = ["flour", "sugar", "salt", "eggs", "milk", "water", "oil", "butter"]
    crepe_measurments = ["250", "40", "0.25", "3", "500", "80", "2", "45"]
    crepe_scale = ["grams", "grams", "teaspoons", "", "ml", "ml", "tablespoons", "tablespoons", "grams"]
    original_servings = 15
    cowsay.fox("how many servings would you like to make?")
    servings = int(input())
    crepe_measuremnts = [float(i)/original_servings for i in crepe_measurments]
    new_measurments = [i * servings for i in crepe_measuremnts]
    cowsay.fox(f"here are the ingredients for crepes\n {servings} servings ")
    for i in range(len(crepe_ingredients)):
        print (f"{crepe_ingredients[i]} {new_measurments[i]} {crepe_scale[i]} ")
    crepes_continue_recipe()

def crepes_continue_recipe():
    cowsay.fox("Would you like to to make this? ")
    continue_answer = input("[Y]es or [N]o  ").lower().strip()
    if continue_answer == "y":
        return crepes_instructions()
    elif continue_answer == "n":
        cowsay.fox("okay, here are some of our other recipes!")
        return test.recipe_menu()
    else:
        cowsay.fox("please enter a valid option")
        return crepes_continue_recipe()
    
def crepes_instructions():
    print("FIRST MAKE THE BATTER\n1. Sift flour into a large mixing bowl. Add sugar and salt, then whisk to combine.\n2. Make a well in the centre and add the eggs. Whisk gently and only mix in a bit of the flour. You can’t blend all the flour with just the eggs yet, so just mix in enough to make a thick paste.\n3. Gradually add the milk, whisking between each addition to create a smooth batter with no lumps.\n4. Whisk in the water and oil until the batter is glossy and pourable. When you dip a spoon in, it should coat the back lightly. Not too thick, not too runny.\n5. Cover and rest for 1 hour at room temperature.\nCOOKING THE CREPES\n6. Heat a 24cm / 9.5' non-stick crêpe pan over medium-high heat (medium if your stove runs hot). If you don’t have one, any good non-stick pan will work, just adjust how much batter you pour in depending on the size, so it spreads nicely without being too thick or thin.\n7 Melt about 1/2 tsp butter, then wipe it off with a paper towel, you want just a little of butter left, no visible pools\n8. Pour the batter – Using a ladle, scoop up ¼ cup of batter, lift the pan off the heat, ladle most of the batter into the centre, and immediately swirl the pan so the batter coats the surface in a thin, even layer. Still while swirling, use the rest of the batter to fill up the empty spots before it sets. Tilting quickly gives you uniform crêpes.\n9. Cook for 45 seconds to 1 minute until the underside is lightly golden and flip using a long spatula and cook the other side for about 30 seconds.\n10. Slide onto a plate, then repeat, adding butter each time.")
    sleep(1)
    cowsay.fox("serve and ENJOY!!")
    xz = input("press enter to continue...").strip().lower()
    if xz == "a":
        return end()
    else:
        return end()


def baked_sausage_breakfast_hash():
    bsbh_ingredients = ["potatoes", "olive oil", "smoked paprika", "dried thyme", "onion powder", "garlic powder", "salt", "bell pepper", "red onion", "pinch of salt and pepper", "bacon", "sausages", "eggs", "parsley"]
    bsbh_measurments = ["800", "2", "0.5", "0.5", "0.25", "80", "2", "45"]
    bsbh_scale = ["grams", "tablespoons", "teaspoons", "teaspoons", "teaspoons", "ml", "tablespoons", "tablespoons", "grams"]
    original_servings = 15
    cowsay.fox("how many servings would you like to make?")
    servings = int(input())
    bsbh_measuremnts = [float(i)/original_servings for i in bsbh_measurments]
    new_measurments = [i * servings for i in bsbh_measuremnts]
    cowsay.fox(f"here are the ingredients for your Baked Sausage breakfast hash\n {servings} servings ")
    for i in range(len(bsbh_ingredients)):
        print (f"{bsbh_ingredients[i]} {new_measurments[i]} {bsbh_scale[i]} ")
    bsbh_continue_recipe()
