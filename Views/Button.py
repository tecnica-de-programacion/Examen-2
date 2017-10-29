from tkinter import Button, PhotoImage, N, S, E, W

class ColorButton(Button):
    class Constants:
        Red = "Assets\Red.gif"
        Blue = "Assets\Blue.gif"
        Black = "Assets\Black.gif"
        Green = "Assets\Green.gif"
        event = "<Button-1>"
        center = N + S + W + E

    def __init__(self, master, key, action=None):
        super().__init__(master)
        self.__action = action
        self.__key = key
        self.configure_image()
        self.bind(self.Constants.event, self.configure_image())

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



