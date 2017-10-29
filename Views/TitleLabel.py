from tkinter import Label, N, S, E, W

class TitleLabel(Label):
    class Constants:
        size = 80
        border_type = 'flat'
        border_width = 1
        font_family = "Quicksand"
        font_size = 68
        bg = '#D80407'
        foreground = '#FFFFFF'
        center = W + E + N + S
        rigth = E
        span = 4

    def __init__(self, master):
        super().__init__(master)
        self.configure(text = "Magic Board")
        self.configure(bg = self.Constants.bg)
        self.configure(foreground = self.Constants.foreground)
        self.configure(font = (self.Constants.font_family, self.Constants.font_size))

    def position(self, row, column):
        self.grid(row = row, column = column, sticky = self.Constants.center, columnspan = self.Constants.span)

    def text(self, text):
        self.configure(text = text)