Project Reflection for Recipe Scaler
Floran Yaadar

Year: 1
my aim
The goal of this project was to make a tool that actually helps in the kitchen. Most people struggle to do the math in their head when they want to make a recipe for 3 people when the recipe says 8. I wanted to build something that handles that math automatically but also lets the user save their own creations so they don't have to keep re-typing them every time.

Using OOP (Classes and Inheritance)

When I first started, I was using  parrallel lists for things like names, amounts, and units. It was a long process and i had to type out or copy out alot of the same code for each preloaded recipe. It just wasnt very efficient.

After I went back over the oop classes, I decided to refactor everything.

I made an Ingredient class to keep all the info about one item together.

In the final version of the code, I moved away from using multiple separate lists (one for names, one for amounts, etc.) and instead used Classes. I created an Ingredient class which acts as a container for the name, quantity, and unit. This made the scaling math much easier because I could just tell the ingredient to "scale itself" by a factor, rather than trying to loop through three different lists at once and hope they stayed in sync.

The Data Filtering with Regex

For the "Create Your Own" feature, I needed a way to let the user type in ingredients naturally. I used the re (Regular Expressions) library for this. My pattern (\d*\.?\d+)\s*(\w*)\s*(.*) was designed to pull out the number, the measurement unit, and the ingredient name from a single line of text.

The main challenge here was making sure it didn't crash if someone typed a whole number instead of a decimal (like "2 eggs" instead of "2.0"). By using the ? and * in my Regex, I made the parser flexible enough to handle both.

File I/O and Persistence

To make sure the recipes didn't disappear every time the program was turned off, I implemented File I/O. My save_recipe_to_file function creates a recipes/ directory if it doesn't exist and writes the object data into a .txt file.

I used the with open() syntax because it handles the file "closing" automatically. This part of the project was satisfying because it turned the script into a tool that actually saves progress, and I was slowly getting more comfortable using File i/o

Final Thoughts and Challenges

The biggest challenge was definitely the "Logic Flow"—making sure that when a user creates a recipe, it actually gets stored in a way that the Recipe class can read it back later. I also had a bit of a struggle with the float() conversion; early on, the program would crash if I tried to multiply a string by a number, so I had to make sure the Regex output was converted to a number type immediately.

If I were to do this again, I’d probably add a way to delete files from within the app, but for now, the ability to create, save, and scale recipes covers all the main goals I had for the project.

The Regex Part

The hardest part was making the "Create Recipe" feature feel natural. I didn't want the user to have to answer five different prompts for one egg.

I used Regular Expressions (Regex) to solve this. My pattern (\d*\.?\d+)\s*(\w*)\s*(.*) basically takes a whole sentence like "1.5 cups flour" and chops it into three pieces for the computer. It took me ages to get the \s* parts right so it didn't crash if someone forgot to put a space, but it makes the UI feel a lot more professional.

What I struggled with

Honestly, I spent way too much time trying to figure out the self keyword in Python. At first, I didn't understand why I had to put it in every function inside a class. I also had a nightmare with the math logic where the scaling factor was rounding down to zero because I wasn't using floats properly. I fixed this by forcing all inputs to float() before doing the multiplication.