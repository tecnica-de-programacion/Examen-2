from tkinter import Button

class ColorButton(Button):
    class Constants:
        width = 100
        height = 75
        bg = '#d29bd4'

    def __init__(self, master, x, y, color, image, action = None):
        self.__button = Button(master, command = self.__did_button_tap, image = image)
        self.__color = color
        self.__button.configure(width = self.Constants.width, height = self.Constants.height, bg = self.Constants.bg)
        self.__button.place(x= x, y= y)
        self.__action = action

    def __did_button_tap(self):
        if self.__action is None: return
        self.__action(self.__color)