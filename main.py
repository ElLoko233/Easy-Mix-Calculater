from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.behaviors import MagicBehavior
from kivymd.uix.label import MDLabel

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
        self.yellow = [255 / 255, 237 / 255, 47 / 255, 1]
        self.blue = [23 / 255, 70 / 255, 162 / 255, 1]
        self.red = [234 / 255, 18 / 255, 17 / 255, 1]
        # Screen size
        self.screen_size = Window.size

        # The instance of the previous tab
        self.previous_tab = ''

        # creating the previous screen attribute
        self.previous_screen = ''

    def on_start(self):

        # Wobbling the splash screen text
        self.root.ids.title.wobble()

        # Populating the MDTabs
        for ingredient in Base_Ingredients:
            # Creating a tab containing the appropriate info
            product = ProductScreen(title=ingredient, base_ingredients=Base_Ingredients[ingredient], app=self)
            self.root.ids.tabs.add_widget(product)

        else:
            # Setting tool bar size
            self.root.ids.home_toolbar.ids.label_title.font_size = '25sp'

            # Removing splash screen
            Clock.schedule_once(lambda x: self.change_screen('HomePage', direction='left'), 3)



            return True

    def current_tab(self, tab, tabbase, tablabel, tab_name):

        # Play exit animation of previous tab
        try:
            self.previous_tab.orgCard_out()
            self.previous_tab = tabbase
        except AttributeError:
            self.previous_tab = tabbase

        # Play entering animation of next tab
        tabbase.orgCard_in()

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.accent_palette = "Blue"

        # Loading saved style
        try:
            with open('settings.jk', 'r') as file:
                self.theme_cls.theme_style = file.read()

        except FileNotFoundError:
            pass

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

    def save_settings(self):
        # Saving value of the app style
        with open('settings.jk', 'w') as file:
            file.write(self.theme_cls.theme_style)

    def change_style(self, instance):
        # Changing the style
        self.theme_cls.theme_style = 'Light' if self.theme_cls.theme_style == 'Dark' else 'Dark'

        # Saving the setting
        self.save_settings()

        # Changing icon
        instance.icon = 'flashlight-off' if self.theme_cls.theme_style == 'Dark' else 'flashlight'

        # Fixing the toolbar color
        self.root.ids.home_toolbar.specific_text_color = self.blue


class CustomLabel(MagicBehavior, MDLabel):
    pass


if __name__ == '__main__':
    EasyMixCalculatorApp().run()
