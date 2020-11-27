"""
The class managing the the product display
"""
from kivy.properties import StringProperty, DictProperty
from kivy.animation import Animation

from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.gridlayout import MDGridLayout


class ProductScreen(MDTabsBase, FloatLayout):
    title = StringProperty()
    base_ingredients = DictProperty()

    def __init__(self, title, base_ingredients, app, **kwargs):
        super(ProductScreen, self).__init__(**kwargs)
        self.title = title
        self.text = title
        self.base_ingredients = base_ingredients
        self.app = app

        # Creating an entering animation
        self.enter_anim = Animation(pos_hint={'right': 0.95}, duration=0.5, t='in_out_sine')

        # Creating an exiting animation
        self.exit_anim = Animation(pos_hint={'right': 0}, duration=0.5)

        # Looping through base_ingredients and displaying them on screen
        for ingredient in self.base_ingredients:
            # Creating a grid for the row
            ingRow = MDGridLayout(cols=2, rows=1)

            # Adding the label for the ingredient name
            label = MDLabel(text=ingredient, size_hint_y=None, font_style='Subtitle1')
            label.height = label.texture_size[1]

            ingRow.add_widget(label)

            # Adding the label the ingredients values
            label = MDLabel(text=str(self.base_ingredients[ingredient]),
                            size_hint_y=None, font_style='Subtitle1', halign='right')
            label.height = label.texture_size[1]
            label.width = label.texture_size[0]

            ingRow.add_widget(label)

            # Adding the row to the display
            self.ids['orgGrid'].add_widget(ingRow)

            # Adding seperator
            self.ids['orgGrid'].add_widget(
                MDSeparator(height='10dp', color=app.blue if app.theme_cls.theme_style == 'Light' else app.blue))

    def orgCard_in(self):
        """
        Animate the orgCard entering the screen
        :return:
        """
        # Getting the card
        orgCard = self.ids.orgCard

        # Animate the card in the screen
        self.enter_anim.start(orgCard)

    def orgCard_out(self):
        """
        Animate the orgCard exiting the screen
        :return:
        """
        # Getting the card
        orgCard = self.ids.orgCard

        # Animate the card out of the screen
        self.exit_anim.start(orgCard)

    def ingredient_collector_Screen(self, **kwargs):
        # Customizing the ICS
        self.app.root.ids.ICS.product_update(product=self.title, base_ingredients=self.base_ingredients, app=self.app)

        # Change Screen
        self.app.change_screen("ICS")

    def product_collector_Screen(self, **kwargs):
        # Customizing the PCS
        self.app.root.ids.PCS.product_update(product=self.title, base_ingredients=self.base_ingredients, app=self.app)

        # Change Screen
        self.app.change_screen("PCS")
