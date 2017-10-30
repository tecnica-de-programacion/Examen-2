from tkinter import Canvas

class DrawBoard(Canvas):

    class Constants:
        width = 600
        heigth = 500

    def __init__(self, master, height, width):
        super().__init__(master)
        self.configure(height = height, width = width, bg = '#ffffff')
        self.grid(row = 1, column = 0, columnspan = 4)