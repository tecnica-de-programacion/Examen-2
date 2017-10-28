from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants():
        title = "Pizarra Mágica"
        height = 600
        width = 800
        height_sketch = 500
        width_sketch = 600
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(self.Constants.width, self.Constants.height)
        self.minsize(self.Constants.width, self.Constants.height)
        self.config(bg = "#DA5D16")

        self.__label = Label(self)
        self.__canvas = Canvas(self, width = self.Constants.width_sketch, height = self.Constants.height_sketch)

        self.__canvas.grid(column=0, sticky=self.Constants.center)
        self.__canvas.grid(column=2, sticky=self.Constants.center)
        self.__canvas.grid(row = 1, column = 1, sticky = self.Constants.center)
        self.columnconfigure(0, minsize = int((self.Constants.width - self.Constants.width_sketch)/2))
        self.columnconfigure(1, minsize= int((self.Constants.width - self.Constants.width_sketch)/2))
        self.columnconfigure(2, minsize= int((self.Constants.width - self.Constants.width_sketch)/2))
        self.rowconfigure(0, minsize = int((self.Constants.height - self.Constants.height_sketch)/2))
        self.rowconfigure(1, minsize=int((self.Constants.height - self.Constants.height_sketch) / 2))
        self.rowconfigure(2, minsize=int((self.Constants.height - self.Constants.height_sketch) / 2))

