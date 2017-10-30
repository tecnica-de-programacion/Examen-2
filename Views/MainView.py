from tkinter import Tk, Canvas, PhotoImage
from Views.ColorButton import ColorButton
from Views.ViewEmoji import ViewEmoji

class MainView(Tk):
    class Constants:
        title = 'Pizarra mágica'
        drawing_screen_height = 500
        drawing_screen_width = 600
        width = 900
        height = 650
        left_width = 100
        line_width = 2
        image_with = 12
        Black_image = "Assets/Black.png"
        Blue_image = "Assets/Blue.png"
        Red_image = "Assets/Red.png"
        Green_image = "Assets/Green.png"
        bg = '#510082'
        event_space = '<space>'
        buttons_width = 750
        black_button_y = 145
        red_button_y = 250
        green_button_y = 355
        blue_button_y = 460
        Black = "#000000"
        Blue = '#0000bb'
        Red = "#ff0000"
        Green = '#00bb00'

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)

    class ChangeColor:
        line_color = "#000000"

    def __init__(self, tap_button_handler = None, tap_space_handler = None):
        super().__init__()
        self.__tap_button_handler = tap_button_handler
        self.__tap_space_handler = tap_space_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.height)
        self.maxsize(self.Constants.width, self.Constants.height)
        self.config(bg = self.Constants.bg)
        self.__coordinates = []
        self.__configure_ui()

    def __configure_ui(self):
        self.__canvas = Canvas(self, width=self.Constants.drawing_screen_width,
                               height=self.Constants.drawing_screen_height)
        self.__canvas.place(x=self.Constants.left_width,
                            y=(self.Constants.height - self.Constants.drawing_screen_height) / 2)
        self.__black_image = PhotoImage(file = self.Constants.Black_image)
        self.__black_button = ColorButton(self, self.Constants.buttons_width, self.Constants.black_button_y,
                                          self.Constants.Black, self.__black_image , action=self.__did_button_tap)
        self.__red_image = PhotoImage(file=self.Constants.Red_image)
        self.__red_button = ColorButton(self, self.Constants.buttons_width, self.Constants.red_button_y,
                                        self.Constants.Red, self.__red_image, action=self.__did_button_tap)
        self.__blue_image = PhotoImage(file=self.Constants.Blue_image)
        self.__blue_button = ColorButton(self, self.Constants.buttons_width, self.Constants.blue_button_y,
                                         self.Constants.Blue, self.__blue_image, action=self.__did_button_tap)
        self.__green_image = PhotoImage(file=self.Constants.Green_image)
        self.__green_button = ColorButton(self, self.Constants.buttons_width, self.Constants.green_button_y,
                                          self.Constants.Green, self.__green_image, action=self.__did_button_tap)
        self.__image = ViewEmoji(self)
        self.__image.place(x = self.Constants.buttons_width, y = self.Constants.image_with)

    def __did_button_tap(self, color):
        if self.__tap_button_handler is None: return
        self.__tap_button_handler(color)

    def __did_space_tap(self, space):
        if self.__tap_space_handler is None: return
        self.__tap_space_handler()

    def update_canvas(self, x, y):
        if self.__coordinates:
            self.__canvas.create_line(self.__coordinates[0], self.__coordinates[1], x, y, width = self.Constants.line_width, fill = self.ChangeColor.line_color)
            if self.__coordinates[0] == x and self.__coordinates[1] == y:
                self.__image.change_image(False)
            else:
                self.__image.change_image(True)
            self.__coordinates[0] = x
            self.__coordinates[1] = y
        else:
            self.__coordinates.append(x)
            self.__coordinates.append(y)

        self.bind(self.Constants.event_space, self.__did_space_tap)

    def clean_screen(self):
        self.__canvas = Canvas(self, width=self.Constants.drawing_screen_width,
                               height=self.Constants.drawing_screen_height)
        self.__canvas.place(x=self.Constants.left_width,
                            y=(self.Constants.height - self.Constants.drawing_screen_height) / 2)
        self.__image.change_image(None)

