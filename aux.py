from tkinter import Tk, Canvas, Label, Frame, N, S, E, W, Button
from Models.MainModel import MainModel
from Views.ButtonsConstruct import Buttons


class MainView(Tk):


    class Constants:
        title = "--Pizarron magico--"
        height = 800
        width = 1000
        width_canvas = 500
        height_canvas = 600
        center = N + S + E + W
        text_label = "Cambia el color de la linea"
        radio = 5
        colores = ["green","red","blue", "black"]
        h_button = -1

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width,cls.height)


    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())


        #self.__frame = Frame(self)
        #self.__frame.grid(column =0, row = 0)

        self.configure(background = "dark red")

        self.__controller = MainModel()
        self.maxsize(self.Constants.width, self.Constants.height)
        self.minsize(self.Constants.width,self.Constants.height)


        self.__canvas = Canvas(self, width = self.Constants.width_canvas, height = self.Constants.height_canvas)
        self.__canvas.grid(column = 0, row= 0,columnspan = 5, rowspan = 10, sticky = self.Constants.center)
        #self.__canvas.create_rectangle(0,0,self.Constants.width_canvas,self.Constants.height_canvas,fill = "blue")

        #for color in self.Constants.colores:
         #   self.Constants.h_button += 1
          #  self.button = Buttons(self,color)
          #  self.button.position(self.Constants.h_button,3)


        self.grid_rowconfigure(0, weight = 0)
        self.grid_columnconfigure(0, weight = 1)






    def draw_figure(self,last_x,last_y,data,figure):
        coordinates_tupla =self.__controller.handle_data(data)
        x = coordinates_tupla[0]
        y = coordinates_tupla[1]
        if figure == "lines":
            if abs(x - int(last_x)) > 5 or abs(y - int(last_y)) > 5:
                self.__canvas.create_line(last_x,last_y,x,y)
                return coordinates_tupla
        else:
            self.__canvas.create_oval(x - self.Constants.radio, y - self.Constants.radio, x + self.Constants.radio,
                                      y + self.Constants.radio, fill="red")
            return None



