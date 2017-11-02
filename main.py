from tkinter import Tk, Button, Label, PhotoImage, Canvas, N, S, E, W

class ColorButton():
    def __init__(self, master, column, color, file_path, action=None):
        self.__master = master
        self.__color = color
        self.__file_path = file_path
        self.__action = action
        self.__column = column

class MainView(Tk):
    class Constants:
        title = 'Pizarra mágica'
        drawing_screen_height = 500
        drawing_screen_width = 600
        width = 900
        height = 700
        event_space = '<space>'
        Black = "#262525"
        Blue = '#1025bc'
        Red = "#d60a0a"
        Green = '#4abb00'

        @classmethod
        def size(cls):
            return '{0}x{1}'.format(cls.width, cls.height)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.height)
        self.maxsize(self.Constants.width, self.Constants.height)

class MainApp:
    def __init__(self):
        self.__master = MainView()

    def run(self):
        self.__master.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.run()








