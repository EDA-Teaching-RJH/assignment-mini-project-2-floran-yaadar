import re
import cowsay
#THE INGREDIENT CLASS 
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = float(quantity)
        self.unit = unit

    def scale(self, factor):
        """Returns the scaled quantity."""
        return self.quantity * factor

    def __str__(self):
        """How the ingredient looks when printed."""
        return f"{self.quantity:.2f} {self.unit} {self.name}"

# THE RECIPE SUPERCLASS
class Recipe:
    def __init__(self, name, original_servings, ingredients, instructions):
        self.name = name
        self.original_servings = int(original_servings)
        self.ingredients = ingredients  
        self.instructions = instructions

    def get_scaling_factor(self, target_servings):
        """Calculates the math for scaling."""
        return target_servings / self.original_servings

    def display_scaled_recipe(self, target_servings):
        """Prints the final result for the user."""
        factor = self.get_scaling_factor(target_servings)
        print(f"\n--- {self.name} ({target_servings} servings) ---")
        for ing in self.ingredients:
            scaled_qty = ing.scale(factor)
            print(f"- {scaled_qty:.2f} {ing.unit} {ing.name}")
        print(f"\nInstructions:\n{self.instructions}")

# THE BAKING RECIPE SUBCLASS 
class BakingRecipe(Recipe):
    def __init__(self, name, original_servings, ingredients, instructions, oven_temp):
        super().__init__(name, original_servings, ingredients, instructions)
        self.oven_temp = oven_temp

    def display_scaled_recipe(self, target_servings):
        print(f"!!! REMINDER: Preheat oven to {self.oven_temp}°C !!!")
        super().display_scaled_recipe(target_servings)
