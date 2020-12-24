from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDSeparator

from kivy.properties import DictProperty, ObjectProperty

from .resultwidget import ResultWidget, ResultWidgetProduct
from CALCULATORS.Ingredients import Ingredients


class ResultsPage(MDScreen):
    product = 'title'  # StringProperty()
    app = ObjectProperty()
    ingredients = DictProperty()
    ingDisplay = ObjectProperty()

    def product_update(self, app, product, ingredients):
        """
        this method updates the screen to display proper values
        :param product: The name of the product
        :param ingredients: the  ingredients of the product
        :param app: the app object
        """
        # Setting class attributes
        self.product = product
        self.ingredients = ingredients
        self.app = app

        # Updating the toolbar title
        app.root.ids.RP_toolbar.title = product

        # accessing the card for displaying ingredients
        self.ingDisplay: MDBoxLayout = app.root.ids.RP_ingDisplay

        # Removing and widget initialized in the ingDisplay
        self.ingDisplay.clear_widgets()

        # looping through base_ingredients and adding the IngredientCollectorWidget
        for ingredient in self.ingredients:

            if type(self.ingredients[ingredient]) == Ingredients:
                self.ingDisplay.add_widget(ResultWidgetProduct(app=self.app, ingredient_name=ingredient,
                                                               ingredient=self.ingredients[ingredient]))

            else:
                # Testing if result is valid
                result = ResultWidget(app=self.app, ingredient_name=ingredient, ingredient=self.ingredients[ingredient])

                if result.is_valid():
                    self.ingDisplay.add_widget(result)
                    continue
                else:
                    result.dialog.open()
                    return False

        else:
            return True
