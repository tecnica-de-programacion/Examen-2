from tkinter import LabelFrame
from Views.ColorButton import ColorButton
from Views.CustomColors import Colors

class ButtonsArea():
    def __init__(self, master, text, color_handler=None):
        self.__master = master
        self.__text = text
        self.__configure_buttons_area(color_handler)


    def __configure_buttons_area(self, color_handler):
        self.__label_area = LabelFrame(self.__master, text=self.__text)
        self.__label_area.grid(row=2, column=0)

        self.counter = 0
        for color in Colors.colors:
            ColorButton(self.__label_area, self.counter, color[0], color[1], color_handler)
            self.counter += 1

