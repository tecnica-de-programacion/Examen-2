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
        position_black_button = N + W
        position_red_button = N + E
        position_green_button = W
        position_blue_button = E
        center = N + S + E + W
        color_text = "Colors:"
        black = "black"
        red = "red"
        green = "green"
        blue = "blue"
        color_bg = "#DA5D16"


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
        self.__black_button.grid(row = 1, column = 0, sticky = self.Constants.position_black_button )

        self.__red_button = Button(self, bg = self.Constants.red, width = self.Constants.width_button, height = self.Constants.height_button)
        self.__red_button.grid(row=1, column=0, sticky = self.Constants.position_red_button)

        self.__green_button = Button(self, bg = self.Constants.green, width = self.Constants.width_button, height = self.Constants.height_button)
        self.__green_button.grid(row=1, column=0, sticky = self.Constants.position_green_button)

        self.__blue_button = Button(self, bg = self.Constants.blue, width = self.Constants.width_button, height = self.Constants.height_button)
        self.__blue_button.grid(row=1, column=0, sticky = self.Constants.position_blue_button)

        self.__label = Label(self, text = self.Constants.color_text, bg = self.Constants.color_bg)
        self.__label.grid(row = 0,  column = 0)

