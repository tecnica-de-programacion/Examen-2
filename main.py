from tkinter import Tk, Button, Label, PhotoImage, Canvas, N, S, E, W

class DrawScreen(Canvas):
    class Constants:
        drawing_screen_height = 500
        drawing_screen_width = 600
        color_bg = '#911e5d'

    def __init__(self, master, drawing_screen_height, drawing_screen_width):
        super().__init__(master)
        self.__drawing_canvas = Canvas(self, width=self.Constants.drawing_screen_width,
                               height=self.Constants.drawing_screen_height, bg=self.Constans.color_bg)
        self.__drawing_canvas.place(x=200, y=100)
        self.__drawing_canvas.grid(row = 1, column = 0)

class ColorButton():
    def __init__(self, master, column, color, action=None):
        self.__master = master
        self.__column = column
        self.__color = color
        self.__action = action

    def __press_button_tap(self):
        if self.__action is None: return
        self.__action(self.__color)

class Buttons():
    class Constants:
        Black_image = "Assets/negro.png"
        Blue_image = "Assets/azul.png"
        Green_image = "Assets/verde.png"
        Red_image = "Assets/rojo.png"
        Black = "#262525"
        Blue = '#1025bc'
        Red = "#d60a0a"
        Green = '#4abb00'

    def __init__(self, master, color_handler=None):
        self.__master = master
        self.__configure_buttons(color_handler)

    def __configure_ui(self):
        self.__black_image = PhotoImage(file=self.Constants.Black_image)
        self.__black_button = ColorButton(self, 40, 200, self.Constants.Black, self.__black_image, action=self.__did_button_tap)
        self.__red_image = PhotoImage(file=self.Constants.Red_image)
        self.__red_button = ColorButton(self, 40, 400, self.Constants.Red, self.__red_image, action=self.__did_button_tap)
        self.__blue_image = PhotoImage(file=self.Constants.Blue_image)
        self.__blue_button = ColorButton(self, 740, 200, self.Constants.Blue, self.__blue_image, action=self.__did_button_tap)
        self.__green_image = PhotoImage(file=self.Constants.Green_image)
        self.__green_button = ColorButton(self, 740, 400, self.Constants.Green, self.__green_image, action=self.__did_button_tap)

    def __configure_buttons(self, color_handler):
        self.__label_button_color = LabelFrame(self.__master)
        self.__label_button_color.grid(row=0, column=0)

class MainView(Tk):
    class Constants:
        title = 'Pizarra mágica'
        width = 900
        height = 700
        event_space = '<space>'

        @classmethod
        def size(cls):
            return '{0}x{1}'.format(cls.width, cls.height)

    def __did_button_tap(self, color):
        if self.__tap_button_handler is None: return
        self.__tap_button_handler(color)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.height)
        self.maxsize(self.Constants.width, self.Constants.height)

class MainApp:
    def __init__(self):
        self.__master = MainView()

    def run(self):
        self.__master.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.run()








