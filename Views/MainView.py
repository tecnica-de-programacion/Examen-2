from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigth = 700
        width = 1000
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())