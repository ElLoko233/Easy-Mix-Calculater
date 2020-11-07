"""
The class managing the the product display
"""
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu

from kivy.properties import StringProperty, DictProperty, NumericProperty, ObjectProperty


class ProductScreen(MDTabsBase, FloatLayout):
    title = StringProperty()
    base_ingredients = DictProperty()

    def __init__(self, title, base_ingredients, app, **kwargs):
        super(ProductScreen, self).__init__(**kwargs)
        self.title = title
        self.text = title
        self.base_ingredients = base_ingredients
        self.app = app

        # Looping through base_ingredients and displaying them on screen
        for ingredient in self.base_ingredients:
            # Adding the label for the ingredient name
            label = MDLabel(text=ingredient, size_hint_y=None, font_style='Subtitle1')
            label.height = label.texture_size[1]

            self.ids['orgGrid'].add_widget(label)

            # Adding the label the ingredients values
            label = MDLabel(text=str(self.base_ingredients[ingredient]),
                            size_hint_y=None, font_style='Subtitle1', halign='right')
            label.height = label.texture_size[1]
            label.width = label.texture_size[0]

            self.ids['orgGrid'].add_widget(label)

    def ingredient_collector_Screen(self, **kwargs):
        # Customizing the ICS
        self.app.root.ids.ICS.product_update(product=self.title, base_ingredients=self.base_ingredients, app=self.app)

        # Change Screen
        self.app.change_screen("ICS")

    def product_collector_Screen(self, **kwargs):
        pass


class IngredientCollectorWidget(MDBoxLayout):
    product = StringProperty()
    value = NumericProperty()
    unit = StringProperty()

    def __init__(self, app, ingredients_object, ingredient_name='', **kwargs):
        super(IngredientCollectorWidget, self).__init__(**kwargs)

        self.product = ingredient_name
        self.ingredient_type = ingredients_object

        # units of the ingredient
        self.menu_items = list(ingredients_object.size.keys())

        # Creating MDMenu instance
        self.unit_menu = MDDropdownMenu(caller=self.ids['input_unit'], width_mult=3, background_color=app.yellow)

        # User selected values
        self.value = int() # Text Input text
        self.unit = self.menu_items[0]

