from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigth = 650
        width = 1000
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(self.Constants.width, self.Constants.heigth)
        self.minsize(self.Constants.width, self.Constants.heigth)
        self.__canvas = Canvas(self, width=self.Constants.width, height=self.Constants.heigth)
        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__draw_window = self.__canvas.create_rectangle(200, 20, 800, 520, fill="silver")