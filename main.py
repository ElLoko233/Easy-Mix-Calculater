from kivy.core.window import Window
from kivy.lang.builder import Builder

from kivymd.app import MDApp

from Product_Resources.product_base_ingredients import Base_Ingredients
from Product_Resources.productscreener import ProductScreen
from Product_Resources.collectorscreener import IngredientCollectorScreen, ProductCollectorScreen
from Product_Resources.collectorwidget import IngredientCollectorWidget, ProductCollectorWidget
from Product_Resources.resultsscreener import ResultsPage
from Product_Resources.resultwidget import ResultWidget, ResultWidgetProduct
from appdetails.app_details import HelpPage, AboutUsPage

Window.size = [300, 520]


class EasyMixCalculatorApp(MDApp):

    def __init__(self, **kwargs):
        super(EasyMixCalculatorApp, self).__init__(**kwargs)
        self.grey = [226 / 255, 226 / 255, 226 / 255, 1]
        self.yellow = [255 / 255, 218 / 255, 6 / 255, 1]
        self.blue = [0 / 255, 35 / 255, 234 / 255, 1]
        self.red = [226 / 255, 19 / 255, 19 / 255, 1]

        # creating the previous screen attribute
        self.previous_screen = ''

    def on_start(self):
        # Changing to results page
        # self.root.current = 'RP'

        # Populating the MDTabs
        for ingredient in Base_Ingredients:
            # Creating a tab containing the appropriate info
            product = ProductScreen(title=ingredient, base_ingredients=Base_Ingredients[ingredient], app=self)
            self.root.ids.tabs.add_widget(product)

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.accent_palette = "Blue"

        # self.theme_cls.theme_style = 'Dark'

        return Builder.load_file('EasyMix.kv')

    def change_screen(self, page, direction='left'):
        # This function controls the changing of screens and the direction they change to
        """
        :param page: name of the screen to change to
        :param direction: the direction in which the screen will change in
        :return: nothing
        """
        # Setting up the previous screen attribute
        self.previous_screen = self.root.current

        # Changing the Screen
        self.root.transition.direction = direction
        self.root.current = page


if __name__ == '__main__':
    EasyMixCalculatorApp().run()
