from tkinter import Tk, Canvas, N, S, E, W,TOP

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
        font = ("Comicsand",14)
        x_position = 0
        y_position = 500
        x_new = 0
        y_new = 500
        color = "black"

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


    def space_drawing(self,width,height):
        self.__board = Canvas(self, width=width, height=height, bg=self.Constants.canvas_color)
        self.__board.pack(side=TOP)

    def set_pencil(self, horizontal, vertical):
        self.__line = self.__board.create_line(self.Constants.x_new, self.Constants.y_new, horizontal, self.Constants.y_position- vertical, fill=self.Constants.color)
        self.Constants.x_new = horizontal
        self.Constants.y_new = self.Constants.y_position - vertical

