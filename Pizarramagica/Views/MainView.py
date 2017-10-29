from tkinter import Tk, Canvas, Label, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigthV = 700
        widthV = 800
        heigthC =600
        widthC = 500
        center = N + S + E + W


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.widthV, cls.heigthV)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.new_position=[]

        self.__line = None
        self.__lable = Label(self)
        self.__canvas = Canvas(self, width = self.Constants.widthC, height=self.Constants.heigthC,bg="pink")

        self.__canvas.grid( sticky=self.Constants.center)
        self.__lable.grid(row=0, column=1, sticky = self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)
        self.grid_columnconfigure(1, weight=True, minsize = self.Constants.widthV / 2)

        self.update_bar(0,0,new_position=[])


    def update_bar(self,Xvalue,Yvalue,new_position):
        if len(new_position)==0:
            return
        else:
          new_position[0] = Xvalue
          new_position[1] = Yvalue

        self.__line = self.__canvas.create_line(new_position[0],new_position[1] ,Xvalue, Yvalue)

