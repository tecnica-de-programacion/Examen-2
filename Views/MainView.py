from tkinter import Tk, N, S, E, W

class MainView(Tk):

    class Constants:
        title = 'Pizarra mágica'
        width = 900
        height = 650
        c_red = '#FF0000'
        c_blue = '#0000FF'
        c_yellow = '#FFFF00'
        c_green = '#00FF00'
        c_window = '#155287'
        c_draw = '#D2FBDF'
        center = N + S + E + W

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)


    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.config(bg = self.Constants.c_window)

