from tkinter import Tk, N, S, E, W
from Views.TitleLabel import TitleLabel
from Views.CanvasBoard import CanvasBoard

class MainView(Tk):

    class Constants:
        title = "Pizarra Magica"
        window_height = 725
        window_width = 700
        white_board_height = 500
        white_board_width = 600
        border = 25
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.window_width, cls.window_height)

    class Events:
        space_bar = "<space>"

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg = "#D80407")

        self.resizable(width = False, height = False)

        self.__configure_ui()
        self.__configure_grid()

        self.bind(self.Events.space_bar , self.clear_white_board)

    def __configure_ui(self):
        self.__title_label = TitleLabel(self)
        self.__title_label.position(0, 0)

        self.__white_board = CanvasBoard(self, self.Constants.white_board_height, self.Constants.white_board_width)


    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize = TitleLabel.Constants.size)
        self.grid_rowconfigure(1, minsize = self.Constants.border)
        self.grid_rowconfigure(2, minsize = self.Constants.white_board_height)
        self.grid_rowconfigure(3, minsize = self.Constants.window_height - self.Constants.white_board_height - self.Constants.border - TitleLabel.Constants.size)

        for column_index in range(4):
            self.grid_columnconfigure(column_index, minsize = self.Constants.window_width / 4)

    def new_line(self, coordinates):
        self.__white_board.create_line(coordinates)

    def clear_white_board(self, event):
        for past_action in self.__white_board.find_all():
            self.__white_board.delete(past_action)