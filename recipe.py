import re
import os

class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = float(quantity)
        self.unit = unit

    def scale(self, factor):
        return self.quantity * factor

class Recipe:
    def __init__(self, name, original_servings, ingredients, instructions):
        self.name = name
        self.original_servings = int(original_servings)
        self.ingredients = ingredients  # List of Ingredient objects
        self.instructions = instructions

    def display_scaled(self, target_servings):
        factor = target_servings / self.original_servings
        print(f"\n--- {self.name} for {target_servings} servings ---")
        for ing in self.ingredients:
            print(f"- {ing.scale(factor):.2f} {ing.unit} {ing.name}")
        print(f"\nMethod:\n{self.instructions}\n")

# REGEX PARSER
def parse_line(line):
    # Regex looks for: [Number] [Unit] [Name]
    match = re.search(r"(\d*\.?\d+)\s*(\w*)\s*(.*)", line)
    if match:
        return match.groups()
    return None

# FILE I/O 
def save_recipe_to_file(recipe_obj):
    filename = f"recipes/{recipe_obj.name.lower().replace(' ', '_')}.txt"
    os.makedirs('recipes', exist_ok=True)
    with open(filename, "w") as f:
        f.write(f"Name: {recipe_obj.name}\n")
        f.write(f"Servings: {recipe_obj.original_servings}\n")
        f.write("Ingredients:\n")
        for ing in recipe_obj.ingredients:
            f.write(f"{ing.quantity} {ing.unit} {ing.name}\n")
        f.write(f"Instructions: {recipe_obj.instructions}")