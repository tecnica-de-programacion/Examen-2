from tkinter import *
from Views.ColorButton import ColorButton

class MainView(Tk):
    class Constants:
        title = 'Pizarra Magica'
        height = 700
        width = 500
        center = N + S + E + W
        span = 4
        last_horizontal = None
        last_vertical = None
        color = "#202020"

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

        self.bind("<space>", self.clean)

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=True)
        self.grid_rowconfigure(1, minsize = self.Constants.height - 600, weight=True)

        for column_index in range(0, 4):
            self.grid_columnconfigure(column_index, minsize=self.Constants.width / 4, weight=True)

    def __configure_ui(self):
        self.__canvas = Canvas(self, width = self.Constants.width, height = self.Constants.height, bg = 'gray')
        self.__canvas.grid(row = 0, column = 0, sticky = self.Constants.center, columnspan = self.Constants.span)

        self.__blue_button = ColorButton(self, 'Blue', '#278ad1', click_handler = self.__color_chooser)
        self.__blue_button.position(1, 0)
        self.__green_button = ColorButton(self, 'Green', '#1cb714', click_handler = self.__color_chooser)
        self.__green_button.position(1, 1)
        self.__red_button = ColorButton(self, 'Red', '#e00808', click_handler = self.__color_chooser)
        self.__red_button.position(1, 2)
        self.__black_button = ColorButton(self, 'Black', '#202020', click_handler = self.__color_chooser)
        self.__black_button.position(1, 3)

    def __color_chooser(self, color):
        self.Constants.color = color

    def update_line(self, horizontal, vertical):
        if not self.Constants.last_horizontal:
            self.Constants.last_horizontal = horizontal
            self.Constants.last_vertical = vertical
        self.__canvas.create_line(self.Constants.last_horizontal, self.Constants.last_vertical, horizontal, vertical, fill = self.Constants.color, width = 4)
        self.Constants.last_horizontal = horizontal
        self.Constants.last_vertical = vertical

    def clean(self, event):
        self.__canvas.delete(ALL)

