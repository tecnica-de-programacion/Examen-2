from tkinter import Button

class ButtonPrototype(Button):
    class Events:
        click = "<Button-1>"

    def __init__(self, master, button_name, button_color):
        super().__init__(master)
        self.__button_name = button_name
        self.__button_color = button_color

        self.configure(text = self.__button_name)
        self.bind(self.Events.click, self.__did_tap_button)

    def __did_tap_button(self):
        self.__color = __button_color
        print(self.__color)
        return self.__color

    def position(self, row, column):
        self.row = row
        self.column = column
        self.grid(row = self.row, column = self.column)