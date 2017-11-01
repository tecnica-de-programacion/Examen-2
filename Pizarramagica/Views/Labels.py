from tkinter import Label

class BackGround(Label):

    class Constants:
        width = 900

    def __init__ (self, master, x, y,width, image):
        self.__label = Label(master, image = image, width=width)
        self.__label.place(x = x, y = y)
