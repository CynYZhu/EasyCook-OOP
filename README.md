# EasyCook

## Instruction:

The goal of this program is to navigate a player through lists of food options and let the
player to choose what food to cook. This program will prompt a recipe file of foods selected by
the player in the end.
The player shall use Python3 in command line to open the recipe.py file. This program has
four options in the main menu, including “Select food”, “View selected food and recipe”,
“Finish”, and “Help”. “Select food” guides the player to four food categories, including
“Protein”, “Veggie”, “Dessert”, and “Drink”. Each food category prompts food options and their
cooking methods for player to choose from. Based on player’s preference, a recipe will be
generated at the end of food category and the end of the program. “View selected food and
recipe” guides the player to a list of food the player already selected. “Finish” allows the player
to exit the program with a pile of recipes. “Help” directs the player to a detailed instruction file
for reference. In order to make a choice, the player should type in the number that displayed
ahead of each option; otherwise, the program will ask again for a valid number.

## Future improvement:
This program would be more efficient if food options and their cooking instructions are
stored in a more structured database. It would trigger less errors and guide the player to the
correct recipe more efficiently if options are growing. It would help if a “remove” function is
available for player to remove a selected food. This function would pair very interestingly with a
“Calorie” class, which calculates total calories of food selections. This would trigger the player
to change their food options.

## Challenges solved:
Class “Food” as the superclass contains a very important function “Choose” inherited by
all the subclasses. It renders player’s decision on each selection across all food categories very
efficiently. The class “Recipe” has functions to add header, ingredients, and instructions. Also, it
has a function “recipeOutput” to generate recipe in a dictionary format. I first tried to use list, but
it’s hard to find the title of each section. Dictionary format gives a clear structure to organize.
Class “Engine” has a class attribute related to recipe, and it stores all the recipes generated from
all food subclasses. This combination allows faster and accurate recipe generation and storage
