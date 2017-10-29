from tkinter import Tk, Canvas, Label, N, S, E, W, Button
class MainView(Tk):
    class Constants:
        title = "PIZARRA MAGICA"
        heigth_outside = 700
        width_outside = 800
        center_main_window = N + S + E + W
        bar_offset = 300
        height_inside = 500
        width_inside = 600


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width_outside, cls.heigth_outside)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width_outside, self.Constants.heigth_outside)
        self.maxsize(self.Constants.width_outside,self.Constants.heigth_outside)

        self.lines = None

        self.label = Label(self)

        self.canvas = Canvas(self, width = self.Constants.width_inside,height =self.Constants.height_inside)
        self.label.grid(row = 0, column = 3, sticky = W)
        self.canvas.grid(row= 0, column = 0, sticky = self.Constants.center_main_window)
        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(1, weight=True)

        self.button_black = None
        self.button_green = None
        self.button_blue = None
        self.button_yellow= None
        self.color = self.create_buttons()
        self.create_main_window_drawing()

    def create_drawing(self, vertical, horizontal):
        if self.lines is not None:
            self.canvas.delete(self.lines)
        self.lines = self.canvas.create_line(300-horizontal, 300, 300-vertical,300, fill = self.color)
        self.position_y =  self.canvas.coords(self.lines)
        print(self.position_y)

    def create_main_window_drawing(self):
        self.canvas.create_rectangle(100,100,600,600, fill = "white")

    def create_buttons(self):
        self.button_black = self.canvas.create_rectangle((10,10,90,50) ,fill= "black")
        self.canvas.tag_bind(self.button_black, "<Button-1>", lambda x: self.setColor("black"))
        self.button_green = self.canvas.create_rectangle((110,10,190,50) ,fill= "green")
        self.canvas.tag_bind(self.button_green, "<Button-1>", lambda x: self.setColor("green"))
        self.button_blue = self.canvas.create_rectangle((210,10,290,50) ,fill= "blue")
        self.canvas.tag_bind(self.button_blue, "<Button-1>", lambda x: self.setColor("Blue"))
        self.button_yellow = self.canvas.create_rectangle((310,10,390,50) ,fill= "yellow")
        self.canvas.tag_bind(self.button_yellow, "<Button-1>", lambda x: self.setColor("yellow"))

    def setColor(self,newcolor):
        self.color = newcolor
        print(self.color)
        return self.color












'''
        print()
        self.rectangle_horizontal = None
        self.rectangle_vertical = None

        self.__canvas_vertical = Canvas(self, width = self.Constants.width / 2, height = self.Constants.heigth)
        self.__canvas_horizontal = Canvas(self, width = self.Constants.width_inside / 2, height = self.Constants.heigth_inside)

        self.__canvas_vertical.grid(row=0, column=0, sticky=self.Constants.center)
        self.__canvas_horizontal.grid(row=1, column=1, sticky=self.Constants.center)

        self.grid_rowconfigure(0, weight = True)
        self.grid_columnconfigure(1, weight = True, minsize = self.Constants.width / 2)

        self.grid_rowconfigure(1, weight = True)
        self.grid_columnconfigure(1, weight=True, minsize=self.Constants.width / 2)

        self.funtion_rectangule_horizontal(0)
        self.funtion_rectangule_vertical(0)


    def funtion_rectangule_horizontal(self, value):
        if self.rectangle_horizontal is not None:
            self.__canvas.delete(self.rectangle_horizontal)
        self.rectangle_horizontal = self.__canvas_horizontal.create_rectangle(self.Constants.bar_offset, self.Constants.heigth - value, self.Constants.width / 2, self.Constants.heigth, fill="red")

    def funtion_rectangule_vertical(self, value):
        if self.rectangle_vertical is not None:
            self.__canvas.delete(self.rectangle_vertical)
        self.rectangle_vertical = self.__canvas_vertical.create_rectangle(self.Constants.bar_offset, self.Constants.heigth - value, self.Constants.width / 2, self.Constants.heigth, fill="blue")

'''
