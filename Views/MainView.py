from tkinter import Tk, Label, Canvas, N, S, E, W


class MainView(Tk):
    class Constants:
        title = "Pizarra Magica"
        height = 900
        width = 1000
        side_width = 200
        side_height = 200
        center = N + S + E + W
        border_color = 'salmon'
        magic_board_color = 'white'
        margin_size = 200

        @classmethod
        def size (cls):
            return '{}x{}'.format(cls.width,cls.height)

    def __init__(self):
        super().__init__()

        self.title('Pizarra Mágica')
        self.geometry(self.Constants.size())
        self.minsize(width=self.Constants.width, height=self.Constants.height)
        self.maxsize(width=self.Constants.width, height=self.Constants.height)

        self.configure(bg=self.Constants.border_color)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.__magic_board = Canvas(self, width=600, height=500, bg=self.Constants.magic_board_color)
        self.__magic_board.grid(row=1, column=0)

        self.__magic_board.create_line(0,500,10,490)

