from tkinter import Tk, Canvas, Label, N, S, E, W, Frame, Button
from Models.Brain import Brain


class MainView(Tk):
    class Constants:
        title = "Pizarra Mágica"
        width = 520
        height = 630
        height_pizarra = 600
        width_pizarra = 500
        position = 601
        center = N + S + E + W
        distance = 150
        color_line = 'Black'


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__frame = Frame(self)
        self.__frame.grid(column = 0, row = 0)

        self.configure(background = 'dark blue')

        self.__controller = Brain()
        self.maxsize(self.Constants.width,self.Constants.height)
        self.minsize(self.Constants.width, self.Constants.height)
        self.__canvas = Canvas(self.__frame, width = self.Constants.width_pizarra, height = self.Constants.height_pizarra)
        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__canvas.create_rectangle(0, 0, self.Constants.width_pizarra, self.Constants.height_pizarra, fill = 'white')
        self.__label = Label(self.__frame, text = 'COLORES')

        self.__label.grid(row=5, column=0, sticky = N + W)
        self.grid_rowconfigure(0, weight = True)
        self.grid_columnconfigure(0, weight = True)


        self.__frame.bind("<space>", self.did_space_tap)
        self.__frame.focus_set()
        self.__frame.pack()

        self.button_green = Button(self, text="Green", font = ('Century Gothic',7),bg = 'green', command = self.__green_color).place(x=self.Constants.distance,y=self.Constants.position)
        self.Constants.distance += 50
        self.button_red = Button(self, text="   Red  ", font = ('Century Gothic',7),bg = 'red' , command = self.__red_color).place(x=self.Constants.distance,y=self.Constants.position)
        self.Constants.distance += 50
        self.button_blue = Button(self, text="  Blue  ", font = ('Century Gothic',7),bg= 'blue' , command = self.__blue_color).place(x=self.Constants.distance,y=self.Constants.position)
        self.Constants.distance += 50
        self.button_black = Button(self, text="Black", font = ('Century Gothic',7),bg = 'black', command = self.__dark_color).place(x=self.Constants.distance,y=self.Constants.position)

    def did_space_tap(self, event):
        #print("pressed")
        self.__canvas.destroy()
        self.__canvas = Canvas(self.__frame, width=self.Constants.width_pizarra, height=self.Constants.height_pizarra)
        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__canvas.create_rectangle(0, 0, self.Constants.width_pizarra, self.Constants.height_pizarra, fill='white')


    def draw_line (self, initial_x, initial_y, data):
        vector = self.__controller.handle_data(data)
        self.__canvas.create_line(initial_x, initial_y, vector[0], vector[1], fill = self.Constants.color_line, width = 2)
        return vector

    def __blue_color(self):
        #print('blue')
        self.Constants.color_line = "blue"

    def __dark_color(self):
        #print('dark')
        self.Constants.color_line = "black"

    def __green_color(self):
        #print('green')
        self.Constants.color_line = "green"

    def __red_color(self):
        #print('red')
        self.Constants.color_line = "red"


