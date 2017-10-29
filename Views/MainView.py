from tkinter import Tk, Button, N, S, E, W
from Views.TitleLabel import TitleLabel
from Views.CanvasBoard import CanvasBoard


class MainView(Tk):

    class Constants:
        title = "Pizarra Magica"
        window_height = 680
        window_width = 700
        white_board_height = 500
        white_board_width = 600
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.window_width, cls.window_height)

    class Events:
        space_bar = "<space>"
        click = "<Button-1>"

    def __init__(self):
        super().__init__()
        self.__color = "#FF0000"

        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg = "#D80407")

        self.resizable(width = False, height = False)

        self.__configure_ui()
        self.__configure_grid()

        self.bind(self.Events.space_bar , self.clear_white_board)

    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize = TitleLabel.Constants.size)
        self.grid_rowconfigure(1, minsize = self.Constants.white_board_height)
        self.grid_rowconfigure(2, minsize = self.Constants.window_height - self.Constants.white_board_height - 150)
        for column_index in range(4):
            self.grid_columnconfigure(column_index, minsize = self.Constants.window_width / 4)

    def __configure_ui(self):
        self.__title_label = TitleLabel(self)
        self.__title_label.position(0, 0)

        self.__white_board = CanvasBoard(self, self.Constants.white_board_height, self.Constants.white_board_width)
        #self.__keypad = KeypadView(self)

        self.__black_button = Button(self)
        self.__black_button.configure(text = "Black")
        self.__black_button.grid(row = 3, column = 0, sticky = self.Constants.center)
        self.__black_button.bind(self.Events.click, self.__did_tap_black_button)

        self.__red_button = Button(self)
        self.__red_button.configure(text = "Red")
        self.__red_button.grid(row = 3, column = 1, sticky = self.Constants.center)
        self.__red_button.bind(self.Events.click, self.__did_tap_red_button)


        self.__green_button = Button(self)
        self.__green_button.configure(text = "Green")
        self.__green_button.grid(row=3, column=2, sticky=self.Constants.center)
        self.__green_button.bind(self.Events.click, self.__did_tap_green_button)

        self.__blue_button = Button(self)
        self.__blue_button.configure(text = "Blue")
        self.__blue_button.grid(row=3, column=3, sticky=self.Constants.center)
        self.__blue_button.bind(self.Events.click, self.__did_tap_blue_button)

    def __did_tap_black_button(self, event):
        self.__color = "#000000"

    def __did_tap_red_button(self, event):
        self.__color = "#FF0000"

    def __did_tap_blue_button(self, event):
        self.__color = "#2980B9"

    def __did_tap_green_button(self, event):
        self.__color = "#138D75"

    def __get_color(self):
        return self.__color

    def new_line(self, coordinates):
        color = self.__get_color()
        self.__white_board.create_line(coordinates, fill = color)


    def clear_white_board(self, event):
        for past_action in self.__white_board.find_all():
            self.__white_board.delete(past_action)