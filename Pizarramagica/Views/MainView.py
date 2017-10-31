from tkinter import Tk, Canvas, Button,Label,PhotoImage
from Views.Buttons import ChangeColorButton
from Views.Back import BackGround
class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigthV = 800
        widthV = 960
        heigthC =500
        widthC = 600
        Black_button = "assets/blackB.png"
        Blue_button = "assets/blueB.png"
        Green_button = "assets/greenB.png"
        Red_button = "assets/redB.png"
        My_board = "assets/pi.png"


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.widthV, cls.heigthV)

    class NewPencil:
        pencil_color="#000000"

    def __init__(self,tap_button_handler=None):
        super().__init__()
        self.__tap_button_handler=tap_button_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.widthV,self.Constants.heigthV)
        self.__new_position=[]
        self.__interfaz_configure()

    def __interfaz_configure(self):
        self.__pencil_color= "Blue"
        self.__line = None

        self.__fondo = PhotoImage(file = self.Constants.My_board)

        self.__board =BackGround(self,0,0,image=self.__fondo)

        self.__canvas = Canvas(self, width = self.Constants.widthC , height=self.Constants.heigthC,bg="white")
        self.__canvas.place(x = 90,y = 30)

        self.__blackBi = PhotoImage(file=self.Constants.Black_button)
        self.__black_button= ChangeColorButton(self ,3,30,"black",self.__blackBi,action=self.__did_button_tap)

        self.__blueBi=PhotoImage(file=self.Constants.Blue_button)
        self.__blue_button= ChangeColorButton(self ,3,400,"blue",self.__blueBi,action=self.__did_button_tap)

        self.__redBi=PhotoImage(file=self.Constants.Red_button)
        self.__red_button= ChangeColorButton(self ,700,30,"red",self.__redBi,action=self.__did_button_tap)

        self.__greenBi=PhotoImage(file=self.Constants.Green_button)
        self.__green_button= ChangeColorButton(self ,700,400,"red",self.__greenBi,action=self.__did_button_tap)

    def __did_button_tap(self,color):
        if self.__tap_button_handler is None: return
        self.__tap_button_handler(color)



    def update_canvas(self , Xvalue, Yvalue):

        if self.__new_position:
            self.__line= self.__canvas.create_line(self.__new_position[0],self.__new_position[1], Xvalue, Yvalue ,width=3,fill=self.NewPencil.pencil_color)
            self.__new_position[0]= Xvalue
            self.__new_position[1] = Yvalue
        else:
            self.__new_position.append(Xvalue)
            self.__new_position.append(Yvalue)




