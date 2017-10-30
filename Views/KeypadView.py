from Views.ColorButton import ColorButton

class KeypadView():

    def __init__(self, master):
        self.__color = '#000000'

        button_black = ColorButton(master, "#000000", "Black", action = self.__change_colors)
        button_red = ColorButton(master, "#ff0000", "Red", action=self.__change_colors)
        button_green = ColorButton(master, "#33cc33", "Green", action=self.__change_colors)
        button_blue = ColorButton(master, "#0000ff","Blue", action = self.__change_colors)

        button_black.position(2, 0)
        button_red.position(2, 1)
        button_green.position(2, 2)
        button_blue.position(2, 3)

    def __change_colors(self, color):
        self.__color = color

    @property
    def get_color(self):
        return self.__color