from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):

    class Constants:

        title = "Etch a Sketch 2017 /,,/"
        canvas_height = 600
        canvas_width = 500
        center = N + S + E + W

        screen_height = 1000
        screen_width = 1000

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.screen_width, cls.screen_height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__canvas = Canvas(self, width = self.Constants.canvas_width, height = self.Constants.canvas_height)

        self.__canvas.grid(row = 1 , column = 2, sticky = self.Constants.center)