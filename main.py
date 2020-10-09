from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.toast import toast

from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import pyperclip as clipboard
import re

Window.size = [300, 520]


class EasyMixCalculatorApp(MDApp):

    def __init__(self, **kwargs):
        super(EasyMixCalculatorApp, self).__init__(**kwargs)
        self.grey = [226 / 255, 226 / 255, 226 / 255, 1]
        self.yellow = [255 / 255, 218 / 255, 6 / 255, 1]
        self.blue = [0 / 255, 35 / 255, 234 / 255, 1]
        self.red = [226 / 255, 19 / 255, 19 / 255, 1]
        self._loaded_kv_file = Builder.load_file('EasyMixCalculator.kv')

    def build(self):
        # self.theme_cls.theme_style = 'Dark'
        return self._loaded_kv_file

    @staticmethod
    def change_screen(manager: ScreenManager, page, direction='left'):
        manager.transition.direction = direction
        manager.current = page


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
                                 'youtube': '[ref=YouTube]Snowflake Life[/ref]'}
                 }

    # Developer info
    App_Dev = {'profile': "Lelethu Futshane",
               'gmail': "[ref=CopyPaste]ellokoprograma@gmail.com[/ref]",
               'github': "[ref=GitHub]Elloko233[/ref]"}

    def __init__(self, **kwargs):
        super(AboutUsPage, self).__init__(**kwargs)
        # Dictionary of the linked to the corresponding functions
        self.ref_pattern = {'(\[ref=WebSite\])(?P<WebSite>.*)(\[/ref\])': self.open_site,
                            '(\[ref=CopyPaste\])(?P<Copy>.*)(\[/ref\])': self.copyPaste,
                            '(\[ref=Facebook\])(?P<Facebook>.*)(\[/ref\])': self.open_facebook,
                            '(\[ref=Instagram\])(?P<Instagram>.*)(\[/ref\])': self.open_instagram,
                            '(\[ref=YouTube\])(?P<YouTube>.*)(\[/ref\])': self.open_youtube,
                            '(\[ref=GitHub\])(?P<GitHub>.*)(\[/ref\])': self.open_git}

    # Handles ref attributes from labels
    def RefHandler(self, instance: MDLabel, *args, **kwargs):
        # Handles the ref tagged labels
        for pattern in self.ref_pattern:
            # Finding the match from txt
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


if __name__ == "__main__":
    app = EasyMixCalculatorApp()
    app.run()
