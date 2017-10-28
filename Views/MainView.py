from tkinter import Tk, Canvas, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Board"
        height = 500
        width = 600
        center = N + S + E + W
        x_pos = 0
        y_pos = 0

        color = "black"


        @classmethod
        def size (cls):
            return '{}x{}'.format(cls.width,cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__dot = None
        self.maxsize(width=self.Constants.width, height=self.Constants.height)
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.__canvas = Canvas(self, width=self.Constants.width, height=self.Constants.height)
        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)





    def update_dot(self, x_value, y_value):
        self.__dot = self.__canvas.create_rectangle(x_value-1, y_value-1, x_value, y_value, fill = self.Constants.color)

