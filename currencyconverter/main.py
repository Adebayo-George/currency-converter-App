from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

Window.size = (500, 700)

Builder.load_file('converter.kv')

class MyLayout(Widget):
    from_currency_str = StringProperty()
    to_currency_str = StringProperty()

    def convert(self):
        # create a var for currency amount
        amount = float(self.ids.currency_input.text)

        # self.ids.convert_label.text = f'Conversion is: {amount}'

        # set a condition from converting one currency to another
        from_currency = self.from_currency_str    # using properties to hold conversions...
        to_currency = self.to_currency_str

        if from_currency == "ngn" and to_currency == "usd":
            conversion = amount / 415.75
        elif from_currency == "usd" and to_currency == "ngn":
            conversion = amount * 415.75
        elif from_currency == "euro" and to_currency == "ngn":
            conversion = amount * 546.03
        elif from_currency == "ngn" and to_currency == "euro":
            conversion = amount / 546.03

        else:
            conversion = 'Unsupported Conversion'
        # update the label to converted amount
        self.ids.convert_label.text = f'Conversion is: {conversion:.2f}'

class CurrencyConverterApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CurrencyConverterApp().run()

