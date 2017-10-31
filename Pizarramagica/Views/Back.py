from tkinter import Label

class BackGround(Label):
    class Constants:
        width=800
        height=600
    def __init__ (self,master,x,y,image):
        self.__label=Label(master,image=image)
        #self.__label.configure(width=self.Constants.width,height=self.Constants.height)
        self.__label.place(x=x,y=y)
