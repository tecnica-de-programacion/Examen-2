from tkinter import Label, PhotoImage


class PokemonButton(Label):

    class Constants:
        black_file = "Assets/black.ppm"
        blue_file = "Assets/blue.ppm"
        green_file = "Assets/green.ppm"
        red_file = "Assets/red.ppm"
        event = "<Button-1>"

    def __init__(self, master, tap_color_handler = None):
        super().__init__(master)
        self.__tap_handler = tap_color_handler
        self.__state = False
        self.__black_image = PhotoImage(file = self.Constants.black_file)
        self.__blue_image = PhotoImage(file = self.Constants.blue_file)
        self.__green_image = PhotoImage(file = self.Constants.green_file)
        self.__red_image = PhotoImage(file = self.Constants.red_file)
        self.bind(self.Constants.event, self.__toggle)
        self.__set_images()

    def __toggle(self, event):
        return


    def __set_images(self):
        self.configure(image = image)
        self.image = image