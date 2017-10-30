from tkinter import Tk, Canvas, Button, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigth = 650
        width = 1000
        center = N + S + E + W
        before_x = 0
        before_y = 0
        color = "black"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    class Events:
        space = '<space>'

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(self.Constants.width, self.Constants.heigth)
        self.minsize(self.Constants.width, self.Constants.heigth)
        self.__build_buttons()
        self.__canvas = Canvas(self, width=self.Constants.width, height=self.Constants.heigth)
        self.__canvas.grid(row=0, column=1, sticky=self.Constants.center)
        self.__draw_window = self.__canvas.create_rectangle(200, 20, 800, 520, fill="silver")
        self.bind(self.Events.space, self.__erase_all)

    def __build_buttons(self):
        self.__description_label = Label(self, text="Botones para cambiar el color del cursor", bg="DodgerBlue")
        self.__red_button = Button(self, text="Rojo", command=self.__change_color("red"), bg="red")
        self.__black_button = Button(self, text="Negro", command=self.__change_color("black"), bg="DimGray")
        self.__green_button = Button(self, text="Verde", command=self.__change_color("green"), bg="green")
        self.__blue_button = Button(self, text="Azul", command=self.__change_color("blue"), bg="blue")
        self.__description_bar_label = Label(self, text="Oprima espacio para borrar todo", bg="DarkRed")

        self.__description_label.grid(row=5, column=0, sticky=self.Constants.center)
        self.__red_button.grid(row=1, column=0, sticky=self.Constants.center)
        self.__black_button.grid(row=2, column=0, sticky=self.Constants.center)
        self.__green_button.grid(row=3, column=0, sticky=self.Constants.center)
        self.__blue_button.grid(row=4, column=0, sticky=self.Constants.center)
        self.__description_bar_label.grid(row=6, column=0, sticky=self.Constants.center)

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=0)

    def update_line(self, value_x, value_y):
        if self.Constants.before_x == 0:
            self.__positions(value_x, value_y)

        if value_x < self.Constants.before_x:
            self.update_line_x(self.Constants.before_x, value_y, value_x, value_y)
        elif value_x > self.Constants.before_x:
            self.update_line_x(value_x, value_y, self.Constants.before_x, value_y)

        if value_y < self.Constants.before_y:
            self.update_line_y(value_x, value_y, value_x, self.Constants.before_y)
        elif value_y > self.Constants.before_y:
            self.update_line_y(value_x, self.Constants.before_y, value_x, value_y)

        self.__positions(value_x, value_y)

    def __positions(self, value_x, value_y):
        self.Constants.before_x = value_x
        self.Constants.before_y = value_y

    def update_line_x(self, x1, y1, x2, y2):
        self.__line_x = self.__canvas.create_line(x1,y1,x2,y2, fill=self.Constants.color)

    def update_line_y(self, x1, y1, x2, y2):
        self.__line_y = self.__canvas.create_line(x1,y1,x2,y2, fill=self.Constants.color)

    def __erase_all(self, event):
        self.__canvas.delete("all")
        self.__draw_window = self.__canvas.create_rectangle(200, 20, 800, 520, fill="silver")

    def __change_color(self, color):
        self.Constants.color = color