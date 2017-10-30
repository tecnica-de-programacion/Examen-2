from tkinter import Tk, Canvas, Label, N, S, E, W, PhotoImage, Button

class MainView(Tk):

    class Constants:

        title = "Etch a Sketch"
        canvas_height = 500
        canvas_wid  th = 600
        center = N + S + E + W

        black_on = "Assets/black_button_on.ppm"

        event = "<Button-1>"

        color = "Black"

        screen_height = 600
        screen_width = 600

        horizontal_position = 0
        vertical_position = 0

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.screen_width, cls.screen_height)

        @classmethod
        def positions(cls, new_horizontal_position, new_vertical_position):
            cls.horizontal_position = new_horizontal_position
            cls.vertical_position = new_vertical_position

    def __init__(self):
        super().__init__()

        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__line = None

        self.__canvas = Canvas(self, width = self.Constants.canvas_width, height = self.Constants.canvas_height)
        self.__canvas.bind("<Key>", self.__clean_canvas)
        self.__canvas.bind("<Button-1>", self.__did_tapped_on_canvas)
        self.__canvas.grid(row = 0 , column = 0, sticky = self.Constants.center)

        self.__black = Button(self, command = self.__black_color, text = "Black")
        self.__black.grid(row = 1, column = 0, sticky = self.Constants.center)

        self.__blue_button = Button(self, command = self.__blue_color, text = "Blue")
        self.__blue_button.grid(row = 2, column = 0, sticky = self.Constants.center)

        self.__red_button = Button(self, command = self.__red_color, text = "Red")
        self.__red_button.grid(row = 3, column = 0, sticky = self.Constants.center)

        self.__green_button = Button(self, command = self.__green_color, text = "Green")
        self.__green_button.grid(row = 4, column = 0, sticky = self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)

    def __blue_color(self):
        self.Constants.color = "Blue"

    def __black_color(self):
        self.Constants.color = "Black"

    def __red_color(self):
        self.Constants.color = "Red"

    def __green_color(self):
        self.Constants.color = "Green"

    def drawing_line(self, horizontal_position, vertical_position):
        if self.__line == None: self.__line = self.__canvas.create_line( 0 , 0 , 0 , 0 ,fill = self.Constants.color, width = 0)
        else: self.__line = self.__canvas.create_line( self.Constants.horizontal_position ,self.Constants.canvas_height - self.Constants.vertical_position , horizontal_position ,self.Constants.canvas_height - vertical_position ,fill = self.Constants.color, width = 1)

    def __clean_canvas(self, event):
        if repr(event.char) == "' '":
            self.__canvas.delete("all")

    def __did_tapped_on_canvas(self, event):
        self.__canvas.focus_set()