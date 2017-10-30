from tkinter import Label, N, S, E, W, Button

class Buttons():

    class Constants:
        text_button = "Turn the color to  "
        size = 50
        width = 4
        border_type = 'groove'
        border_width = 10
        center = W + E + N + S
        font = ("Arial, 12")

    def __init__(self,master,color,y):
        self.color =color
        self.button = Button(master, text = "Change the color to " + color,command = self.__change_color ).place(x = 560,y= y, )
        #self.button.configure(width = self.Constants.size, height=self.Constants.size )
        #self.button.configure(font = self.Constants.font,command = self.__cambiar_color)
        #self.button.configure(borderwidth = self.Constants.border_width,relief = self.Constants.border_type)

    def __change_color(self,color):
        pass



