from tkinter import Tk, N, S, E, W
from Views.TitleLabel import TitleLabel

class MainView(Tk):

    class Constants:
        title = "Pizarra Magica"
        window_height = 725
        window_width = 700
        board_height = 500
        board_width = 600
        border = 25
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.window_width, cls.window_height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg = "red")

        self.__configure_ui()
        self.__configure_grid()

    def __configure_ui(self):
        self.__title_label = TitleLabel(self)
        self.__title_label.position(0, 0)


    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize = TitleLabel.Constants.size)

        self.grid_rowconfigure(1, minsize = self.Constants.border)

        self.grid_rowconfigure(2, minsize = self.Constants.board_height)

        self.grid_rowconfigure(3, minsize = self.Constants.window_height - self.Constants.board_height - self.Constants.border)

        for column_index in range(4):
            self.grid_columnconfigure(column_index, minsize = self.Constants.window_width / 4)
