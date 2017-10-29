from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = 'Pizarra mágica'
        drawing_screen_height = 500
        drawing_screen_width = 600
        width = 900
        height = 650
        left_width = 100
        center = N + S + E + W
        bg = '#8d3d31'
        event = '<space>'

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.height)
        self.maxsize(self.Constants.width, self.Constants.height)
        self.config(bg = self.Constants.bg)

        self.__label = Label(self)
        self.__canvas = Canvas(self, width = self.Constants.drawing_screen_width, height = self.Constants.drawing_screen_height)
        self.__canvas.place(x = self.Constants.left_width, y = (self.Constants.height - self.Constants.drawing_screen_height) / 2)


