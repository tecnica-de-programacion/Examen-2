from tkinter import Tk, Canvas, Label, N, S, E, W
class MainView(Tk):
    class Constants:
        title = "PIZARRA MAGICA"
        heigth_outside = 700
        width_outside = 800
        center_main_window = N + S + E + W
        bar_offset = 300
        height_inside = 500
        width_inside = 600
        width_button = 200

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
        self.canvas = Canvas(self, width = self.Constants.width_inside,height =self.Constants.height_inside)
        self.canvas.grid(row= 0, column = 0, sticky = N+S+E+W)
        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(1, weight=True)
        self.position_x = 0
        self.position_y = 0
        self.create_main_window_drawing()


    def create_drawing(self, vertical, horizontal):
        if self.lines is not None:
            self.canvas.delete(self.lines)
        self.lines = self.canvas.create_line(300-horizontal, 300, 300-vertical,300)
        self.position_y =  self.canvas.coords(self.lines)
        print(self.position_y)
    def create_main_window_drawing(self):
        self.canvas.create_rectangle(100,100,700,600,fill = "red")













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
