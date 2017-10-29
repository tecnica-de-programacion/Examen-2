from tkinter import Tk, N, S, E, W, Label, Canvas, Button, StringVar, Menu

class MainView(Tk):

    class Constants:
        title = 'Pizarra mágica'
        width = 1100
        height = 750
        effective_area_h = 500
        effective_area_w = 600
        c_red = '#FF0000'
        c_blue = '#0000FF'
        c_yellow = '#FFFF00'
        c_green = '#00FF00'
        c_window = '#155287'
        c_draw = '#9BECFA'
        center = N + S + E + W

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width, cls.height)


    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.config(bg = self.Constants.c_window)
        self.minsize(self.Constants.width, self.Constants.height)
        self.maxsize(self.Constants.width, self.Constants.height)



        self.__draw_screen = Canvas(self, bg=self.Constants.c_draw, width=self.Constants.effective_area_w, height=self.Constants.effective_area_h)
        self.__draw_screen.grid(column = 3, row=2, sticky=self.Constants.center)


        for num in range(0,5):
            self.rowconfigure(num, weight=True)
            self.columnconfigure(num, weight=True)



















