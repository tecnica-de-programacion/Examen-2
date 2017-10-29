from tkinter import Canvas

class Cleaner(Canvas):
    class Events:
        eraser = "<Button-1>"

    def __init__(self, master, text, color):
        super().__init__(master)
        self.configure(text = text)
        self.configure(bg = color)
        self.configure(foreground = self.Constants.foreground)
        self.configure(font = (self.Constants.font_family, self.Constants.font_size))

    def position(self, row, column, columnspan = 1):
        self.grid(row = row, column = column, columnspan = columnspan, sticky = self.Constants.center)