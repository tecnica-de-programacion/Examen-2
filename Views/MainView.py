from tkinter import Tk, Canvas, Label, N, S, E, W


class MainView(Tk):
    class Constants:
        title = "Pizarra Mágica"
        width = 900
        heigth = 700
        heigth_pizarra = 500
        width_pizarra = 600
        center = N + S + E + W


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__rectangle = None
        self.__label = Label(self)
        self.__canvas = Canvas(self, width=self.Constants.width / 2, height=self.Constants.heigth)

        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__label.grid(row=0, column=1, sticky=self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)
        self.grid_columnconfigure(1, weight=True, minsize=self.Constants.width / 2)

    def draw (self, last_x, last_y, data):
        pass
