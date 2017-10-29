from tkinter import Tk, Label, Canvas, N, S, E, W

class MainView(Tk):
    class Constants:
        title = 'Pizarra Magica'
        height = 800
        width = 500
        center = N + S + E + W
        color = "#a2a2a2"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.height)
        self.maxsize(self.Constants.width, self.Constants.height)

        self.__canvas = Canvas(self, width = self.Constants.width, height = self.Constants.height - 200)

        self.__canvas.grid(row = 0, column = 0, sticky = self.Constants.center)

        self.grid_columnconfigure(0, weight = True)
        self.grid_rowconfigure(0, weight = True)