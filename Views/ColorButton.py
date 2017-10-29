from tkinter import Label, N, S, E, W

class ColorButton(Label):
    class Constants:
        font_family = "Quicksand"
        font_size = 20
        foreground = '#FFFFFF'
        center = N + S + W + E

    class Events:
        click = "<Button-1>"

    def __init__(self, master, text, color):
        super().__init__(master)
        self.configure(text = text)
        self.configure(bg = color)
        self.configure(foreground = self.Constants.foreground)
        self.configure(font = (self.Constants.font_family, self.Constants.font_size))

        #self.bind(self.Events.click, self.__color_clicked)

    def position(self, row, column, columnspan = 1):
        self.grid(row = row, column = column, columnspan = columnspan, sticky = self.Constants.center)
