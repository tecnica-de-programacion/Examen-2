from tkinter import *


class MainView(Tk):
    class Constants:
        title = "Alfonso Vega Garza"
        height = 650
        width = 900
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.color = "black"

        self.x = 300
        self.y = 250
        self.cx = 300
        self.cy = 250

        self.__top_text = Label(self, text = "Magic Board by Vega", bg = "#666699")
        self.__top_text.config(font = ("Comic Sans MS", 44))
        self.__bottom_text = Label(self, text = "To erase use your space bar", bg ="#666699")
        self.__bottom_text.config(font = ("Comic Sans MS", 20))
        self.__screen = Canvas(self, width = 600, height = 500, bg = "gray")
        self.__black_line = Button(self, text = "Black",bg = "black", fg = "white", command = self.black, font = ("Comic Sans MS", 20))
        self.__red_line = Button(self, text="Red", bg="red", fg = "white",command = self.red, font = ("Comic Sans MS", 20))
        self.__green_line = Button(self, text="Green", fg="white", bg ="green",command = self.green, font = ("Comic Sans MS", 20))
        self.__blue_line = Button(self, text="Blue", bg="blue",fg = "white", command = self.blue,font = ("Comic Sans MS", 20))

        self.__top_text.grid(row = 0, columnspan = 3, sticky = self.Constants.center)
        self.__black_line.grid(row = 1, column = 0, sticky = self.Constants.center)
        self.__red_line.grid(row = 2, column = 0, sticky = self.Constants.center)
        self.__screen.grid(row=1, column = 1, rowspan = 2)
        self.__blue_line.grid(row=1, column=2, sticky=self.Constants.center)
        self.__green_line.grid(row=2, column=2, sticky=self.Constants.center)
        self.__bottom_text.grid(row=3, columnspan=3, sticky=self.Constants.center)

        self.bind("<space>",self.erase)

        for v in range(0,3):
            self.rowconfigure(v, weight=True)
            self.columnconfigure(v,weight = True)

    def black(self):
        self.color = "black"

    def red(self):
        self.color = "red"

    def green(self):
        self.color = "green"

    def blue(self):
        self.color = "blue"

    def erase(self, event):
        self.__screen.delete(self,"all")
        self.x = 300
        self.y = 250

    def draw_line(self, x ,y):
        line_width = 1.8
        new_x = x * 600 / 1023
        new_y = y * 500 / 1023
        para_x = 300 - new_x
        para_y = 250 - new_y
        print(self.x - para_x,self.y - para_y)

        if abs(self.x - para_x) >= self.cx - 20 or abs(self.y - para_y) >= self.cy - 20 :
            self.__screen.create_line(self.x, self.y, self.cx + para_x, self.cy - para_y, fill=self.color, width=line_width)
            self.x = self.cx + para_x
            self.y = self.cy - para_y



