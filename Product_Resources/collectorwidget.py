"""
Contains the necessary widgets  collecting user input and converting it to the right type
"""

from kivy.properties import StringProperty, NumericProperty

from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.menu import MDDropdownMenu


class IngredientCollectorWidget(MDGridLayout):
    product = StringProperty()
    value = NumericProperty()
    unit = StringProperty()

    def __init__(self, app, ingredients_object, ingredient_name='', **kwargs):
        super(IngredientCollectorWidget, self).__init__(**kwargs)

        # Creating instance of the menu widget
        menu_items = [{"icon": "flask", "text": f"{size}"} for size in list(ingredients_object.size.keys())]

        self.unit_menu = MDDropdownMenu(caller=self.ids.input_unit, selected_color=app.blue, items=menu_items,
                                        background_color=app.yellow,  width_mult=3)
        self.unit_menu.bind(on_release=self.set_unit)

        self.product = ingredient_name
        self.ingredient_type = ingredients_object

        # User selected values
        self.value = int()
        self.unit = list(ingredients_object.size.keys())[0]

    def set_unit(self, menu_instance, selected_icon):
        """
         :param menu_instance: the MDDropDownMenu widget
         :param selected_icon: the selected icon
         :: This function will change the unit attribute to the selected size
         """

        # Change unit to the selected item
        self.unit = selected_icon.text

        # Dismissing the menu
        menu_instance.dismiss()

    def is_valid(self):
        """
        This method will test if the values that the users inputted are valid
        :return: true if valid and false if not valid
        """

        # Assigning the text value from TextField widget
        self.value = self.ids.input_value.text if self.ids.input_value.text else 0
        # Testing if input is positive value
        if 0 < self.value < 9999:
            return True
        else:
            return False

    def input_error(self, error):
        """
        Changes the textfield to error mode
        :error:: determines whether the error will be inflicted
        :return: 1 if failed 0
        """
        try:
            # Setting the textfield to error true
            self.ids.input_value.error = True if error else False

            # Focusing on the input
            self.ids.input_value.focus = True
            return 1

        except:
            return 0

    def convert_to_type(self):
        """

        :return: An instance of the ingredient_type
        """
        return self.ingredient_type(self.value, self.unit)


class ProductCollectorWidget(MDGridLayout):
    product = StringProperty()
    value = NumericProperty()
    unit = StringProperty()

    def __init__(self, app, ingredients_object, ingredient_name='', **kwargs):
        super(ProductCollectorWidget, self).__init__(**kwargs)
        self.product = ingredient_name
        self.ingredient_type = ingredients_object

        # User selected values
        self.value = int()
        self.unit = ingredient_name[0].upper()

    def is_valid(self):
        """
        This method will test if the values that the users inputted are valid
        :return: true if valid and false if not valid
        """

        # Assigning the text value from TextField widget
        self.value = self.ids.input_value.text if self.ids.input_value.text else 0
        # Testing if input is positive value
        if 0 < self.value < 9999:
            return True
        else:
            return False

    def input_error(self, error):
        """
        Changes the textfield to error mode
        :error:: determines whether the error will be inflicted
        :return: 1 if failed 0
        """
        try:
            # Setting the textfield to error true
            self.ids.input_value.error = True if error else False

            # Focusing on the input
            self.ids.input_value.focus = True
            return 1

        except:
            return 0

    def convert_to_type(self):
        """

        :return: An instance of the ingredient_type
        """
        return self.ingredient_type(self.value, self.unit)
