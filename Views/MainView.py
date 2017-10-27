from tkinter import Tk, Label, Canvas, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Pizarra Magica"
        height = 900
        width = 1000
        center = N + S + E + W
        color = 'salmon'

        @classmethod
        def size (cls):
            return '{}x{}'.format(cls.width,cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
