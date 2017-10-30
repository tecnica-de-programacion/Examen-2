from tkinter import Button, PhotoImage, N, S, W, E

class ColorButton(Button):

    class Constants:
        center = N + S + E + W
        button_file = 'Assets\ButtonPicture.gif'

    class Events:
        click = "<Button-1>"

    def __init__(self, master, color, name, action = None):
        super().__init__(master)
        self.__color = color
        self.__name = name
        self.__action = action
        self.__canChange = True

        self.__button_image = PhotoImage(file = self.Constants.button_file)

        self.configure(image = self.__button_image)

        self.bind(self.Events.click, self.__change_color)

    def __change_color(self, event):
        if self.__action is None: return
        self.__action(self.__color)

    def position(self, row, column):
        self.grid(row = row, column = column)