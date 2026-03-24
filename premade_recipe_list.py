import cowsay
def pancakes():
    ingredients = ["flour", "baking powder", "sugar", "salt", "milk", "butter", "egg"]
    measurments = ["1.5", "3.5", "1", "0.25", "1.25", "3", "1"]
    scale = ["cups", "teaspoons", "tablespoons", "teaspoons", "cups", "tablespoons", ""]
    original_servings = 8
    cowsay.fox("how many servings would you like to make?")
    servings = int(input())
    measuremnts = [float(i)/original_servings for i in measurments]
    new_measurments = [i * servings for i in measuremnts]
    cowsay.fox(f"here are the ingredients for panckes\n {servings} servings ")
    for i in range(len(ingredients)):
        print (f"{ingredients[i]} {new_measurments[i]} {scale[i]} ")
    continue_recipe()
    
def continue_recipe():
    cowsay.fox("Would you liketo to make this? ")
    continue_answer = input("[Y]es or [N]o  ").lower().strip()
    if continue_answer == "y":
        return pancakes_instructions()
    elif continue_answer == "n":
        cowsay.fox("okay, here are some of our other recipes!")
        return recipe_menu()
    else:
        cowsay.fox("please enter a valid option")
        return continue_recipe()
def pancakes_instructions():
    print("1.Sift flour, baking powder, sugar, and salt together in a large bowl. Make a well in the center and add milk, melted butter, and egg; mix until smooth.\n2. Heat a lightly oiled griddle or pan over medium-high heat. Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake; cook until bubbles form and the edges are dry, about 2 to 3 minutes.\n3. Flip and cook until browned on the other side. Repeat with remaining batter.")
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
        return open_menu()
    elif end_answer == "n":
        cowsay.fox("okay have a nice day! ")
    else:
        cowsay.fox("please enter a valid option")
        return end()
    

    