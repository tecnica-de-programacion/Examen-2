from tkinter import Tk, Canvas, Label, N, S, E, W , Button
from Views.Buttons import ButtonsF

class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigthV = 600
        widthV = 800
        heigthC =500
        widthC = 600


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.widthV, cls.heigthV)



    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__new_position=[]
        self.__line = None
        self.__canvas = Canvas(self, width = self.Constants.widthC , height=self.Constants.heigthC,bg="white").place(x=60,y=30)
        self.__botonA=Button(self,text="Blue",bg="blue").place(x=700,y=30)
        self.__botonB = Button(self, text="Black", bg="black").place(x=3,y=30)
        self.__botonV= Button(self, text="Green", bg="green").place(x=3,y=120)
        self.__botonR = Button(self, text="Red", bg="Red").place(x=700,y=120)
        self.update_canvas(0,0)


    def update_canvas(self,Xvalue,Yvalue):
        #if self.__new_position:
        if self.__line is not None:
            self.__canvas.delete(self.__line)
        self.__line= self.__canvas.create_line(0,Xvalue, Xvalue, Yvalue )
            #self.__new_position[0]= Xvalue
            #self.__new_position[1] = Yvalue
        #else:
            #self.__new_position.append(Xvalue)
            #self.__new_position.append(Yvalue)

#def to_Blue(self):
    #self.Constants.pencil_color= "Blue"



#def to_Green(self):
    #self.Constants.pencil_color = "Green"


#def to_Red(self):
    #self.Constants.pencil_color= "Red"


#def to_Black(self):
    #self.Constants.pencil_color= "Black"
