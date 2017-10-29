from tkinter import Tk, Canvas, Label, N, S, E, W, Frame
from Models.Brain import MainModel


class MainView(Tk):
    class Constants:
        title = "Pizarra Mágica"
        width = 900
        height = 700
        height_pizarra = 600
        width_pizarra = 500
        center = N + S + E + W


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__frame = Frame(self)
        self.__frame.grid(column = 0, row = 0)

        self.configure(background = 'blue')

        self.__controller = MainModel()
        self.maxsize(self.Constants.width,self.Constants.height)
        self.minsize(self.Constants.width, self.Constants.height)
        self.__canvas = Canvas(self.__frame, width = self.Constants.width_pizarra, height = self.Constants.height_pizarra)
        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__canvas.create_rectangle(0, 0, self.Constants.width_pizarra, self.Constants.height_pizarra, fill = 'white')
        self.__label = Label(self.__frame, text = 'COLORES')

        self.__label.grid(row=0, column=3, sticky = N + E)
        self.grid_rowconfigure(0, weight = True)
        self.grid_columnconfigure(0, weight = True)

    def draw_line (self, initial_x, initial_y, data):
        vector = self.__controller.handle_data(data)
        x = vector[0]
        y = vector[1]

        self.__canvas.create_line(initial_x, initial_y,x,y)
        return vector
