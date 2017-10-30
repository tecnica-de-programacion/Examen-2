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

    def __init__(self, master, key, action = None):
        super().__init__(master)
        self.__action = action
        self.key = key
        self.configure_image()
        self.color = None
        self.bind(self.Event.click, self.__did_tap)


    def configure_image(self):
        if self.key == "red":
            self.__image = PhotoImage(file = self.Constants.Red)
        elif self.key == "blue":
            self.__image = PhotoImage(file=self.Constants.Blue)
        elif self.key == "black":
            self.__image = PhotoImage(file=self.Constants.Black)
        elif self.key == "green":
            self.__image = PhotoImage(file=self.Constants.Green)
        self.configure(image= self.__image)

    def position(self, row, column):
        self.grid(row=row, column=column, sticky = self.Constants.center)

    def __did_tap(self, event):
        if self.__action is None: return
        self.__action(self.key)
