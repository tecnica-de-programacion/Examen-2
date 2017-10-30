from tkinter import Tk, Canvas, Label, N, S, E, W , Button

class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigthV = 700
        widthV = 800
        heigthC =500
        widthC = 600
        center = N + S + E + W
        my_board="assets/lienzo.png"

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.widthV, cls.heigthV)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__new_position=[0,0]
        #self.__line = None
        self.__canvas = Canvas(self, width = self.Constants.widthC, height=self.Constants.heigthC,bg="red").grid(row=2,column=2)
        self.__botonA=Button(self,text="Blue",bg="blue").grid(row=1,column=1)
        self.__botonB = Button(self, text="Black", bg="black").grid(row=3,column=3)
        self.__botonV= Button(self, text="Green", bg="green").grid(row=1,column=3)
        self.__botonR = Button(self, text="Red", bg="Red").grid(row=3,column=1)
        self.update_bar(0,0)




    def update_bar(self,Xvalue,Yvalue):
        if self.__new_position:
            self.__canvas.create_line(self.__new_position[0] , self.__new_position[1], Xvalue, Yvalue)
            self.__new_position[0]= Xvalue
            self.__new_position[1] = Yvalue
        else:
            self.__new_position.append(Xvalue)
            self.__new_position.append(Yvalue)


