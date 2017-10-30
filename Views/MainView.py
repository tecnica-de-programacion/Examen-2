from tkinter import Tk, N, S, E, W, Label, Canvas, Button, StringVar, Menu

class MainView(Tk):

    class Constants:
        title = 'Pizarra mágica'
        width = 750
        height = 600
        effective_area_w = 600
        effective_area_h = 500
        c_red = '#FF0000'
        c_blue = '#0000FF'
        c_yellow = '#FFFF00'
        c_green = '#00FF00'
        c_black = '#040404'
        c_white = '#FDFEFE'
        c_window = '#155287'
        c_draw = '#9BECFA'
        space_x = 100
        space_y = 50
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
        self.color = self.Constants.c_black


        self.__draw_screen = Canvas(self, bg=self.Constants.c_draw, width=self.Constants.effective_area_w, height=self.Constants.effective_area_h)
        self.__draw_screen.place(x=self.Constants.space_x, y=self.Constants.space_y)

        self.__barra_Menu = Menu(self)
        self.__menu_Color = Menu(master=self.__barra_Menu)

        self.__menu_Color.add_command(label='Rojo', command=self.red)
        self.__menu_Color.add_command(label='Azul', command=self.blue)
        self.__menu_Color.add_command(label='Amarillo', command=self.yellow)
        self.__menu_Color.add_command(label='Verde', command=self.green)
        self.__menu_Color.add_separator()
        self.__menu_Color.add_command(label='Negro', command=self.black)
        self.__menu_Color.add_command(label='Blanco', command=self.white)

        self.__barra_Menu.add_cascade(label='Color', menu=self.__menu_Color)
        self.config(menu=self.__barra_Menu)


    def red(self):
        self.color = self.Constants.c_red
        print(self.color)
    def blue(self):
        self.color = self.Constants.c_blue
        print(self.color)
    def yellow(self):
        self.color = self.Constants.c_yellow
        print(self.color)
    def green(self):
        self.color = self.Constants.c_green
        print(self.color)
    def black(self):
        self.color = self.Constants.c_black
        print(self.color)
    def white(self):
        self.color = self.Constants.c_white
        print(self.color)




















