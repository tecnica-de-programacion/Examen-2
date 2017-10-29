from tkinter import Button, PhotoImage, N, S, E, W

class ColorButton(Button):
    class Constants:
        Red = "Assets\Red.gif"
        Blue = "Assets\Blue.gif"
        Black = "Assets\Black.gif"
        Green = "Assets\Green.gif"
        center = N + S + W + E

    class Event:
        click = "<Button-1>"

    def __init__(self, master, key, action=None):
        super().__init__(master)
        self.__action = action
        self.__key = key
        self.configure_image()
        self.color = None
        self.bind(self.Event.click, self.change_color)


    def configure_image(self):
        if self.__key == "Red":
            self.__image = PhotoImage(file = self.Constants.Red)
        elif self.__key == "Blue":
            self.__image = PhotoImage(file=self.Constants.Blue)
        elif self.__key == "Black":
            self.__image = PhotoImage(file=self.Constants.Black)
        elif self.__key == "Green":
            self.__image = PhotoImage(file=self.Constants.Green)
        self.configure(image= self.__image)

    def position(self, row, column):
        self.grid(row=row, column=column, sticky = self.Constants.center)

    def change_color(self, event):
        if self.__key == "Red":
            self.color ='cambia RED'
        elif self.__key == "Blue":
            self.color = 'cambia BLUE'
        elif self.__key == "Black":
            self.color = 'cambia BLACK'
        elif self.__key == "Green":
            self.color = 'cambia GREEN'
        print(self.color)