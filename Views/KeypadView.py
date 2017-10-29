from Views.ButtonPrototype import ButtonPrototype

class KeypadView():

    def __init__(self, master, tap_button_handler = None):
        self.__tap_button_handler = tap_button_handler
        black_button = ButtonPrototype(master, "Black", "#000000", action = self.__did_tap)
        black_button.position(3, 0)
        red_button = ButtonPrototype(master, "Red", "#FF0000", action = self.__did_tap)
        red_button.position(3, 1)
        green_button = ButtonPrototype(master, "Green", "#138D75", action = self.__did_tap)
        green_button.position(3, 2)
        blue_button = ButtonPrototype(master, "Blue", "#2980B9", action = self.__did_tap)
        blue_button.position(3, 3)

    def __get_color_updated(self):
        pass

    def __did_tap(self, sender):
        if self.__tap_button_handler is None: return
        self.__tap_button_handler(sender)
