from tkinter import Button

class ButtonPrototype(Button):
    class Events:
        click = "<Button-1>"

    def __init__(self, master, button_name, button_color, action = None):
        super().__init__(master)
        self.__button_name = button_name
        self.color = button_color
        self.__action = action

        self.configure(text = self.__button_name)
        self.bind(self.Events.click, self.__did_tap_button)

    def __did_tap_button(self, event):
        if self.__action is None: return
        self.__action(self.color)

    def position(self, row, column):
        self.row = row
        self.column = column
        self.grid(row = self.row, column = self.column)