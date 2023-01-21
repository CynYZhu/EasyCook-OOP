from os import system, name
from copy import deepcopy


class Food:
    """Superclass Food has basic functions for player to make choice. """

    def __init__(self):
        self.food_choice_list = None
        self.cooking_methods = None

        self.decision = int()

    def choose(self, option_list):
        self.option_list = option_list
        choices = []

        for i in range(0, len(self.option_list)):
            print("[{}] {}.".format((i + 1), self.option_list[i]))
            choices += [str(i + 1)]

        while True:
            choice = input("Please choose one of the followings.")
            if choice not in choices:
                print("You must choose a number corresponding to the choices given.")
            #                 continue
            else:
                break
        self.decision = int(choice) - 1
        return self.decision


    def remove_selected_food(self):
        pass

class Protein(Food):
    """ Subclass Class protein has four possible instances.
    Based on the choice that player makes, it leads to different further options."""

    def __init__(self):
        super().__init__()
        self.food_choice_list = ["12oz New York Steak", "12oz Atlantic Salmon", "Roasted Chicken", "BBQ Pulled Port",
                                 "Pass"]
        self.cooking_methods = ["Well Done", "Medium", "Medium Rare", "Rare"]
        self.confirmation = ["Yes", "No"]
        self.cooking_time = {"1": 6, "2": 5, "3": 4, "4": 3}
        self.choose_protein()

    def choose_protein(self):
        self.choose(self.food_choice_list)

        if self.decision == 5:  # choice is pass
            pass

        elif self.decision == 0:  # choice is tofu
            print("How do you like your {}?".format(self.food_choice_list[self.decision]))
            self.decision = None
            self.choose(self.cooking_methods)

            cook_steak_instruction = "You would need to sear each side of your 2 cm steak for {} minutes.".format(
                self.cooking_time[str(self.decision + 1)])
            print(cook_steak_instruction)
            print("Don't worry, all details will be added to your instructions.")

            # inicialize and add header to the recipe of steak
            cook_steak_recipe = Recipe()
            cook_steak_recipe.add_header("New York Steak with Garlic Butter")

            # add ingredient to the recipe of steak
            cook_steak_recipe.add_ingredient(["12oz New York Steak", "10mL of olive oil", "Some garlics.",
                                              "5g of Ground Black Pepper", "5g of Kosher Salt",
                                              "15g of unsalted butter"])

            # add instructions to recipe
            rinse_instruction = "Let's give it a rinse first, dry and sit at room temperature for 30 mins."
            cook_steak_recipe.add_instruction([rinse_instruction,
                                               "Sprinkle Kosher salts and black pepper to your steak while sitting.",
                                               "Heat a large cast-iron skillet over high heat. Add oil to pan; swirl to coat. ",
                                               cook_steak_instruction,
                                               "Remove it from pan; cover loosely with foil. Let stand 10 minutes."])
            
            enter = input("There will be a final recipe generated for you in the end. Please press Enter to continue.")
            cook_steak_recipe.recipeOutput()
            Engine.recipe_of_selected_food["New York Steak with Garlic Butter"] = cook_steak_recipe

        elif self.decision == 1:  # choice is steak
            print("How do you like your {}?".format(self.food_choice_list[self.decision]))
            self.choose(self.cooking_methods)

            cook_salmon_instruction = "You would need to sear each side of your 2 cm salmon for {} minutes.".format(
                self.cooking_time[str(self.decision + 1)])
            print(cook_salmon_instruction)
            print("Don't worry, all details will be added to your instructions.")

            # inicialize and add header to the recipe of steak
            cook_salmon_recipe = Recipe()
            cook_salmon_recipe.add_header("Lemony Atlantic Salmon Fillets")

            # add ingredient to the recipe of steak
            cook_salmon_recipe.add_ingredient(
                [self.food_choice_list[self.decision], "10mL of olive oil", "10mL of fresh Lemon Juice",
                 "2g of Ground Black Pepper", "2g of Kosher Salt", "5g of unsalted butter"])

            # add instructions to recipe
            rinse_instruction = "Let's give it a rinse first, dry and sit at room temperature for 30 mins."
            cook_salmon_recipe.add_instruction([rinse_instruction,
                                                "Sprinkle Kosher salts and black pepper to your salmon while sitting, and pour 5mL of lemon juice to it as well.",
                                                "Heat a large cast-iron skillet over high heat. Add oil to pan; swirl to coat. ",
                                                cook_salmon_instruction,
                                                "Remove it from pan; cover loosely with foil. Let stand 5 minutes.",
                                                "Add the rest of lemon juice to the seared salmon. Enjoy!"])
            
            enter = input(
                "There will be a final recipe generated for you in the end. Here is a sneak peak. Please press Enter to continue.")
            cook_salmon_recipe.recipeOutput()
            Engine.recipe_of_selected_food["Lemony Atlantic Salmon Fillets"] = cook_salmon_recipe

        elif self.decision == 2:  # choice is Roasted Chicken
            print("Nice choice! You got a whole Roasted Chicken from Costco!")
            enter = input("Please press Enter to continue.")
            Engine.clear()
            print("It is very easy to prepare. Heat your oven to 375F and toss it in to warm up for 20mins. You are good to go!")
            enter = input("Please press Enter to continue.")
            Engine.clear()

            print("Would you like to challenge yourself to cook something? Try steak or salmon!")
            self.choose(self.confirmation)

            if self.decision == 0:
                Protein()
            else:
               pass

        elif self.decision == 3:  # choice is pork
            print("Nice choice! You got a pack of BBQ pulled pork from Costco!")
            enter = input("Please press Enter to continue.")
            Engine.clear()
            print("It is very easy to prepare. Heat your oven to 375F and toss it in to warm up for 20mins. You are good to go!")
            enter = input("Please press Enter to continue.")
            Engine.clear()

            print("Would you like to challenge yourself to cook something? Try steak or salmon!")
            self.choose(self.confirmation)
            if self.decision == 0:
                Protein()
            else:
                pass

class Veggie(Food):
    """ Subclass Class protein has four possible instances.
    Based on the choice that player makes, it leads to different further options."""

    def __init__(self):
        super().__init__()
        self.food_choice_list = ["Crispy Tofu Bites", "Brussels Sprouts", "Broccoli", "Mushroom", "Pass"]
        self.baking_methods = ["Baked", "Pan-seared"]
        self.confirmation = ["Yes", "No"]
        self.choose_veggie()

    def choose_veggie(self):
        self.choose(self.food_choice_list)
        food_int = deepcopy(self.decision)

        if self.decision == 4:  # choice is pass
            pass

        elif self.decision == 0:  # choice is tofu
            print("How do you want to cook your {}?".format(self.food_choice_list[self.decision]))
            self.decision = int()
            self.choose(self.baking_methods)

            if self.decision == 0:
                prep_bake_instruction = "Turn your oven to 375F 15 minutes before further preparation."
                print(prep_bake_instruction)

            elif self.decision == 1:
                prep_bake_instruction = "Prepare a large cast-iron skillet over high heat."
                print(prep_bake_instruction)

            print("Don't worry, all details will be added to your instructions.")

            # inicialize and add header to the recipe of steak
            tofu_recipe = Recipe()
            tofu_recipe.add_header("Crispy Tofu Bites")

            # add ingredient to the recipe of steak
            tofu_recipe.add_ingredient(["One box of tofu", "10mL of olive oil", "Teriyaki sause",
                                        "Minced scallion", "1g of Kosher Salt", "3g of Cornstarch"])

            # add instructions to recipe
            rinse_instruction = "Cut the tofu to smaller cubes. Let's give it a rinse under water, dry and sit at room temperature for 30 mins."
            tofu_recipe.add_instruction([rinse_instruction,
                                         "Add the cornstarch to coat the cubes, then add teriyaki sauce and olive oil.",
                                         "Move all the tofu to the large cast-iron. ",
                                         prep_bake_instruction])
            if self.decision == 0:
                tofu_recipe.add_instruction(["Put cast iron into oven for 20 mins."])
            else:
                tofu_recipe.add_instruction(["Heat the cast iron pan on stove and flip side after 2 mins."])

            tofu_recipe.add_instruction(["After each side is nice and brown, take them off heat and ready to serve."])
            Engine.clear()
            enter = input("There will be a final recipe generated for you in the end. Here is a sneak peak. Please press Enter to continue.")
            tofu_recipe.recipeOutput()
            Engine.recipe_of_selected_food["Crispy Tofu Bites"] = tofu_recipe

        elif self.decision == 1:  # choice is sprouts
            print("How do you want to cook your {}?".format(self.food_choice_list[self.decision]))
            self.decision = int()
            self.choose(self.baking_methods)

            if self.decision == 0:
                prep_bake_instruction = "Turn your oven to 375F 15 minutes before further preparation."
                print(prep_bake_instruction)

            elif self.decision == 1:
                prep_bake_instruction = "Prepare a a large cast-iron skillet over high heat."
                print(prep_bake_instruction)

            print("Don't worry, all details will be added to your instructions.")

            # inicialize and add header to the recipe
            sprouts_recipe = Recipe()
            sprouts_recipe.add_header("Brussels Sprouts")

            # add ingredient to the recipe
            sprouts_recipe.add_ingredient(["20oz of Brussels Sprouts", "15mL of olive oil", "Kosher salt",
                                           "10 mL of water", "2g of ground black pepper", "2g of minced garlic"])

            # add instructions
            rinse = "Let's give it a rinse under water, dry and sit at room temperature for 30 mins."
            sprouts_recipe.add_instruction([rinse,
                                            "Add all seasonings to the sprouts.",
                                            "Massage and evenly spread all seasonings. ",
                                            prep_bake_instruction])
            if self.decision == 0:
                sprouts_recipe.add_instruction(["Put cast iron into oven for 20 mins."])
            else:
                sprouts_recipe.add_instruction(["Heat the cast iron pan on stove and flip side after 3 mins."])

            sprouts_recipe.add_instruction(["After sprouts are crispy outside,take them off heat and ready to serve."])
            Engine.clear()
            enter = input("There will be a final recipe generated for you in the end. Here is a sneak peak. Please press Enter to continue.")
            sprouts_recipe.recipeOutput()
            Engine.recipe_of_selected_food["Brussels Sprouts"] = sprouts_recipe

        elif self.decision == 2 or 3:  # choice is Brocolli or mushroom
            print("Very nice choice, so healthy!")
            print("You got a box of {} from Costco!".format(self.food_choice_list[self.decision]))
            enter = input("Please press Enter to continue.")
            Engine.clear()
            print("It is very easy to prepare. First boil a pot of water. Give your {} a 3 mins boil.".format(
                self.food_choice_list[self.decision]))
            print("Remove them after water and toss some teriyaki sause on top.")
            enter = input("Please press Enter to continue.")
            Engine.clear()
            print("Would you like to challenge yourself to cook something? Try Tofu or Sprouts!")
            self.choose(self.confirmation)
            if self.decision == 0:
                Veggie()
            else:
                pass

class Dessert(Food):
    """Subclass Dessert leads to instances for player to choose from."""

    def __init__(self):
        super().__init__()
        self.flavor_list = ["Chocolate Chips", "Blueberry"]
        self.dessert_type = ["Muffin", "Cupcake"]
        self.confirmation = ["Yes", "No"]
        self.choose_dessert()

    def choose_dessert(self):
        Engine.clear()
        print("Oops, you don't have any desserts at home right now. ")
        enter = input("Please press Enter to continue.")
        print("Would you like to try some easy baking? I have a few options for you.")

        self.choose(self.flavor_list)
        flavor_type_int = deepcopy(self.decision)

        self.choose(self.dessert_type)
        dessert_type_int = deepcopy(self.decision)
        dessert_recipe = Recipe()

        if flavor_type_int == 2:  # choice is pass
            pass
        elif flavor_type_int == 0 and dessert_type_int == 0:
            dessert_recipe.add_header("Chocolate Chips Muffin")
        elif flavor_type_int == 0 and dessert_type_int == 1:
            dessert_recipe.add_header("Chocolate Chips Cupcake")
        elif flavor_type_int == 1 and dessert_type_int == 0:
            dessert_recipe.add_header("Blueberry Muffin")
        elif flavor_type_int == 1 and dessert_type_int == 1:
            dessert_recipe.add_header("Blueberry Cupcake")

        if dessert_type_int == 0 or 1:
            dessert_recipe.add_ingredient(
                ["2.5 cup of all purpose flour", self.flavor_list[flavor_type_int], "2 tsp baking powder",
                 "170g sugar", "1/4 cup sour cream", "2 room temperature eggs",
                 "56g unstalted butter", "60mL Veggie oil", "240mL milk"])

            dessert_recipe.add_instruction(["Preheat to 400 degrees F.",
                                                 "Add the flour, baking powder and salt to a large bowl then whisk together and set aside.",
                                                 "Toss the {} in about a tablespoon of the dry mixture and set aside. ".format(
                                                     self.flavor_list[flavor_type_int]),
                                                 "In medium bowl, add melted butter, oil, milk, sugar,  eggs,  sour cream then whisk together until combined.",
                                                 "Pour the wet mixture into the dry then mix until almost combined. Add the {} and fold in.".format(
                                                     self.flavor_list[flavor_type_int]),
                                                 "Transfer batter to your prepared tin filling the wells to the top. Cover with the streusel topping.",
                                                 "Bake for about 20 minutes at 400F. Add a ramekin filled with water to keep the {} moist during the bake.".format(
                                                     self.dessert_type[dessert_type_int]),
                                                 "Let the {} cool in the tin for at least 10 minutes before removing.".format(
                                                     self.dessert_type[dessert_type_int])])

        enter = input(
            "There will be a final recipe generated for you in the end. Here is a sneak peak. Please press Enter to continue.")
        dessert_recipe.recipeOutput()
        Engine.recipe_of_selected_food["Dessert"] = dessert_recipe

class Drink(Food):
    def __init__(self):
        super().__init__()
        self.drink_choice_list = ["Merlot", "Chardonnay", "India Pale Ale", "Coke", "Sparking Water"]
        self.confirmation = ["Yes", "No"]
        self.choose_drink()

    def choose_drink(self):
        self.choose(self.drink_choice_list)
        Engine.clear()
        print("Great choice! This pairs greatly with your previous food choices!")

class Recipe:
    """A functional class that generates recipe for each food category. Rincluding header, ingredients, and
    instructions. Each food category is class instance, based on selection. This class helps pools all output together."""

    def __init__(self):
        self.header = ""
        self.ingredient = []
        self.instruction = []
        self.recipe = {}

    def add_header(self, header):
        self.header = header

    def add_ingredient(self, ingredient):
        self.ingredient += [ingredient]

    def add_instruction(self, instruction):
        self.instruction += [instruction]

    def recipeOutput(self):
        """A function allows to display the header, ingredient and instructions."""
        self.recipe['Header'] = self.header
        self.recipe['List of Ingredients'] = self.ingredient
        self.recipe['Instructions'] = self.instruction
        self.__str__()

    def __str__(self):
        print(self.recipe['Header'])
        print('List of Ingredients: ', end="\n")
        for i in range(len(self.recipe['List of Ingredients'])):
            for j in self.recipe['List of Ingredients'][i]:
                print("    - " + j, end="\n")
        print('Instructions: ', end="\n")
        for i in range(len(self.recipe['Instructions'])):
            for j in self.recipe['Instructions'][i]:
                print("    - " + j, end="\n")

    def __repr__(self):
        return self.__str__()

class Engine:
    """User interface that allows the player to drive the program."""
    """ construct a recipe dictionary to store all the selected food and their recipe. Available for view before and at the end."""
    recipe_of_selected_food = {}

    def __init__(self):
        self.action_list = ["Select food", "View selected food and recipe", "Finish", "Help"]
        self.food_category = ["Protein", "Veggie", "Dessert", "Drink", "Return to main menu"]
        self.start()  # Initialize the process of creating a recipe.
        self.decision = int()

    def clear():
        """ A function to clear the screen."""
        if name == 'nt':
            clear = system('cls')
        else:
            clear = system('clear')

    def input_choice(self, option_list):
        choices = []
        for i in range(0, len(option_list)):
            print("[{}] {}.".format((i + 1), option_list[i]))
            choices += [str(i + 1)]

        while True:
            choice = input("Please choose one of the followings.")
            if choice not in choices:
                print("You must choose a number corresponding to the choices given.")
                continue
            else:
                break

        self.decision = int(choice) - 1
        return self.decision

    def __repr__(self):
        """Print the recipe dictionary."""
        for key in Engine.recipe_of_selected_food.keys():
            Engine.recipe_of_selected_food[key].recipeOutput()
            print("\n")
        enter = input("Press 'Enter' to continue.")
        Engine.clear()

    def start(self):
        """The driving force of the game."""

        print(
            "It's meal time. I totally get you that figuring out what to eat is one of the hardest and most recurring questions to deal with EVERY SINGLE DAY. Let me help you!")
        enter = input("Please press Enter to continue.")
        Engine.clear()

        print(
            "Here is the main menu and you can return to this page if you would like to select food, need help, or receive your recipes.")
        enter = input("Please press Enter to continue.")
        Engine.clear()

        while True:
            print("Please choose one of the followings.")
            self.input_choice(self.action_list)
            if self.decision == 0:
                """ Navigate to food catagory, start to select food. """
                print("Fantastic, I found a few items in your kitchen, let's get started!")
                enter = input("Please press Enter to continue.")
                Engine.clear()

                while True:
                    self.input_choice(self.food_category)
                    if self.decision == 0:  # protein check
                        protein = Protein()
                        print("Let's move to the next item.")
                        enter = input("Please press Enter to continue.")
                        Engine.clear()
                    elif self.decision == 1:  # "Veggie" check
                        Veggie()
                        print("Let's move to the next item.")
                        enter = input("Please press Enter to continue.")
                        Engine.clear()
                    elif self.decision == 2:  # "Dessert"
                        Dessert()
                        print("Let's move to the next item.")
                        enter = input("Please press Enter to continue.")
                        Engine.clear()
                    elif self.decision == 3:  # "Drink"
                        Drink()
                        print("Let's move to the next item.")
                        enter = input("Please press Enter to continue.")
                        Engine.clear()
                    elif self.decision == 4:  # return to actions
                        print("What would you like to do next?")
                        enter = input("Please press Enter to continue.")
                        break

            elif self.decision == 1:
                """Display selected items and their recipes."""
                self.__repr__()


            elif self.decision == 2:   # Generate the final recipe and break out of the program.
                print("You just chose to exit the game.")
                enter = input("Please press Enter to continue.")
                print("Here is your recipe of all your selections. Enjoy your cooking jouney and meal!")
                self.__repr__()
                enter = input("Please press Enter to continue.")
                print("See you next time!")
                break

            elif self.decision == 3:
            # Generate a help menu when player needs help to play the game.
                print("Instructions:")
                print("-" * 100)
                print("You are the client this program will serve.")
                print("\nThe main menu has four options, Select food, View selected food and recipe, Finish, and Help.")
                print("\nSelect food - guide you to four food categories, Protein, Veggie, Dessert, and Drink.")
                print("\nView selected food and recipe - guide you to a list of food you already selected. ")
                print("\nFinish - allow you to exit the program. It will generate final recipes for all the food you have selected.")
                print("\nHelp - directs you to here, a detailed instructions for reference.")
                print("-" * 100)
                print("\nWithin each food category, take Protein as example:")
                print("\nAfter you select one of the protein, it prompts a question to ask for 'How well would you like your protein to be?'")
                print("\nBased on your preference, you could select one of the options. Then, it directs you to a proper next question. ")
                print("\nOnce you finished one food category, it directs you back to the the list of food categories for a next food item.")
                print("-" * 100)
                print("\nAfter selected all the food you like:")
                print("\nYou could go back to the main menu to view all your selection and their recipes, or Exit the program.")
                enter = input("Press 'Enter' to continue.")

Engine()

