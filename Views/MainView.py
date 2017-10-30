from tkinter import Tk, Canvas, Label, N, S, E, W, Button

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
        font_size = 30
        value_x = 0
        value_y = 500
        first_y = 600
        color = 'Black'
        event= "<Button-1>"
        event_delete = "<space>"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.screen_width, cls.screen_heigth)



    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__lines = True
        self.__canvas = Canvas(self, width = self.Constants.width , height=self.Constants.heigth)
        self.__green = Button(self, text = "Green",bg = '#00ff00', font =self.Constants.font_family  )
        self.__blue = Button(self, text="Blue", bg = '#0000ff', font=self.Constants.font_family)
        self.__red = Button(self, text="Red", bg = '#df0101', font=self.Constants.font_family, )
        self.__black = Button(self, text="Black", bg='#202020', font=self.Constants.font_family )


        self.__canvas.grid(row=2, column=0, sticky=self.Constants.center)
        self.__green.grid(row = 2, column = 1, sticky = self.Constants.center)
        self.__blue.grid(row=2, column=2, sticky= self.Constants.center)
        self.__red.grid(row=2, column=3, sticky=self.Constants.center)
        self.__black.grid(row = 2, column = 4, sticky = self.Constants.center)


        self.grid_columnconfigure(0, weight=True,minsize = self.Constants.width )
        self.grid_columnconfigure(1, weight=True, minsize = self.Constants.width / 4 )
        self.grid_columnconfigure(2, weight=True,minsize = self.Constants.width /4)
        self.grid_columnconfigure(3, weight=True, minsize=self.Constants.width / 4)
        self.grid_columnconfigure(4, weight=True, minsize=self.Constants.width / 4)


        self.__green.configure(font = (self.Constants.font_family, self.Constants.font_size), anchor = self.Constants.right)
        self.__blue.configure(font=(self.Constants.font_family, self.Constants.font_size), anchor=self.Constants.right)
        self.__red.configure(font=(self.Constants.font_family, self.Constants.font_size), anchor=self.Constants.right)
        self.__black.configure(font=(self.Constants.font_family, self.Constants.font_size), anchor=self.Constants.right)
        self.__black.configure(foreground = '#FFFFFF')


        self.__green.bind(self.Constants.event , self.__update_color_green)
        self.__blue.bind(self.Constants.event , self.__update_color_blue)
        self.__red.bind(self.Constants.event , self.__update_color_red)
        self.__black.bind(self.Constants.event, self.__update_color_black)
        self.bind(self.Constants.event_delete, self.__delete_draw)

    def __update_color_green(self, event):
            self.Constants.color = "#00ff00"


    def __update_color_blue(self, event):
        self.Constants.color = "#0000ff"


    def __update_color_red(self, event):
            self.Constants.color = "#df0101"

    def __update_color_black(self, event):
        self.Constants.color = "Black"


    def __delete_draw(self, event):
        self.__canvas.delete("all")


    def update_lines(self, axis_x, axis_y):

        self.__lines = self.__canvas.create_line(self.Constants.value_x, self.Constants.value_y, axis_x, self.Constants.first_y - axis_y, fill= self.Constants.color)
        self.Constants.value_x = axis_x
        self.Constants.value_y = self.Constants.first_y = axis_y

