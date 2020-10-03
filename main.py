from kivymd.app import MDApp

from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import webbrowser as wb

Window.size = [300, 520]


class AboutUsPage(ScrollView):
    EM_text = [
        "EasyMixCalculator helps bakers calculate the right amount of ingredients to make large amounts of products.",
        "It also helps customers to calculate the right amounts of ingredients they can use if they don't have the exact amounts of ingredients to make a product."]

    SnowFlake = {'Telephone': '0115 654 300',
                 'Address': 'Building 5\nMaxwell Office Park\nMagwa Crescent West\nWaterfall City\n2090',
                 'Customer Care Email': 'customercare@premierfmcg.com',
                 'Customer Care': '0860 122 300',
                 'Website': 'www.snowflake.co.za',

                 'SocialMedia': {'facebook': 'snowflakesouthafrica',
                                 'instagram': 'snowflake_sa',
                                 'youtube': 'Snowflake Life'}
                 }

    @staticmethod
    def open_browser(instance, *args, **kwargs):
       print(f"https://{instance.text}")


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


if __name__ == "__main__":
    app = EasyMixCalculatorApp()
    app.run()
