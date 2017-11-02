from tkinter import Tk, Canvas, Label, N, S, W ,E, Button
from Models.LineBrain import LineBrain

class MainView (Tk):
    class Constants ():
        title = "pizarra magica"
        heigth = 650
        width =800
        center =N+W+E+S
        canvas_heigth=500
        canvas_width =600

        event = "<space>"

        @classmethod
        def size (cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__ (self):
        super ().__init__ ()
        self.title (self.Constants.title)
        self.geometry(self.Constants.size())
        self.__canvas_configure ()
        self.color_button_configure()
        self.moving = LineBrain()
        self.real_cordinates = 0

    def __canvas_configure(self):
        self.__canvas = Canvas(self, width= self.Constants.canvas_width, height=self.Constants.canvas_heigth,bg ="white")
        self.__line = None
        self.__canvas.grid(row=0, column=1, sticky=self.Constants.center)
        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)

    def color_button_configure (self):
        pass
        self.__red_button = Button(self, text="red", bg="red", command = self.__color("red"))
        self.__blue_button = Button(self, text="blue",bg ="blue", command= self.__color("blue"))
        self.__green_button = Button(self, text= "green", bg ="green", command= self.__color("green"))
        self.__black_button = Button(self, text= "black", bg ="black", command= self.__color("black"))
        self.__anouncement_of_change = Label(self, text="change your colour",bg="yellow")

        self.__anouncement_of_change.grid(row=1, column=1, sticky=W + E)
        self.__red_button.grid(row=2, column=1, sticky=W + E)
        self.__blue_button.grid(row=3, column=1, sticky=W + E)
        self.__green_button.grid(row =4, column=1, sticky = W + E)
        self.__black_button.grid(row= 5, column =1, sticky= W + E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def update_line(self,vertical_moving,horizontal_moving):
        # if self.__line is not None:
        #     self.__canvas.delete(self.__line)
        self.real_cordinates = self.moving.updating(vertical_moving,horizontal_moving)
        self.__line = self.__canvas.create_line(real_cordinates, fill =color)

    def __color(self,color):
        self.__color = color
        return self.__color







