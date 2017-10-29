from tkinter import Tk, Canvas, PhotoImage, Label, Button, N, S, E, W


class MainView(Tk):
    class Constants:
        title = "Board"
        canvas_height = 500
        canvas_width = 600
        canvas_color = "salmon"
        height = 619
        width = 725
        pokemon_width = 125
        center = N + S + E + W
        color = "black"
        black_file = "Assets/black.ppm"
        blue_file = "Assets/blue.ppm"
        green_file = "Assets/green.ppm"
        red_file = "Assets/red.ppm"
        title_file = "Assets/pokecap.ppm"
        color_event = "<Button-1>"

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width,cls.height)

    def __init__(self, eraser_handler = None, color_handler = None):
        super().__init__()
        self.__eraser_handler = eraser_handler
        self.__color_handler = color_handler
        self.__dot = None
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(width=self.Constants.width, height=self.Constants.height)
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=True)
        self.grid_rowconfigure(1, weight=True)
        self.grid_rowconfigure(2, weight=True)
        self.grid_rowconfigure(3, weight=True)
        self.grid_rowconfigure(4, weight=True)
        self.grid_columnconfigure(0, weight=True, minsize=self.Constants.canvas_width)
        self.grid_columnconfigure(1, weight=True, minsize=self.Constants.pokemon_width)

    def __configure_UI(self):
        self.__canvas = Canvas(self, width=self.Constants.canvas_width, height=self.Constants.canvas_height)
        self.__canvas.grid(row=1, column=0,  rowspan=500, sticky=self.Constants.center)
        self.__canvas.create_rectangle(0, 0, 600, 500, fill=self.Constants.canvas_color)

        self.__title_image = PhotoImage(file=self.Constants.title_file)
        self.__title_label = Label(image=self.__title_image)
        self.__title_label.grid(row=0, column=0, columnspan=775, sticky=self.Constants.center)
        self.__title_label.bind(self.Constants.color_event, self.__did_tap_color_change)

        self.__black_image = PhotoImage(file=self.Constants.black_file)
        self.__black_button = Button(image = self.__black_image)
        self.__black_button.grid(row=1, column=1, sticky=self.Constants.center)
        self.__black_button.bind(self.Constants.color_event, self.__did_tap_color_change)

        self.__blue_image = PhotoImage(file=self.Constants.blue_file)
        self.__blue_button = Button(image=self.__blue_image)
        self.__blue_button.grid(row=2, column=1, sticky=self.Constants.center)
        self.__blue_button.bind(self.Constants.color_event, self.__did_tap_color_change)

        self.__green_image = PhotoImage(file=self.Constants.green_file)
        self.__green_button = Button(image=self.__green_image)
        self.__green_button.grid(row=3, column=1, sticky=self.Constants.center)
        self.__green_button.bind(self.Constants.color_event, self.__did_tap_color_change)

        self.__red_image = PhotoImage(file=self.Constants.red_file)
        self.__red_button = Button(image=self.__red_image)
        self.__red_button.grid(row=4, column=1, sticky=self.Constants.center)
        self.__red_button.bind(self.Constants.color_event, self.__did_tap_color_change(self.Constants.color_event, "blue"))

    def __did_tap_color_change(self, event, color):
        if self.__color_handler is None:
            return

    def update_dot(self, x_value, y_value):
        self.__dot = self.__canvas.create_line(x_value-1, y_value-1, x_value, y_value, fill = self.Constants.color)

    def erase_window(self):
        self.__canvas.create_rectangle(0, 0, 600, 500, fill=self.Constants.canvas_color)




