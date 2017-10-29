from tkinter import Label, PhotoImage


class ColorButton():
    def __init__(self, master, column, color, file_path, action=None):
        self.__master = master
        self.__color = color
        self.__file_path = file_path
        self.action = action
        self.__column = column

        self.__image = PhotoImage(file=file_path)
        self.__button = Label(self.__master, image=self.__image)
        self.__button.grid(row=0, column=self.__column)
        self.__button.bind("<Button-1>", self.__tap_handler)

    def __tap_handler(self, event):
        print('Color button pressed:', self.__color)



