from tkinter import Tk, Canvas, Label, N, S, E, W
from Models.MainModel import MainModel

class MainView(Tk):

    class Constants:
        title = "--Pizarron magico--"
        height = 800
        width = 800
        width_canvas = 500
        height_canvas = 600
        center = N + S + E + W
        text_label = "cambia el color"
        radio = 5

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width,cls.height)


    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__controller = MainModel()

        self.maxsize(self.Constants.width, self.Constants.height)
        self.minsize(self.Constants.width,self.Constants.height)

        self.__canvas = Canvas(self, width = self.Constants.width_canvas, height = self.Constants.height_canvas)
        self.__canvas.create_rectangle(0,0,self.Constants.width_canvas,self.Constants.height_canvas,fill = "blue")

        self.grid_rowconfigure(0, weight = True)
        self.grid_columnconfigure(0, weight = True)

        #self.__canvas.grid(row = 0, column = 0)
        self.__canvas.place(x=0,y=0)

    def update_pointer(self,data):
        coordinates_tupla = self.__controller.handle_data(data)
        x = coordinates_tupla[0]
        y =coordinates_tupla[1]
        self.__canvas.create_oval(x-self.Constants.radio,y-self.Constants.radio,x+self.Constants.radio,y+self.Constants.radio,fill = "red" )





