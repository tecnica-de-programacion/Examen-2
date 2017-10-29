from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Pizarra Màgica"
        heigth = 600
        width = 500
        screen_heigth = 600
        screen_width = 1000
        button_heigth = 150
        button_width = 100
        center = N + S + E + W
        right = W
        bar_offset = 30
        font_family = 'Arial'
        font_size = 60

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.screen_width, cls.screen_heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__rectangle = None
        self.__lable = Label(self)
        self.__canvas = Canvas(self, width = self.Constants.width , height=self.Constants.heigth)
        self.__green = Label(self, width=self.Constants.button_width, height=self.Constants.button_heigth)
        self.__blue = Label(self)
        self.__red = Label(self)
        self.__black = Label(self)

        self.__canvas.grid(row=0, column=0, sticky=self.Constants.center)
        self.__lable.grid(row=0, column=1, sticky = self.Constants.center)
        self.__green.grid(row = 2, column = 3, sticky = self.Constants.center)
        self.__blue.grid(row=1, column=3, sticky= self.Constants.center)
        self.__red.grid(row=0, column=3, sticky=self.Constants.center)
        self.__black.grid(row = 3, column = 3, sticky = self.Constants.center)


        self.grid_columnconfigure(0, weight=True,minsize = self.Constants.width )
        self.grid_columnconfigure(1, weight=True, minsize = self.Constants.width /3)
        self.grid_columnconfigure(3, weight=True,minsize = self.Constants.width /3)

        self.grid_rowconfigure(0, weight=True, minsize=self.Constants.heigth / 4)
        self.grid_rowconfigure(1, weight = True, minsize = self.Constants.heigth / 4)
        self.grid_rowconfigure(2, weight = True, minsize = self.Constants.heigth / 4)
        self.grid_rowconfigure(3, weight=True, minsize=self.Constants.heigth / 4)

        self.__green.configure(text = "Green")
        self.__green.configure(bg = '#00ff00')
        self.__green.configure(font = (self.Constants.font_family, self.Constants.font_size), anchor = self.Constants.right)

        self.__blue.configure(text="Blue")
        self.__blue.configure(bg='#0000ff')
        self.__blue.configure(font=(self.Constants.font_family, self.Constants.font_size), anchor=self.Constants.right)

        self.__red.configure(text = 'Red')
        self.__red.configure(bg = '#df0101')
        self.__red.configure(font=(self.Constants.font_family, self.Constants.font_size), anchor=self.Constants.right)

        self.__black.configure(text='Black')
        self.__black.configure(bg='#202020')
        self.__black.configure(font=(self.Constants.font_family, self.Constants.font_size), anchor=self.Constants.right)
        self.__black.configure(foreground = '#FFFFFF')


    def update_bar(self, value):
        if self.__rectangle is not None:
            self.__canvas.delete(self.__rectangle)
        self.__rectangle = self.__canvas.create_line(self.Constants.bar_offset, self.Constants.heigth - value, self.Constants.width / 2,
                                                          self.Constants.heigth, fill="black")
\