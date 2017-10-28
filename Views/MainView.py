from tkinter import *

class MainView(Tk):
    class Constants:
        title = "Board"
        height = 500
        width = 600
        center = N + S + E + W
        x_pos = 0
        y_pos = 0
        color = "black"
        erase_color = "white"
        event = "<Enter>"

        @classmethod
        def size (cls):
            return '{}x{}'.format(cls.width,cls.height)

    def __init__(self, eraser_handler = None):
        super().__init__()
        self.__eraser_handler = eraser_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__dot = None
        self.maxsize(width=self.Constants.width, height=self.Constants.height)
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.__canvas = Canvas(self, width=self.Constants.width, height=self.Constants.height)
        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__canvas.bind(self.Constants.event, self.__did_tap_eraser)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)

    def update_dot(self, x_value, y_value):
        self.__dot = self.__canvas.create_rectangle(x_value, y_value, x_value, y_value, fill = self.Constants.color)

    def __did_tap_eraser(self, event):
        if self.__eraser_handler is None:
            return
        self.__eraser_handler()

    def erase_window(self):
        self.__canvas.create_rectangle(0, 0, 600, 500, fill=self.Constants.erase_color)

