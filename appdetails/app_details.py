"""
contains the screen to display app details
"""
from kivy.uix.scrollview import ScrollView

from kivymd.toast import toast
from kivymd.uix.label import MDLabel

import pyperclip as clipboard
import re


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
    ingredient_btn_help_p1 = "This button will take you to a page where you will input the ingredients you currently  " \
                             "have."

    ingredient_btn_help_p2 = "If an ingredient is too small you will be asked to increase its size or unit."

    ingredient_btn_help_p3 = "On completion it will show you the exact amounts of each ingredient that you can use to " \
                             "make a certain amount of the product "

    product_btn_help_p1 = "This button will take you to a page where you will input the amount of product you want to " \
                          "make"

    product_btn_help_p2 = "If the amount of product you provide is too small you will be asked to increase it."

    product_btn_help_p3 = "On completion it will show you the exact amounts of each ingredient that you can use to " \
                             "make the provided amount of the product "

    input_help_p1 = "This is where you will provide the measurement/amount of ingredient you have"

    input_help_error = "Cannot be smaller than or equal to zero.\n\ncannot be larger than 9999"

    dropdown_help_p1 = "This is where you can change the unit of the ingredient."

