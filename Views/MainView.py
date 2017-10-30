from tkinter import Tk, Canvas, Label, Frame, N, S, E, W, Button, PhotoImage
from Models.MainModel import MainModel
from Views.ButtonsConstruct import Buttons


class MainView(Tk):
    class Constants:
        title = "--Pizarron magico--"
        height = 630
        width = 730
        width_canvas = 500
        height_canvas = 600
        center = N + S + E + W
        radio = 5
        width_line = 1
        h_button = 300
        color_line = "black"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)


    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())


        self.configure(background="dark red")

        self.__controller = MainModel()
        self.maxsize(self.Constants.width, self.Constants.height)
        self.minsize(self.Constants.width, self.Constants.height)

        self.__canvas = Canvas(self, width=self.Constants.width_canvas, height=self.Constants.height_canvas)
        self.__canvas.place(x=10, y=10)


        self.button1 = Button(self, text=" Change the color to green",background = "green",command=self.__change_colorg).place(x=520,
                                                                                        y=self.Constants.h_button
                                                                                         )



        self.Constants.h_button += 30
        self.button2 = Button(self, text="Change the color to red",command=self.__change_colorr).place(x=520, y=self.Constants.h_button
                                                                                      )
        self.Constants.h_button += 30
        self.button3 = Button(self, text=" Change the color to blue",command=self.__change_colorb).place(x=520, y=self.Constants.h_button
                                                                                       )
        self.Constants.h_button += 30
        self.button4 = Button(self, text="Change the color to black",command=self.__change_colorbl).place(x=520,
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







    def draw_figure(self, last_x, last_y, data, figure):
        coordinates_tupla = self.__controller.handle_data(data)
        x = coordinates_tupla[0]
        y = coordinates_tupla[1]
        if figure == "lines":
            if abs(x - int(last_x)) > 5 or abs(y - int(last_y)) > 5:
                self.__canvas.create_line(last_x, last_y, x, y, fill=self.Constants.color_line,width=self.Constants.width_line)
                return coordinates_tupla
        else:
            self.__canvas.create_oval(x - self.Constants.radio, y - self.Constants.radio, x + self.Constants.radio,
                                      y + self.Constants.radio, fill="red")
            return None

    def __change_colorg(self):
        self.Constants.color_line = "green"

    def __change_colorr(self):
        self.Constants.color_line = "red"

    def __change_colorb(self):
        self.Constants.color_line = "blue"

    def __change_colorbl(self):
        self.Constants.color_line = "black"
