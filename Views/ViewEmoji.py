from tkinter import Label, PhotoImage
import time

class ViewEmoji(Label):
    class Constants:
        thinking_file = "Assets/Thinking.png"
        sunglasses_file = "Assets/Sunglasses.png"
        bg = '#510082'

    def __init__(self, master):
        super().__init__(master)
        self.configure(bg = self.Constants.bg)
        self.__thinking_image = PhotoImage(file = self.Constants.thinking_file)
        self.__sunglasses_image = PhotoImage(file = self.Constants.sunglasses_file)

    def change_image(self, case):
        if case:
            image = self.__thinking_image
        else:
            image = self.__sunglasses_image
        self.__set_image(image)

    def __set_image(self, image):
        self.configure(image = image)
        self.image = image