from tkinter import *

class MainView(Tk):
    class Constants:
        title = " !PIZARRA MAGICA¡"
        heigth = 600
        width = 800
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width,cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(self.Constants.width, self.Constants.heigth)
