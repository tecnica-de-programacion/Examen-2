from tkinter import Tk, Canvas, Frame, N, S, E, W
from Views.ColorButton import ColorButton

class MainView(Tk):
    class Constants:
        title = 'Pizarra Magica'
        height = 700
        width = 500
        center = N + S + E + W
        span = 4

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.height)
        self.maxsize(self.Constants.width, self.Constants.height)
        self.__configure_ui()
        self.__configure_grid()

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight = True)
        self.grid_columnconfigure(0, weight = True)
        self.grid_rowconfigure(1, minsize = self.Constants.height - 600, weight = True)

        for column_index in range(1, 4):
            self.grid_columnconfigure(column_index, minsize = self.Constants.width / 4, weight = True)

    def __configure_ui(self):
        self.__canvas = Canvas(self, width = self.Constants.width, height = self.Constants.height)
        self.__canvas.grid(row = 0, column = 0, sticky = self.Constants.center, columnspan = self.Constants.span)

        self.__blue_button = ColorButton(self, 'Blue', '#278ad1')
        self.__blue_button.position(1, 0)
        self.__green_button = ColorButton(self, 'Green', '#1cb714')
        self.__green_button.position(1, 1)
        self.__red_button = ColorButton(self, 'Red', '#e00808')
        self.__red_button.position(1, 2)
        self.__black_button = ColorButton(self, 'Black', '#202020')
        self.__black_button.position(1, 3)

    def update_line(self, horizontal, vertical):
        self.__canvas.create_line(horizontal, vertical, horizontal + 1, vertical + 1, fill = 'black')

