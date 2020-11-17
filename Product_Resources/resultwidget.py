from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.menu import MDDropdownMenu

from kivy.properties import StringProperty


class ResultWidget(MDGridLayout):
    ingredient_name = StringProperty()
    unit = StringProperty()
    ingredient_value = StringProperty()

    def __init__(self, app, ingredient_name, ingredient, **kwargs):
        super(ResultWidget, self).__init__(**kwargs)
        # Creating instance of the menu widget
        menu_items = [{"icon": "flask", "text": f"{size}"} for size in list(ingredient.size.keys())]

        self.unit_menu = MDDropdownMenu(caller=self.ids.input_unit, selected_color=app.blue, items=menu_items,
                                        background_color=app.yellow, width_mult=3)
        self.unit_menu.bind(on_release=self.change_unit)

        # Setting the attributes
        self.app = app
        self.ingredient = ingredient
        self.ingredient_name = ingredient_name
        self.ingredient_type = type(ingredient)
        self.ingredient_value = str(round(ingredient.value, 2))
        self.unit = ingredient.unit

    def change_unit(self, menu_instance, selected_icon):
        """
        changes the unit of the ingredient
         :param menu_instance: the MDDropDownMenu widget
         :param selected_icon: the selected icon
        """

        # Changing the value of ingredient
        self.ingredient_value = str(round(self.ingredient.unit_convert(unit_to=selected_icon.text).value, 2))

        # Change unit to the selected item
        self.unit = selected_icon.text

        # Dismissing the menu
        menu_instance.dismiss()


class ResultWidgetProduct(MDGridLayout):
    ingredient_name = StringProperty()
    ingredient_value = StringProperty()

    def __init__(self, app, ingredient_name, ingredient, **kwargs):
        super(ResultWidgetProduct, self).__init__(**kwargs)

        # Setting the attributes
        self.app = app
        self.ingredient_name = ingredient_name
        self.ingredient_value = str(round(ingredient.value, 2))
