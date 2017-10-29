from tkinter import Tk, Canvas, Button, Label

class ColorButton(Button):
    class Constants:
        width = 12
        height = 3

    def __init__(self, master, x, y, color, action = None):
        self.__button = Button(master, command = self.__did_button_tap)
        self.__color = color
        self.__button.configure(width = self.Constants.width, height = self.Constants.height, bg = color)
        self.__button.place(x= x, y= y)
        self.__action = action

    def __did_button_tap(self):
        if self.__action is None: return
        self.__action(self.__color)