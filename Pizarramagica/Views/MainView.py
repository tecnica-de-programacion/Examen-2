from tkinter import Tk, Canvas, Button,Label,PhotoImage

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
        self.__pencil_color= "Blue"
        self.__line = None
        #self.__fondo = Label(self, image=self.Constants.the_board)
        #self.__fondo.place(x=50, y=20)
        self.__canvas = Canvas(self, width = self.Constants.widthC , height=self.Constants.heigthC,bg="white")
        self.__canvas.place(x = 60,y = 30)

        self.__botonA=Button(self ,text ="Blue",bg="blue",command= to_Blue)
        self.__botonA.place(x = 700,y =30)
        self.__botonB = Button(self, text="Black", bg="black",command= to_Black)
        self.__botonB.place(x = 3,y = 30)
        self.__botonV= Button(self, text="Green", bg="green",command= to_Green)
        self.__botonV.place(x = 3,y = 120)
        self.__botonR = Button(self, text="Red", bg="Red",command= to_Red)
        self.__botonR.place(x = 700,y= 120)




    def update_canvas(self , Xvalue, Yvalue):

        if self.__new_position:
            self.__line= self.__canvas.create_line(self.__new_position[0],self.__new_position[1], Xvalue, Yvalue ,width=3,fill=self.__pencil_color)
            self.__new_position[0]= Xvalue
            self.__new_position[1] = Yvalue
        else:
            self.__new_position.append(Xvalue)
            self.__new_position.append(Yvalue)


def to_Blue(self):
    self.__pencil_color = "Blue"

def to_Green(self):
    self.__pencil_color = "Green"

def to_Red(self):
    self.__pencil_color = "Red"

def to_Black(self):
        self.__pencil_color = "Black"

