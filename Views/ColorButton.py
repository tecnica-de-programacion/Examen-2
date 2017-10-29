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

    def position(self, row, column):
        self.grid(row = row, column = column, sticky = self.Constants.center)
