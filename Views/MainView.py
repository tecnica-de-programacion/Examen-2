from tkinter import Tk, Canvas, Label, N, S, E, W
from Views.Button import ColorButton
from Views.ColorMenuView import ColorMenuView

class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigth = 500
        width = 700
        heigth_canvas = 500
        width_canvas = 600
        center = N + S + E + W
        span = 5

        @classmethod
        def size (cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, tap = None):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.heigth)
        self.configure_ui()
        self.configure_grid()

    def configure_ui(self):
        self.__label = Label(self, bg = '#BDC3C7' )
        self.__canvas = Canvas(self, width=self.Constants.width_canvas, height=self.Constants.heigth_canvas, bg = '#ffffff')

        self.__ColorMenuView = ColorMenuView(self)

    def configure_grid(self):
        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center, rowspan = self.Constants.span)
        self.__label.grid(row=0, column = 1, sticky = self.Constants.center)

    def update_position(self, coordinates):
        self.__label.configure(text = coordinates)

    def update_line(self, coordinates):
        self.__canvas.create_line(coordinates)

