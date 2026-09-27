from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


# ---------- Your existing conversion functions (unchanged) ----------

def decimal_to_binary(number):
    if number == 0:
        return "0"
    binary_list = []
    while number > 0:
        remainder = number % 2
        binary_list.append(remainder)
        number = number // 2
    return "".join(str(x) for x in binary_list[::-1])


def decimal_to_octal(number):
    if number == 0:
        return "0"
    octal_list = []
    while number > 0:
        remainder = number % 8
        octal_list.append(remainder)
        number = number // 8
    return "".join(str(x) for x in octal_list[::-1])


def decimal_to_hexadecimal(number):
    if number == 0:
        return "0"
    lookup = "0123456789ABCDEF"
    hexadecimal_list = []
    while number > 0:
        remainder = number % 16
        hexadecimal_list.append(lookup[remainder])
        number = number // 16
    return "".join(hexadecimal_list[::-1])


def binary_to_decimal(number):
    string = str(number)
    result = 0
    power = 0
    for i in reversed(string):
        result += int(i) * (2 ** power)
        power += 1
    return result


def octal_to_decimal(number):
    string = str(number)
    result = 0
    power = 0
    for i in reversed(string):
        result += int(i) * (8 ** power)
        power += 1
    return result


def hexadecimal_to_decimal(string):
    lookup = "0123456789ABCDEF"
    result = 0
    power = 0
    for i in reversed(string):
        digit_value = lookup.index(i)
        result += digit_value * (16 ** power)
        power += 1
    return result


# ---------- Conversion dispatch table ----------

CONVERSIONS = {
    "Decimal to Binary": lambda n: decimal_to_binary(int(n)),
    "Decimal to Octal": lambda n: decimal_to_octal(int(n)),
    "Decimal to Hexadecimal": lambda n: decimal_to_hexadecimal(int(n)),
    "Binary to Decimal": lambda n: binary_to_decimal(int(n)),
    "Octal to Decimal": lambda n: octal_to_decimal(int(n)),
    "Hexadecimal to Decimal": lambda n: hexadecimal_to_decimal(n.upper()),
    "Binary to Octal": lambda n: decimal_to_octal(binary_to_decimal(int(n))),
    "Binary to Hexadecimal": lambda n: decimal_to_hexadecimal(binary_to_decimal(int(n))),
    "Octal to Binary": lambda n: decimal_to_binary(octal_to_decimal(int(n))),
    "Hexadecimal to Binary": lambda n: decimal_to_binary(hexadecimal_to_decimal(n.upper())),
    "Octal to Hexadecimal": lambda n: decimal_to_hexadecimal(octal_to_decimal(int(n))),
    "Hexadecimal to Octal": lambda n: decimal_to_octal(hexadecimal_to_decimal(n.upper())),
}


# ---------- Kivy GUI ----------

class ConverterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=15, **kwargs)

        self.spinner = Spinner(
            text="Decimal to Binary",
            values=list(CONVERSIONS.keys()),
            size_hint=(1, 0.2),
        )
        self.add_widget(self.spinner)

        self.input_field = TextInput(
            hint_text="Enter number here",
            multiline=False,
            size_hint=(1, 0.2),
        )
        self.add_widget(self.input_field)

        convert_button = Button(text="Convert", size_hint=(1, 0.2))
        convert_button.bind(on_press=self.do_conversion)
        self.add_widget(convert_button)

        self.result_label = Label(text="Result will appear here", size_hint=(1, 0.4))
        self.add_widget(self.result_label)

        credit_label = Label(
            text="Made by Yashraj & Jyothikaa",
            size_hint=(1, 0.1),
            font_size="12sp",
        )
        self.add_widget(credit_label)

    def do_conversion(self, instance):
        choice = self.spinner.text
        value = self.input_field.text.strip()

        if not value:
            self.result_label.text = "Please enter a number"
            return

        try:
            convert_function = CONVERSIONS[choice]
            result = convert_function(value)
            self.result_label.text = f"Result: {result}"
        except ValueError:
            self.result_label.text = "Invalid number for this conversion"
        except Exception as e:
            self.result_label.text = f"Error: {e}"


class ConverterApp(App):
    def build(self):
        return ConverterLayout()


if __name__ == "__main__":
    ConverterApp().run()