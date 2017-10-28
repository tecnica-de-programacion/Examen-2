from tkinter import Tk, Label, Canvas, Button, N, S, E, W

class MainView(Tk):
    class Constants():
        title = "Pizarra Mágica"
        height = 600
        width = 800
        height_sketch = 500
        width_sketch = 600
        width_button = 5
        height_button = 2
        position_black_button = 200
        position_red_button = 300
        position_green_button = 400
        position_blue_button = 500
        center = N + S + E + W
        text_label = "Colores:"
        color_label = "#CA9494"
        black = "black"
        red = "red"
        green = "green"
        blue = "blue"
        color_bg = "#A90000"
        x_start = 0
        y_start = 500
        new_x_start = 0
        new_y_start = 500
        event = "<Button-1>"
        new_color = "black"


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)


    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(self.Constants.width, self.Constants.height)
        self.minsize(self.Constants.width, self.Constants.height)
        self.config(bg = self.Constants.color_bg)

        self.__canvas = Canvas(self, width = self.Constants.width_sketch, height = self.Constants.height_sketch)

        self.__canvas.grid(column=0)
        self.__canvas.grid(column=2)
        self.__canvas.grid(row = 1, column = 1, sticky = self.Constants.center)

        self.columnconfigure(0, minsize = int((self.Constants.width - self.Constants.width_sketch)/2))
        self.columnconfigure(1, minsize= self.Constants.width_sketch)
        self.columnconfigure(2, minsize= int((self.Constants.width - self.Constants.width_sketch)/2))

        self.rowconfigure(0, minsize=int((self.Constants.height - self.Constants.height_sketch) / 2))
        self.rowconfigure(1, minsize=self.Constants.height_sketch)
        self.rowconfigure(2, minsize=int((self.Constants.height - self.Constants.height_sketch) / 2))

        self.__black_button = Button(self, bg = self.Constants.black, width = self.Constants.width_button, height = self.Constants.height_button)
        self.__black_button.place(x = self.Constants.position_black_button)
        self.__black_button.bind(self.Constants.event, self.__get_black_color)

        self.__red_button = Button(self, bg = self.Constants.red, width = self.Constants.width_button, height = self.Constants.height_button)
        self.__red_button.place(x = self.Constants.position_red_button)
        self.__red_button.bind(self.Constants.event, self.__get_red_color)

        self.__green_button = Button(self, bg = self.Constants.green, width = self.Constants.width_button, height = self.Constants.height_button)
        self.__green_button.place(x = self.Constants.position_green_button)
        self.__green_button.bind(self.Constants.event, self.__get_green_color)

        self.__blue_button = Button(self, bg = self.Constants.blue, width = self.Constants.width_button, height = self.Constants.height_button)
        self.__blue_button.place(x = self.Constants.position_blue_button)
        self.__blue_button.bind(self.Constants.event, self.__get_blue_color)

        self.__label = Label(self, text = self.Constants.text_label, bg = self.Constants.color_label)
        self.__label.grid(row = 0,  column = 0)

    def __get_black_color(self, event):
        self.Constants.new_color = self.Constants.black
        self.update_line

    def __get_red_color(self, event):
        self.Constants.new_color = self.Constants.red
        self.update_line

    def __get_green_color(self, event):
        self.Constants.new_color = self.Constants.green
        self.update_line

    def __get_blue_color(self, event):
        self.Constants.new_color = self.Constants.blue
        self.update_line

    def update_line(self, horizontal, vertical):
        #print(horizontal, vertical)
        self.__canvas.create_line(self.Constants.new_x_start, self.Constants.new_y_start, horizontal, self.Constants.y_start - vertical, fill = self.Constants.new_color)
        self.Constants.new_x_start = horizontal
        self.Constants.new_y_start = self.Constants.y_start - vertical

