import unittest
from recipe import Ingredient

class TestRecipeMath(unittest.TestCase):
    def test_scaling(self):
        # Test if 2 cups scaled by 2 becomes 4 cups
        ing = Ingredient("Flour", 2, "cups")
        self.assertEqual(ing.scale(2), 4.0)
        
    def test_zero_scaling(self):
        # Test if scaling by 0 works (edge case)
        ing = Ingredient("Sugar", 10, "grams")
        self.assertEqual(ing.scale(0), 0.0)

if __name__ == '__main__':
    unittest.main()