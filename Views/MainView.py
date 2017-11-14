from tkinter import Tk, Canvas, N, S, E, W,TOP, RIGHT,LEFT, Button, Label

class MainView(Tk):
    class Constants:
        title = " ¡ PIZARRA MAGICA ! "
        width = 900
        height = 600
        width_canvas = 600
        height_canvas = 500
        center = N + S + E + W
        window_color = "gray"
        canvas_color = "white"
        x_position = 0
        y_position = 500
        x_new = 0
        y_new = 500
        color_default = "black"

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)


    def __init__(self):
        super().__init__()

        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg = self.Constants.window_color)
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.maxsize(width=self.Constants.width, height=self.Constants.height)

        #coloca el pizarron
        self.space_drawing(self.Constants.width_canvas, self.Constants.height_canvas)
        #borrador
        self.bind('<space>', self.__erase)

        #BOTONES
        self.__bottom_space = Label(self, text=" CLEAN THE CANVAS WITH SPACE BUTTON ;)", bg="beige")
        self.__bottom_space.config(font=("Comic Sans MS", 20))
        self.__bottom_space.pack()

        self.__black_pencil = Button(self, text="Black", bg="black", fg="white", command=self.black, font=("Comic Sans MS", 20))
        self.__black_pencil.pack(side = RIGHT)

        self.__red_pencil = Button(self, text="Red", bg="red", fg="white", command=self.red, font=("Comic Sans MS", 20))
        self.__green_pencil = Button(self, text="Green", fg="white", bg="green", command=self.green, font=("Comic Sans MS", 20))
        self.__blue_pencil = Button(self, text="Blue", bg="blue", fg="white", command=self.blue, font=("Comic Sans MS", 20))

        self.__red_pencil.pack(side =RIGHT )
        self.__blue_pencil.pack(side = LEFT)
        self.__green_pencil.pack(side = LEFT)

    def space_drawing(self,width,height):
        self.__board = Canvas(self, width=width, height=height, bg=self.Constants.canvas_color)
        self.__board.pack(side=TOP)

    def set_pencil(self, horizontal, vertical):
        self.__line = self.__board.create_line(self.Constants.x_new, self.Constants.y_new, horizontal, self.Constants.y_position- vertical, fill=self.Constants.color_default)
        self.Constants.x_new = horizontal
        self.Constants.y_new = self.Constants.y_position - vertical

    def __erase(self, event):
        self.__board.delete("all")

    def black(self):
        self.Constants.color_default = "black"

    def red(self):
        self.Constants.color_default = "red"

    def green(self):
        self.Constants.color_default = "green"

    def blue(self):
        self.Constants.color_default = "blue"

