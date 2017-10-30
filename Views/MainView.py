from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigth = 650
        width = 1000
        center = N + S + E + W
        bar_offset = 2
        before_x = 0
        before_y = 0

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(self.Constants.width, self.Constants.heigth)
        self.minsize(self.Constants.width, self.Constants.heigth)
        self.__canvas = Canvas(self, width=self.Constants.width, height=self.Constants.heigth)
        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__draw_window = self.__canvas.create_rectangle(200, 20, 800, 520, fill="silver")

    def update_line(self, value_x, value_y):
        if self.Constants.before_x == 0:
            self.__positions(value_x, value_y)

        if value_x < self.Constants.before_x:
            self.update_line_x(self.Constants.before_x, value_y, value_x, value_y+self.Constants.bar_offset)
        elif value_x > self.Constants.before_x:
            self.update_line_x(value_x, value_y, self.Constants.before_x, value_y+self.Constants.bar_offset)

        if value_y < self.Constants.before_y:
            self.update_line_y(value_x, value_y, value_x+self.Constants.bar_offset, self.Constants.before_y)
        elif value_y > self.Constants.before_y:
            self.update_line_y(value_x, self.Constants.before_y, value_x+self.Constants.bar_offset, value_y)

        self.__positions(value_x, value_y)

    def __positions(self, value_x, value_y):
        self.Constants.before_x = value_x
        self.Constants.before_y = value_y

    def update_line_x(self, x1, y1, x2, y2):
        self.__line_x = self.__canvas.create_rectangle(x1,y1,x2,y2, fill="red")

    def update_line_y(self, x1, y1, x2, y2):
        self.__line_y = self.__canvas.create_rectangle(x1,y1,x2,y2, fill="red")

