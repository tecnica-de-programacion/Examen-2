from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):

    class Constants:

        title = "Etch a Sketch 2017 /,,/"
        canvas_height = 500
        canvas_width = 600
        center = N + S + E + W

        screen_height = 1000
        screen_width = 1000

        horizontal_position = 0
        vertical_position = 0

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.screen_width, cls.screen_height)

        @classmethod
        def positions(cls, new_horizontal_position, new_vertical_position):
            cls.horizontal_position = new_horizontal_position
            cls.vertical_position = new_vertical_position

    def __init__(self, tap_color_handler = None):
        super().__init__()

        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__line = None


        self.__canvas = Canvas(self, width = self.Constants.canvas_width, height = self.Constants.canvas_height)
        self.__canvas.bind("<Key>", self.__clean_canvas)
        self.__canvas.bind("<Button-1>", self.__did_tapped_on_canvas)
        self.__canvas.grid(row = 1 , column = 2, sticky = self.Constants.center)

    def drawing_line(self, horizontal_position, vertical_position):
        print("Horizontal: ", horizontal_position, "Vertical: ", vertical_position)
        if self.__line == None: self.__line = self.__canvas.create_line( 0 , 0 , 0 , 0 ,fill = "#7d5692", width = 0)
        else: self.__line = self.__canvas.create_line( self.Constants.horizontal_position ,self.Constants.canvas_height - self.Constants.vertical_position , horizontal_position ,self.Constants.canvas_height - vertical_position ,fill = "#7d5692", width = 1)

    def __clean_canvas(self, event):
        if repr(event.char) == "' '":
            self.__canvas.delete("all")

    def __did_tapped_on_canvas(self, event):
        self.__canvas.focus_set()