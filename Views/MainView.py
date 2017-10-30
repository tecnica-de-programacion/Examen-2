from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "PIZARRA MAGICA"
        heigth_outside = 700
        width_outside = 800
        center_main_window = N + S + E + W
        height_inside = 500
        width_inside = 600
        advance = 1
        width_line = 3
        color_1 = "Black"
        color_2= "Green"
        color_3 = "Red"
        color_4 = "Blue"
        color_5 = "Yellow"
        color_6 = "Purple"
        posicion_x_main = 100
        posicion_y_main = 600
        when_click = "<Button-1>"

        class Events:
            clean_window = "<space>"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width_outside, cls.heigth_outside)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width_outside, self.Constants.heigth_outside)
        self.maxsize(self.Constants.width_outside,self.Constants.heigth_outside)
        self.lines = None
        self.label = Label(self)
        self.close_drawing = None

        self.canvas = Canvas(self, width = self.Constants.width_inside, height = self.Constants.height_inside)
        self.label.grid(row = 0, column = 3, sticky = W)
        self.canvas.grid(row = 0, column = 0, sticky = self.Constants.center_main_window)
        self.grid_rowconfigure(0, weight = True)
        self.grid_columnconfigure(1, weight = True)

        self.position_x = self.Constants.posicion_x_main
        self.position_y = self.Constants.posicion_y_main

        self.button_black = None
        self.button_green = None
        self.button_blue = None
        self.button_red = None
        self.button_yellow = None
        self.button_purple = None

        self.color = self.create_buttons()
        self.create_main_window_drawing()
        self.bind(self.Constants.Events.clean_window, self.clean_window)

    def create_drawing(self, horizontal, vertical):
        if self.lines is not None:
            self.canvas.delete(self.lines)
        new_position_y = vertical - 300
        new_position_x = horizontal - 300
        print(new_position_x,new_position_y)

        if -300 <= new_position_x <= 0:
            self.canvas.create_line(self.position_x, self.position_y, self.position_x - self.Constants.advance, self.position_y, fill = self.color, width = self.Constants.width_line)
            self.position_x += self.Constants.advance

        if 0 <= new_position_x <= 300:
            self.canvas.create_line(self.position_x, self.position_y, self.position_x + self.Constants.advance, self.position_y, fill = self.color, width = self.Constants.width_line)
            self.position_x -= self.Constants.advance

        if -300 <= new_position_y <= 0:
            self.canvas.create_line(self.position_x, self.position_y, self.position_x, self.position_y - self.Constants.advance, fill = self.color, width = self.Constants.width_line)
            self.position_y += self.Constants.advance

        if  0 <= new_position_y <= 300:
            self.canvas.create_line(self.position_x, self.position_y, self.position_x, self.position_y + self.Constants.advance, fill = self.color, width = self.Constants.width_line)
            self.position_y -= self.Constants.advance

    def create_main_window_drawing(self):
        self.canvas.create_rectangle(100,100,600,600, fill = "white")

    def create_buttons(self):
        self.button_black = self.canvas.create_rectangle((10,10,90,50) ,fill = self.Constants.color_1)
        self.canvas.tag_bind(self.button_black, self.Constants.when_click, lambda x: self.setColor(self.Constants.color_1))
        self.button_green = self.canvas.create_rectangle((110,10,190,50) ,fill = self.Constants.color_2)
        self.canvas.tag_bind(self.button_green, self.Constants.when_click, lambda x: self.setColor(self.Constants.color_2))
        self.button_blue = self.canvas.create_rectangle((210,10,290,50) ,fill = self.Constants.color_4)
        self.canvas.tag_bind(self.button_blue, self.Constants.when_click, lambda x: self.setColor(self.Constants.color_4))
        self.button_red = self.canvas.create_rectangle((310,10,390,50) ,fill = self.Constants.color_3)
        self.canvas.tag_bind(self.button_red, self.Constants.when_click, lambda x: self.setColor(self.Constants.color_3))
        self.button_yellow = self.canvas.create_rectangle((410, 10, 490, 50), fill=self.Constants.color_5)
        self.canvas.tag_bind(self.button_yellow, self.Constants.when_click, lambda x: self.setColor(self.Constants.color_5))
        self.button_purple = self.canvas.create_rectangle((510, 10, 590, 50), fill=self.Constants.color_6)
        self.canvas.tag_bind(self.button_purple, self.Constants.when_click, lambda x: self.setColor(self.Constants.color_6))

    def setColor(self,newcolor):
        self.color = newcolor
        print(self.color)
        return self.color
    def clean_window(self, event):
        self.canvas.delete("all")
        self.create_main_window_drawing()
        self.create_buttons()


