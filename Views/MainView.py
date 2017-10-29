from tkinter import Tk, Canvas, PhotoImage, Label, N, S, E, W



class MainView(Tk):
    class Constants:
        title = "Board"
        canvas_height = 500
        canvas_width = 600
        height = 500
        width = 775
        pokemon_width = 175
        center = N + S + E + W
        x_pos = 0
        y_pos = 0
        color = "black"
        erase_color = "white"
        event = "Space"
        black_file = "Assets/black.ppm"
        blue_file = "Assets/blue.ppm"
        green_file = "Assets/green.ppm"
        red_file = "Assets/red.ppm"
        color_event = "<Button-1>"

        @classmethod
        def size (cls):
            return '{}x{}'.format(cls.width,cls.height)

    def __init__(self, eraser_handler = None):
        super().__init__()
        self.__eraser_handler = eraser_handler
        self.__dot = None
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(width=self.Constants.width, height=self.Constants.height)
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True, minsize=self.Constants.canvas_width)
        self.grid_columnconfigure(1, weight=True, minsize=self.Constants.pokemon_width)

    def __configure_UI(self):
        self.__canvas = Canvas(self, width=self.Constants.canvas_width, height=self.Constants.canvas_height)
        self.__canvas.grid(row=0, column=0, rowspan=500, sticky=self.Constants.center)
        self.__canvas.bind(self.Constants.event, self.__did_tap_eraser)

        self.__black_image = PhotoImage(file=self.Constants.black_file)
        self.__black_label = Label(image = self.__black_image)
        self.__black_label.grid(row=0, column=1, sticky=self.Constants.center)
        self.__black_label.bind(self.Constants.color_event, self.color_change("black"))

        self.__blue_image = PhotoImage(file=self.Constants.blue_file)
        self.__blue_label = Label(image=self.__blue_image)
        self.__blue_label.grid(row=1, column=1, sticky=self.Constants.center)
        self.__blue_label.bind(self.Constants.color_event, self.color_change("blue"))

        self.__green_image = PhotoImage(file=self.Constants.green_file)
        self.__green_label = Label(image=self.__green_image)
        self.__green_label.grid(row=2, column=1, sticky=self.Constants.center)
        self.__green_label.bind(self.Constants.color_event, self.color_change("green"))

        self.__red_image = PhotoImage(file=self.Constants.red_file)
        self.__red_label = Label(image=self.__red_image)
        self.__red_label.grid(row=3, column=1, sticky=self.Constants.center)
        self.__red_label.bind(self.Constants.color_event, self.color_change("red"))

    def color_change(self, color):
        self.Constants.color = color

    def update_dot(self, x_value, y_value):
        self.__dot = self.__canvas.create_line(x_value-3, y_value-3, x_value, y_value, fill = self.Constants.color)

    def __did_tap_eraser(self, event):
        if self.__eraser_handler is None:
            return
        self.__eraser_handler()

    def erase_window(self):
        self.__canvas.create_rectangle(0, 0, 600, 500, fill=self.Constants.erase_color)




