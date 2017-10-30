from tkinter import Label, PhotoImage

class GreenButton(Label):

    class Constants:
        green_on = "Assets/green_button_on.ppm"
        green_off = "Assets/green_button_off.ppm"
        event = "<Button-1>"

    def __init__(self, master):
        super().__init__(master)
        self.__state = False
        self.__on_image = PhotoImage(file = self.Constants.green_on)
        self.__off_image = PhotoImage(file = self.Constants.green_off)
        self.__set_image(self.__on_image)
        self.bind(self.Constants.event, self.__toggle)

    def __toggle(self, event):
        self.__state = not self.__state
        image = self.__on_image if self.__state else self.__off_image
        self.__set_image(image)

    def __set_image(self, image):
        self.configure(image = image)
        self.image = image
