from tkinter import Tk, Canvas, Label, N, S, E, W, Button
from Views.ColorButton import ColorButton

class MainView(Tk):
    class Constants:
        title = 'Pizarra mágica'
        drawing_screen_height = 500
        drawing_screen_width = 600
        width = 900
        height = 650
        left_width = 100
        bg = '#8f0595'
        event_space = '<space>'
        buttons_width = 750
        black_button_y = 150
        red_button_y = 250
        green_button_y = 350
        blue_button_y = 450
        Black = "#000000"
        Blue = '#0000bb'
        Red = "#ff0000"
        Green = '#00bb00'

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)

    def __init__(self, tap_handler = None):
        super().__init__()
        self.__tap_handler = tap_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.height)
        self.maxsize(self.Constants.width, self.Constants.height)
        self.config(bg = self.Constants.bg)
        self.__configure_ui()

    def __configure_ui(self):
        self.__canvas = Canvas(self, width=self.Constants.drawing_screen_width,
                               height=self.Constants.drawing_screen_height)
        self.__canvas.place(x=self.Constants.left_width,
                            y=(self.Constants.height - self.Constants.drawing_screen_height) / 2)
        self.__black_button = ColorButton(self, self.Constants.buttons_width, self.Constants.black_button_y,
                                          self.Constants.Black, action=self.__did_tap)
        self.__red_button = ColorButton(self, self.Constants.buttons_width, self.Constants.red_button_y,
                                        self.Constants.Red, action=self.__did_tap)
        self.__blue_button = ColorButton(self, self.Constants.buttons_width, self.Constants.blue_button_y,
                                         self.Constants.Blue, action=self.__did_tap)
        self.__green_button = ColorButton(self, self.Constants.buttons_width, self.Constants.green_button_y,
                                          self.Constants.Green, action=self.__did_tap)

    def __did_tap(self, event):
        if self.__tap_handler is None: return
        self.__tap_handler(event)

