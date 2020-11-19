"""
Contains the screens that manages the collecting of user input and running
them through the necessary verifications and calculation
"""
from kivy.properties import StringProperty, DictProperty

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from .collectorwidget import IngredientCollectorWidget, ProductCollectorWidget
from CALCULATORS.Ingrediant_calculator import calculate_ingredients, calculate_product
from CALCULATORS.Ingredients import Ingredients


class IngredientCollectorScreen(MDScreen):
    product = StringProperty()
    base_ingredients = DictProperty()

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
        for ingredient_name in list(base_ingredients.keys()):
            # Excluding the product
            if type(self.base_ingredients[ingredient_name]) == Ingredients:
                continue

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

            # Opening the the results
            self.open_results(results)

    def open_results(self, ingredients):
        """
        method will open the result page and load the proper info
        :param ingredients: the calculated ingredients dictionary
        :return:
        """

        # Calling the product update method of the ResultsPage
        if self.app.root.ids.RP.product_update(app=self.app, product=self.product, ingredients=ingredients):

            # Change screen
            self.app.change_screen('RP')

        else:
            pass


class ProductCollectorScreen(MDScreen):
    product = StringProperty()
    base_ingredients = DictProperty()

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

        self.ingDisplay.add_widget(ProductCollectorWidget(app=app, ingredient_name=product,
                                                          ingredients_object=type(
                                                              base_ingredients[product])))

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

            # Conducting calculation to get the results for provided ingredients
            results = calculate_ingredients(org_ingredients=self.base_ingredients,
                                            new_product=userIngredients[self.product].value)

            # Converting egg value to base unit
            results['Egg'] = results['Egg'].unit_convert(unit_to=self.base_ingredients['Egg'].unit)

            # Opening the the results
            self.open_results(results)

    def open_results(self, ingredients):
        """
        method will open the result page and load the proper info
        :param ingredients: the calculated ingredients dictionary
        :return:
        """

        # Calling the product update method of the ResultsPage
        if self.app.root.ids.RP.product_update(app=self.app, product=self.product, ingredients=ingredients):

            # Change screen
            self.app.change_screen('RP')

        else:
            pass
