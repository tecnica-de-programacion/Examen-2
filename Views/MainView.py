from tkinter import Tk, Canvas, PhotoImage, Label, Button, N, S, E, W
from Views.PokemonButton import PokemonButton
from Models.PositionManager import PositionManager


class MainView(Tk):
    class Constants:
        title = "Board"
        canvas_height = 500
        canvas_width = 600
        canvas_color = "grey"
        height = 619
        width = 725
        pokemon_width = 125
        center = N + S + E + W
        color = "black"
        black_file = "Assets/black.ppm"
        blue_file = "Assets/blue.ppm"
        green_file = "Assets/green.ppm"
        red_file = "Assets/red.ppm"
        title_file = "Assets/pokecap.ppm"
        color_event = "<Button-1>"

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.width,cls.height)

    def __init__(self):
        super().__init__()
        self.__position = PositionManager()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.maxsize(width=self.Constants.width, height=self.Constants.height)
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_grid(self):
        for row in range(0, 5):
            self.grid_rowconfigure(row, weight=True)
        self.grid_columnconfigure(0, weight=True, minsize=self.Constants.canvas_width)
        self.grid_columnconfigure(1, weight=True, minsize=self.Constants.pokemon_width)

    def __configure_UI(self):
        self.__canvas = Canvas(self, width=self.Constants.canvas_width, height=self.Constants.canvas_height)
        self.__canvas.grid(row=1, column=0, rowspan=500, sticky=self.Constants.center)
        self.__canvas.create_rectangle(0, 0, 600, 500, fill=self.Constants.canvas_color)

        self.__title_image = PhotoImage(file=self.Constants.title_file)
        self.__title_label = Label(image=self.__title_image)
        self.__title_label.grid(row=0, column=0, columnspan=775, sticky=self.Constants.center)

        self.__black_button = PokemonButton(self, self.Constants.black_file, "black", 1, 1, tap_color_handler=self.change_color)
        self.__blue_button = PokemonButton(self, self.Constants.blue_file, "blue", 1, 2, tap_color_handler=self.change_color)
        self.__green_button = PokemonButton(self, self.Constants.green_file, "green", 1, 3, tap_color_handler=self.change_color)
        self.__red_button = PokemonButton(self, self.Constants.red_file, "red", 1, 4, tap_color_handler=self.change_color)

    def update_line(self, second_x, second_y):
        first_x = self.__position.get_position_x()
        first_y = self.__position.get_position_y()
        old_cords = [(first_x, first_y)]
        new_cords = [(second_x, second_y)]
        self.__canvas.create_line(old_cords, new_cords, fill=self.Constants.color)
        self.__position.set_position(second_x, second_y)

    def clear_window(self):
        self.__canvas.create_rectangle(0, 0, 600, 500, fill=self.Constants.canvas_color)

    def change_color(self, new_color):
        self.Constants.color = new_color




