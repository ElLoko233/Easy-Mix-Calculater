"""
The class managing the the product display
"""
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

from kivy.properties import StringProperty, DictProperty


class ProductScreen(MDTabsBase, FloatLayout):
    title = StringProperty()
    base_ingredients = DictProperty()

    def __init__(self, title, base_ingredients, **kwargs):
        super(ProductScreen, self).__init__(**kwargs)
        self.title = title
        self.text = title
        self.base_ingredients = base_ingredients

    def DisplayOrg(self):
        """
        Handles displaying the base ingredients to the screen
        """
        # Looping through the values
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

    def ingredient_collector_Screen(self, srn_mgr, **kwargs):
        print(srn_mgr.ids)

    def product_collector_Screen(self, srn_mgr, **kwargs):
        print(srn_mgr.ids)


class IngredientCollectorScreen(Screen):
    pass


class ProductCollectorScreen(Screen):
    pass