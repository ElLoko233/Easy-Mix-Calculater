import pyperclip as clipboard
import re

from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, DictProperty, NumericProperty
from kivy.uix.scrollview import ScrollView

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.menu import MDDropdownMenu

# Loading base ingredients
from Product_Resources.product_base_ingredients import Base_Ingredients

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

        return Builder.load_string(kv)

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

class AboutUsPage(ScrollView):
    # EasyMixCalculator MDCard info
    EM_text = [
        "EasyMixCalculator helps bakers calculate the right amount of ingredients to make large amounts of products.",
        "It also helps customers to calculate the right amounts of ingredients they can use if they don't have the exact amounts of ingredients to make a product."]

    # SnowFlake MDCard info
    SnowFlake = {'Telephone': '[ref=CopyPaste]0115 654 300[/ref]',
                 'Address': 'Building 5\nMaxwell Office Park\nMagwa Crescent West\nWaterfall City\n2090',
                 'Customer Care': '[ref=CopyPaste]0860 122 300[/ref]',
                 'Website': '[ref=WebSite]www.snowflake.co.za[/ref]',

                 'SocialMedia': {'facebook': '[ref=Facebook]snowflakesouthafrica[/ref]',
                                 'instagram': '[ref=Instagram]snowflake_sa[/ref]',
                                 'youtube': '[ref=YouTube]Snowflake Life[/ref]'}}
    # Developer info
    App_Dev = {'profile': "Lelethu Futshane",
               'gmail': "[ref=CopyPaste]ellokoprograma@gmail.com[/ref]",
               'github': "[ref=GitHub]ElLoko233[/ref]"}

    def __init__(self, **kwargs):
        super(AboutUsPage, self).__init__(**kwargs)
        # Dictionary of the linked to the corresponding functions
        self.ref_pattern = {'(\[ref=WebSite\])(?P<WebSite>.*)(\[/ref\])': self.open_site,
                            '(\[ref=CopyPaste\])(?P<Copy>.*)(\[/ref\])': self.copyPaste,
                            '(\[ref=Facebook\])(?P<Facebook>.*)(\[/ref\])': self.open_facebook,
                            '(\[ref=Instagram\])(?P<Instagram>.*)(\[/ref\])': self.open_instagram,
                            '(\[ref=YouTube\])(?P<YouTube>.*)(\[/ref\])': self.open_youtube,
                            '(\[ref=GitHub\])(?P<GitHub>.*)(\[/ref\])': self.open_git}

    # Handles ref attribute from labels
    def RefHandler(self, instance: MDLabel, *args, **kwargs):

        for pattern in self.ref_pattern:
            # locating the ref tagged labels
            match = re.match(pattern, instance.text)

            # Assigning match to their respective function
            if match:
                match = match.groupdict()
                for key in match:
                    self.ref_pattern[pattern](match[key])

    # Handles open site links
    def open_site(self, url):
        # Save link to clipboard
        clipboard.copy(f'https://{url}')
        # Display toast on screen, inform url is saved to clipboard
        toast("url saved in clipboard")

    def copyPaste(self, text):
        # Save link to clipboard
        clipboard.copy(text)
        # Display toast on screen, inform url is saved to clipboard
        toast("saved in clipboard")

    def open_facebook(self, page):
        # Save link to clipboard
        clipboard.copy(f'https://www.facebook.com/{page}/')
        # Display toast on screen, inform url is saved to clipboard
        toast("url saved in clipboard")

    def open_git(self, page):
        # Save link to clipboard
        clipboard.copy(f'https://github.com/{page}')
        # Display toast on screen, inform url is saved to clipboard
        toast("url saved in clipboard")

    def open_instagram(self, page):
        # Save link to clipboard
        clipboard.copy(f'https://www.instagram.com/{page}/')
        # Display toast on screen, inform url is saved to clipboard
        toast("url saved in clipboard")

    def open_youtube(self, page):
        # Save link to clipboard
        clipboard.copy(f'https://www.youtube.com/c/{page}/featured')
        # Display toast on screen, inform url is saved to clipboard
        toast("url saved in clipboard")

class HelpPage(ScrollView):
    pass

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
        for ingredient_name in list(base_ingredients.keys())[:-1]:

            self.ingDisplay.add_widget(IngredientCollectorWidget( app=app, ingredient_name=ingredient_name,
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
            # Appending the product to dictionary
            userIngredients[list(self.base_ingredients.keys())[-1]] = self.base_ingredients.get(list(self.base_ingredients.keys())[-1])

            print( userIngredients)

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
        ingredient_name = list(base_ingredients.keys())[-1]

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
            # Appending the ingredients to dictionary
            for ingName in list(self.base_ingredients)[:-1]:
                userIngredients[ingName] = self.base_ingredients[ingName]
            else:

                return userIngredients

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
        # Customizing the PCS
        self.app.root.ids.PCS.product_update(product=self.title, base_ingredients=self.base_ingredients, app=self.app)

        # Change Screen
        self.app.change_screen("PCS")

class IngredientCollectorWidget(MDGridLayout):
    product = StringProperty()
    value = NumericProperty()
    unit = StringProperty()

    def __init__(self, app, ingredients_object, ingredient_name='', **kwargs):
        super(IngredientCollectorWidget, self).__init__(**kwargs)

        # Creating menu items
        self.menu_items = [{"flask": size} for size in list(ingredients_object.size.keys())]

        # Creating MDMenu instance
        self.unit_menu = MDDropdownMenu(selected_color=app.blue, caller=self.ids.input_unit, width_mult=3,
                                        background_color=app.yellow, items=self.menu_items, radius=0.5)

        # Binging the menu to the set_unit function
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
        if 0 <= self.value < 9999:
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
        if 0 <= self.value < 9999:
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


kv = """

ScreenManager:
    name: srn_mgr
    id: srn_mgr

    MDScreen:
        name: "HomePage"

        BoxLayout:
            orientation: 'vertical'

            MDToolbar:
                title: "EM Calculator"
                right_action_items: [["help-circle-outline", lambda x: app.change_screen('HelpPage')], ["comment-question", lambda x: app.change_screen( "AboutPage")]]
                specific_text_color: app.blue
                elevation: 10

            MDTabs:
                id: tabs
                text_color_normal: app.blue
                text_color_active: app.red
                color_indicator: app.blue
                tab_bar_height: '30dp'
                tab_indicator_anim: True


    IngredientCollectorScreen:
        name: 'ICS'
        id: ICS

        BoxLayout:
            orientation: 'vertical'

            MDToolbar:
                title: ICS.product
                left_action_items: [["home", lambda x: app.change_screen( 'HomePage', 'right')]]
                right_action_items: [["help-circle-outline", lambda x: app.change_screen('HelpPage')]]
                specific_text_color: app.blue
                elevation: 2
                id: ICS_toolbar

            ScrollView:
                do_scroll_x: False
                do_scroll_y: True

                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_height: True
                    padding: ['10dp', '25dp']
                    spacing: '25dp'

                    MDBoxLayout:
                        id: ICS_ingDisplay
                        orientation: 'vertical'
                        adaptive_height: True
                        spacing: '15dp'
                        padding: '10dp'
                        pos_hint: {'center_y': 0.5, 'center_x': 0.5}

                    AnchorLayout:
                        anchor_x: 'center'

                        MDRaisedButton:
                            elevation: '5dp'
                            markup: True
                            text: '[b][size=18]calculate[/size][/b]'
                            md_bg_color: app.blue
                            text_color: app.theme_cls.primary_color
                            on_release: ICS.collect_user_input()

    ProductCollectorScreen:
        name: 'PCS'
        id: PCS

        BoxLayout:
            orientation: 'vertical'

            MDToolbar:
                title: ICS.product
                left_action_items: [["home", lambda x: app.change_screen( 'HomePage', 'right')]]
                right_action_items: [["help-circle-outline", lambda x: app.change_screen('HelpPage')]]
                specific_text_color: app.blue
                elevation: 2
                id: PCS_toolbar

            ScrollView:
                do_scroll_x: False
                do_scroll_y: True

                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_height: True
                    padding: ['10dp', '25dp']
                    spacing: '25dp'

                    MDBoxLayout:
                        id: PCS_ingDisplay
                        orientation: 'vertical'
                        adaptive_height: True
                        spacing: '15dp'
                        padding: '10dp'
                        pos_hint: {'center_y': 0.5, 'center_x': 0.5}

                    AnchorLayout:
                        anchor_x: 'center'

                        MDRaisedButton:
                            elevation: '5dp'
                            markup: True
                            text: '[b][size=18]calculate[/size][/b]'
                            md_bg_color: app.blue
                            text_color: app.theme_cls.primary_color
                            on_release: PCS.collect_user_input()
    MDScreen:
        name: 'HelpPage'

        BoxLayout:
            orientation: 'vertical'

            MDToolbar:
                title: "Help"
                left_action_items: [["arrow-bottom-left", lambda x: app.change_screen( app.previous_screen, 'right')]]
                specific_text_color: app.blue
                elevation: 10

            HelpPage:
                do_scroll_x: False
                do_scroll_y: True
                id: HelpPage

                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_height: True
                    padding: '20dp'
                    spacing: '20dp'

                    MDCard:
                        orientation: "vertical"
                        size_hint: [0.9, None]
                        height: self.minimum_height
                        pos_hint: {"center_x": .5, "center_y": .5}
                        padding: "5dp"
                        elevation: '0.5dp'

                        MDBoxLayout:
                            id: image_box
                            adaptive_height: True

                            Image:
                                source: './folder.png'
                                size_hint: .3, None
                                height: image_box.height

                        MDBoxLayout:
                            id: text_box
                            orientation: 'vertical'
                            adaptive_height: True
                            spacing: '2dp'

                            MDLabel:
                                font_style: 'H5'
                                text: 'Title'
                                theme_text_color: "Secondary"
                                size_hint_y: None
                                height: self.texture_size[1]

                            MDSeparator:
                                height: "2dp"
                                color: app.blue

                            MDLabel:
                                text: 'Text'
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"

                    MDCard:
                        orientation: "vertical"
                        size_hint: [0.9, None]
                        height: self.minimum_height
                        pos_hint: {"center_x": .5, "center_y": .5}
                        padding: "5dp"
                        elevation: '0.5dp'

                        MDBoxLayout:
                            id: image_box
                            adaptive_height: True

                            Image:
                                source: './folder.png'
                                size_hint: .3, None
                                height: image_box.height

                        MDBoxLayout:
                            id: text_box
                            orientation: 'vertical'
                            adaptive_height: True
                            spacing: '2dp'

                            MDLabel:
                                font_style: 'H5'
                                text: 'Title'
                                theme_text_color: "Secondary"
                                size_hint_y: None
                                height: self.texture_size[1]

                            MDSeparator:
                                height: "2dp"
                                color: app.blue

                            MDLabel:
                                text: 'Text'
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"

                    MDCard:
                        orientation: "vertical"
                        size_hint: [0.9, None]
                        height: self.minimum_height
                        pos_hint: {"center_x": .5, "center_y": .5}
                        padding: "5dp"
                        elevation: '0.5dp'

                        MDBoxLayout:
                            id: image_box
                            adaptive_height: True

                            Image:
                                source: ''
                                size_hint: .3, None
                                height: image_box.height

                        MDBoxLayout:
                            id: text_box
                            orientation: 'vertical'
                            adaptive_height: True
                            spacing: '2dp'

                            MDLabel:
                                font_style: 'H5'
                                text: 'Title'
                                theme_text_color: "Secondary"
                                size_hint_y: None
                                height: self.texture_size[1]

                            MDSeparator:
                                height: "2dp"
                                color: app.blue

                            MDLabel:
                                text: 'Text'
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"





    MDScreen:
        name: 'AboutPage'

        BoxLayout:
            orientation: 'vertical'

            MDToolbar:
                title: "About Us"
                left_action_items: [["arrow-bottom-left", lambda x: app.change_screen( app.previous_screen, 'right')]]
                specific_text_color: app.blue
                elevation: 10

            AboutUsPage:
                do_scroll_x: False
                do_scroll_y: True
                id: AboutUsPage

                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_height: True
                    padding: '20dp'
                    spacing: '20dp'

                    MDCard:
                        orientation: "vertical"
                        size_hint: [0.9, None]
                        height: self.minimum_height
                        pos_hint: {"center_x": .5, "center_y": .5}
                        padding: "8dp"
                        spacing: '10dp'
                        elevation: '0.5dp'


                        MDLabel:
                            font_style: 'H5'
                            text: 'EM Calculator'
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]

                        MDSeparator:
                            height: "2dp"
                            color: app.blue

                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True

                            MDLabel:
                                text: 'Version'
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                text: '0.0.1'
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"

                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True

                            MDLabel:
                                text: AboutUsPage.EM_text[0]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"

                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True

                            MDLabel:
                                text: AboutUsPage.EM_text[1]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"



                    MDCard:
                        orientation: "vertical"
                        size_hint: [0.9, None]
                        height: self.minimum_height
                        pos_hint: {"center_x": .5, "center_y": .5}
                        padding: "8dp"
                        spacing: '10dp'
                        elevation: '0.5dp'


                        MDLabel:
                            font_style: 'H5'
                            text: 'SnowFlake'
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]

                        MDSeparator:
                            height: "2dp"
                            color: app.blue

                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True

                            MDLabel:
                                text: "Telephone"
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.SnowFlake["Telephone"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"
                                on_ref_press: AboutUsPage.RefHandler(self)

                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True

                            MDLabel:
                                text: "Address"
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.SnowFlake["Address"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"

                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True

                            MDLabel:
                                text: "Website"
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.SnowFlake["Website"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"
                                on_ref_press: AboutUsPage.RefHandler(self)

                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True

                            MDLabel:
                                text: "Customer Care"
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.SnowFlake["Customer Care"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"
                                on_ref_press: AboutUsPage.RefHandler(self)

                        MDGridLayout:
                            orientation: 'vertical'
                            cols: 2
                            rows: 1
                            spacing: '10dp'
                            adaptive_height: True

                            MDIcon:
                                icon: "facebook"
                                size_hint: [None, None]
                                width: self.texture_size[0]
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.SnowFlake["SocialMedia"]["facebook"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"
                                on_ref_press: AboutUsPage.RefHandler(self)

                        MDGridLayout:
                            orientation: 'vertical'
                            cols: 2
                            rows: 1
                            spacing: '10dp'
                            adaptive_height: True

                            MDIcon:
                                icon: "youtube"
                                size_hint: [None, None]
                                width: self.texture_size[0]
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.SnowFlake["SocialMedia"]["youtube"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"
                                on_ref_press: AboutUsPage.RefHandler(self)

                        MDGridLayout:
                            orientation: 'vertical'
                            cols: 2
                            rows: 1
                            spacing: '10dp'
                            adaptive_height: True

                            MDIcon:
                                icon: "instagram"
                                size_hint: [None, None]
                                width: self.texture_size[0]
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.SnowFlake["SocialMedia"]["instagram"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"
                                on_ref_press: AboutUsPage.RefHandler(self)

                    MDCard:
                        orientation: "vertical"
                        size_hint: [0.9, None]
                        height: self.minimum_height
                        pos_hint: {"center_x": .5, "center_y": .5}
                        padding: "8dp"
                        spacing: '10dp'
                        elevation: '0.5dp'

                        MDLabel:
                            font_style: 'H5'
                            text: 'App Developer'
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]

                        MDSeparator:
                            height: "2dp"
                            color: app.blue

                        MDGridLayout:
                            orientation: 'vertical'
                            cols: 2
                            rows: 1
                            spacing: '10dp'
                            adaptive_height: True

                            MDIcon:
                                icon: "account"
                                size_hint: [None, None]
                                width: self.texture_size[0]
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.App_Dev["profile"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"

                        MDGridLayout:
                            orientation: 'vertical'
                            cols: 2
                            rows: 1
                            spacing: '10dp'
                            adaptive_height: True

                            MDIcon:
                                icon: "gmail"
                                size_hint: [None, None]
                                width: self.texture_size[0]
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.App_Dev["gmail"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"
                                on_ref_press: AboutUsPage.RefHandler(self)

                        MDGridLayout:
                            orientation: 'vertical'
                            cols: 2
                            rows: 1
                            spacing: '10dp'
                            adaptive_height: True

                            MDIcon:
                                icon: "github"
                                size_hint: [None, None]
                                width: self.texture_size[0]
                                height: self.texture_size[1]
                                theme_text_color: "Hint"
                            MDLabel:
                                markup: True
                                text: AboutUsPage.App_Dev["github"]
                                font_style: 'Body1'
                                size_hint_y: None
                                height: self.texture_size[1]
                                theme_text_color: "Primary"
                                on_ref_press: AboutUsPage.RefHandler(self)
<ProductCollectorWidget>:
    id: product_input_widget
    adaptive_height: True
    row_default_height: '50dp'
    cols_minimum: {0:10}
    cols: 2

    MDBoxLayout:
        size_hint_x: 0.15

        MDLabel:
            id: label_text
            text: root.product
            halign: 'left'
            valign: 'bottom'

    BoxLayout:
        size_hint_x: 0.4

        MDTextField:
            id: input_value
            on_text_validate: (lambda : root.input_error(0) if root.is_valid() else root.input_error(1))()
            input_filter: 'int'
            hint_text: 'Input ingredients'
            helper_text_mode: 'on_error'
            helper_text: "input value that's >= 0 and is < 9999"
            required: True


<IngredientCollectorWidget>:
    id: product_input_widget
    adaptive_height: True
    row_default_height: '50dp'
    cols_minimum: {0:10}
    cols: 3

    MDBoxLayout:
        size_hint_x: 0.15

        MDLabel:
            id: label_text
            text: root.product
            halign: 'left'
            valign: 'bottom'

    BoxLayout:
        size_hint_x: 0.4

        MDTextField:
            id: input_value
            on_text_validate: (lambda : root.input_error(0) if root.is_valid() else root.input_error(1))()
            input_filter: 'int'
            hint_text: 'Input ingredients'
            helper_text_mode: 'on_error'
            helper_text: "input value that's >= 0 and is < 9999"
            required: True

    BoxLayout:
        size_hint_x: 0.2

        MDDropDownItem:
            id: input_unit
            pos_hint: {'center_y': .62}
            text: root.unit
            on_release: root.unit_menu.open()


<ProductScreen>:

    ScrollView:
        do_scroll_y: True
        do_scroll_x: False

        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            padding: '20dp'
            spacing: '20dp'

            MDCard:
                id: orgCard
                orientation: "vertical"
                size_hint: [0.9, None]
                height: self.minimum_height
                pos_hint: {"center_x": .5, "center_y": .5}
                spacing: '10dp'
                elevation: '0.5dp'

                MDBoxLayout:
                    adaptive_height: True
                    padding: '10dp'
                    md_bg_color: app.theme_cls.primary_color

                    MDLabel:
                        font_style: 'H5'
                        text: root.title
                        theme_text_color: "Custom"
                        text_color: app.blue
                        size_hint_y: None
                        height: self.texture_size[1]

                MDGridLayout:
                    id: orgGrid
                    on_adaptive_height: root.DisplayOrg()
                    cols: 2
                    adaptive_height: True
                    padding: '25dp'
                    spacing: '35dp'

            MDGridLayout:
                cols: 2
                rows: 1
                adaptive_height: True

                AnchorLayout:
                    MDRaisedButton:
                        elevation: '5dp'
                        text: '#ingredients'
                        text_color: app.yellow
                        md_bg_color: app.blue
                        on_release: root.ingredient_collector_Screen()

                AnchorLayout:
                    MDRaisedButton:
                        elevation: '5dp'
                        text: '#products'
                        text_color: app.yellow
                        md_bg_color: app.blue
                        on_release: root.product_collector_Screen()

"""

if __name__ == '__main__':
    EasyMixCalculatorApp().run()