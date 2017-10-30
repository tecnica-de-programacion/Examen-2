from tkinter import *

class MainView(Tk):
    class Constants:
        title = " ! PIZARRA MAGICA ¡"
        height = 800
        width = 800
        center = N + S + E + W
        height_canvas = 500
        width_canvas = 600
        pos_x = 0
        pos_y = 0

        event_but = "<Button-1>"
        event_del = "<space>"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width,cls.height)


        def __pencil_pos(cls, new_x, new_y):
            cls.pos_x= new_x
            cls.pos_y = new_y

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.maxsize(self.Constants.width, self.Constants.height)
        self.minsize(self.Constants.width, self.Constants.height)

        self.__canvas = Canvas(self,width = self.Constants.width_canvas, height = self.Constants.height_canvas)
        self.__canvas.grid(row = 0, column = 0, sticky = self.Constants.center)

        self.__pencil = None

    def space_work(self, pos_x, pos_y):
        if self.__pencil is not None:
            self.__pencil = self.__canvas.create_rectangle( 0 , 0 , 0 , 0 ,fill = "white")
        self.__pencil = self.__canvas.create_rectangle(self.Constatns.pos_x,self.Constants.height_canvas - self.Constants.pos_y,pos_x,self.Constants.height_canvas - pos_y,fill = "white")

