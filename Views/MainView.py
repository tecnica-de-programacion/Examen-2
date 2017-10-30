from tkinter import Tk, N, S, E, W
from Views.DrawBoard import DrawBoard
from Views.KeypadView import KeypadView

class MainView(Tk):

    class Constants:
        title = 'Pizarra Magica'
        window_height = 625
        window_width = 700
        board_height = 500
        board_width = 600
        border = 25
        center = N + S + E + W

        @classmethod
        def size(cls):
            return '{}x{}'.format(cls.window_width, cls.window_height)

    class Events:
        space_bar = "<space>"

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg = '#ff0000')
        self.resizable(width = False, height = False)

        self.__configure_ui()
        self.__configure_grid()

        self.bind(self.Events.space_bar, self.__clear_board)

    def __configure_ui(self):
        self.__board = DrawBoard(self, self.Constants.board_height, self.Constants.board_width)
        self.__keypad = KeypadView(self)

    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize = self.Constants.border)

        self.grid_rowconfigure(1, minsize = self.Constants.board_height)

        self.grid_rowconfigure(2, minsize = self.Constants.window_height - self.Constants.board_height - self.Constants.border)

        for column_index in range(4):
            self.grid_columnconfigure(column_index, minsize = self.Constants.window_width / 4)
            
    def create_line(self, coordinate):
        self.__board.create_line(coordinate, fill = self.__keypad.get_color)

    def __clear_board(self, event):
        for i in self.__board.find_all():
            self.__board.delete(i)