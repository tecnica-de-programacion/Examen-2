from tkinter import Button, PhotoImage


class PokemonButton():

    def __init__(self, master, photo_file, color, column, row, tap_color_handler=None):
        self.__master = master
        self.__tap_handler = tap_color_handler
        self.__photo_file = photo_file
        self.__color = color
        self.__column = column
        self.__row = row

        self.__image = PhotoImage(file=self.__photo_file)
        self.__button = Button(self.__master, image=self.__image)
        self.__button.grid(row=self.__row, column=self.__column)
        self.__button.bind("<Button-1>", self.__did_tap_change)

    def __did_tap_change(self, event):
        self.__tap_handler(self.__color)
