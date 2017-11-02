from tkinter import Tk, Button, Label, PhotoImage, Canvas, N, S, E, W

class DrawScreen(Canvas):
    class Constants:
        drawing_screen_height = 500
        drawing_screen_width = 600
        color_bg = '#911e5d'

    def __init__(self, master, drawing_screen_height, drawing_screen_width):
        super().__init__(master)
        self.__drawing_canvas = Canvas(self, width=self.Constants.drawing_screen_width,
                               height=self.Constants.drawing_screen_height, bg=self.Constans.color_bg)
        self.__drawing_canvas.grid(row = 1, column = 0)

class ColorButton():
    def __init__(self, master, column, color, action=None):
        self.__master = master
        self.__column = column
        self.__color = color
        self.__action = action

    def __press_button_tap(self):
        if self.__action is None: return
        self.__action(self.__color)

class Buttons():
    def __init__(self, master, color_handler=None):
        self.__master = master
        self.__configure_buttons(color_handler)

    def __configure_buttons(self, color_handler):
        self.__label_button_color = LabelFrame(self.__master)
        self.__label_button_color.grid(row=0, column=0)


class MainView(Tk):
    class Constants:
        title = 'Pizarra mágica'
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








