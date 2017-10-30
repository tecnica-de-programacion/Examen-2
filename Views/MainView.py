from tkinter import Tk, Canvas, Label, Frame, N, S, E, W, Button, PhotoImage
from Models.MainModel import MainModel
from Views.ButtonsConstruct import Buttons


class MainView(Tk):
    class Constants:
        title = "--Pizarron magico--"
        height = 630
        width = 650
        width_canvas = 500
        height_canvas = 600
        center = N + S + E + W
        radio = 3
        width_line = 2
        h_button = 100
        color_line = "black"


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)


    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__figure = "lines"

        self.configure(background= "dark red")

        self.__controller = MainModel()
        self.maxsize(self.Constants.width, self.Constants.height)
        self.minsize(self.Constants.width, self.Constants.height)

        self.__canvas = Canvas(self, width=self.Constants.width_canvas, height=self.Constants.height_canvas)
        self.__canvas.place(x=10, y=10)


        self.button1 = Button(self, text=" Use color green",background = "green",command=self.__change_colorg).place(x=520,
                                                                                        y=self.Constants.h_button
                                                                                         )



        self.Constants.h_button += 100
        self.button2 = Button(self, text="Use color red",command=self.__change_colorr).place(x=520, y=self.Constants.h_button
                                                                                      )
        self.Constants.h_button += 100
        self.button3 = Button(self, text=" Use color blue",command=self.__change_colorb).place(x=520, y=self.Constants.h_button
                                                                                       )
        self.Constants.h_button += 100
        self.button4 = Button(self, text="Use color black",bg = "black",command=self.__change_colorbl).place(x=520,
                                                                                        y=self.Constants.h_button)
        self.Constants.h_button += 100
        self.button5 = Button(self, text="Change figure ", command=self.__change_figure).place(x=520,
                                                                                                           y=self.Constants.h_button
                                                                                                           )





        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.bind("<space>", self.space_taped)
        self.focus_set()

    def space_taped(self, event):
        self.__canvas.destroy()
        self.__canvas = Canvas(self, width=self.Constants.width_canvas, height=self.Constants.height_canvas)
        self.__canvas.place(x=10, y=10)







    def draw_figure(self, last_x, last_y, data):
        coordinates_tupla = self.__controller.handle_data(data)
        x = coordinates_tupla[0]
        y = coordinates_tupla[1]
        print(coordinates_tupla)
        if self.__figure == "lines":
            if abs(x - int(last_x)) > 5 or abs(y - int(last_y)) > 5:
                self.__canvas.create_line(last_x, last_y, x, y, fill=self.Constants.color_line,width=self.Constants.width_line)
                return coordinates_tupla
        else:
            self.__canvas.create_oval(x - self.Constants.radio, y - self.Constants.radio, x + self.Constants.radio,
                                      y + self.Constants.radio, fill=self.Constants.color_line)

            return None

    def __change_colorg(self):
        self.Constants.color_line = "green"
        self.configure(background="dark " + self.Constants.color_line)

    def __change_colorr(self):
        self.Constants.color_line = "red"
        self.configure(background="dark "+ self.Constants.color_line)

    def __change_colorb(self):
        self.Constants.color_line = "blue"
        self.configure(background="dark " + self.Constants.color_line)

    def __change_colorbl(self):
        self.Constants.color_line = "black"
        self.configure(background=self.Constants.color_line)
    def __change_figure(self):
        self.space_taped("<space>")
        if self.__figure == "lines":
            self.__figure = "circles"
        else:
            self.__figure = "lines"
