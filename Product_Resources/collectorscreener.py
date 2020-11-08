"""
Contains the screens that manages the collecting of user input and running
them through the necessary verifications and calculation
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from .collectorwidget import IngredientCollectorWidget, ProductCollectorWidget
from CALCULATORS.Ingrediant_calculator import calculate_ingredients, calculate_product


class IngredientCollectorScreen(MDScreen):
    product = ''
    base_ingredients = {}

    def product_update(self, app, product='', base_ingredients={}):
        """
        This function will update the screen and add certain widgets to the screen
        :param product: The name of the product
        :param base_ingredients: the base ingredients of the product
        :param app: the app object
        :return: 1
        """
        # Creating an app attribute
        self.app = app

        # Updating the class attribute
        self.base_ingredients = base_ingredients
        self.product = product

        # Updating the toolbar title
        app.root.ids.ICS_toolbar.title = product

        # accessing the card for collecting ingredients
        self.ingDisplay: MDBoxLayout = app.root.ids.ICS_ingDisplay

        # Removing and widget initialized in the ingDisplay
        self.ingDisplay.clear_widgets()

        # looping through base_ingredients and adding the IngredientCollectorWidget
        for ingredient_name in list(base_ingredients.keys())[1:]:
            self.ingDisplay.add_widget(IngredientCollectorWidget(app=app, ingredient_name=ingredient_name,
                                                                 ingredients_object=type(
                                                                     base_ingredients[ingredient_name])))

    def collect_user_input(self):
        """
        this function will collect the users input and load them into a dictionary
        :return: 1 if success
        """
        # Dictionary of the user inputted values
        userIngredients = {}

        # Looping through the user input
        for userInput in self.ingDisplay.children:
            # Testing if the user input is valid
            if userInput.is_valid():
                # deactivating the error mode
                userInput.input_error(error=0)

                # Appending the users input into dictionary
                userIngredients[userInput.product] = userInput.convert_to_type()

            else:
                # Clearing the dictionary
                userIngredients.clear()

                # Running the error method
                userInput.input_error(error=1)
                break
        else:
            # Converting egg value to grams from base_ingredients
            self.base_ingredients['Egg'] = self.base_ingredients['Egg'].unit_convert(unit_to='g')

            # Flipping order of dictionary
            values = list(userIngredients.keys())
            values.reverse()

            userIngredients = {item: userIngredients[item] for item in values}

            # Conducting calculation to get the results for provided ingredients
            results = calculate_product(org_ingredient=self.base_ingredients, new_ingredient=userIngredients)


class ProductCollectorScreen(MDScreen):
    product = ''
    base_ingredients = {}

    def product_update(self, app, product='', base_ingredients={}):
        """
        This function will update the screen and add certain widgets to the screen
        :param product: The name of the product
        :param base_ingredients: the base ingredients of the product
        :param app: the app object
        :return: 1
        """
        # Creating an app attribute
        self.app = app

        # Updating the class attribute
        self.base_ingredients = base_ingredients
        self.product = product

        # Updating the toolbar title
        app.root.ids.PCS_toolbar.title = product

        # accessing the card for collecting ingredients
        self.ingDisplay: MDBoxLayout = app.root.ids.PCS_ingDisplay

        # Removing and widget initialized in the ingDisplay
        self.ingDisplay.clear_widgets()

        # accessing product from base_ingredients and adding the IngredientCollectorWidget
        ingredient_name = list(base_ingredients.keys())[0]

        self.ingDisplay.add_widget(ProductCollectorWidget(app=app, ingredient_name=ingredient_name,
                                                          ingredients_object=type(
                                                              base_ingredients[ingredient_name])))

    def collect_user_input(self):
        """
        this function will collect the users input and load them into a dictionary
        :return: 1 if success
        """
        # Dictionary of the user inputted values
        userIngredients = {}

        # Looping through the user input
        for userInput in self.ingDisplay.children:
            # Testing if the user input is valid
            if userInput.is_valid():
                # deactivating the error mode
                userInput.input_error(error=0)

                # Appending the users input into dictionary
                userIngredients[userInput.product] = userInput.convert_to_type()

            else:
                # Clearing the dictionary
                userIngredients.clear()

                # Running the error method
                userInput.input_error(error=1)
                break
        else:
            # Ensuring the product is not invalid
            userIngredients['Product'].value = userIngredients['Product'].value if userIngredients['Product'].value > 0 else self.base_ingredients['Product'].value

            # Conducting calculation to get the results for provided ingredients
            results = calculate_ingredients(org_ingredients=self.base_ingredients,
                                         new_product=userIngredients['Product'].value)

