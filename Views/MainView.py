from tkinter import *

class MainView(Tk):
    class Constants:
        title = " !PIZARRA MAGICA¡"
        height = 600
        width = 800
        center = N + S + E + W
        height_canvas = 500
        width_canvas = 600

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width,cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(self.Constants.width, self.Constants.height)
        self.minsize(self.Constants.width, self.Constants.height)

        self.__canvas = Canvas(self,width = self.Constants.width_canvas, height = self.Constants.height_canvas)
        self.__canvas.grid(row = 0, column = 0, sticky = self.Constants.center)
        self.space_work()


    def space_work(self):
        self.__space_work = self.__canvas.create_rectangle(100,100,700,800,fill = "white")
