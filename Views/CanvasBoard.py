from tkinter import Canvas

class CanvasBoard(Canvas):

    def __init__(self, master, height, width):
        super().__init__(master)
        self.__height = height
        self.__width = width
        self.configure(height = self.__height, width = self.__width, bg = 'white')
        self.grid(row = 1, column = 0, columnspan = 4)