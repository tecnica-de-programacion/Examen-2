from tkinter import Tk, Canvas, PhotoImage,ALL
from Views.Buttons import ChangeColorButton
from Views.Labels import BackGround
class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigthV = 1000
        widthV = 1000
        event_space = '<space>'
        heigthC =500
        widthC = 600
        Red = '#FF0000'
        Black = '#000000'
        Green = '#00BB00'
        Blue = '#0000BB'

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.widthV, cls.heigthV)
    class Images:
        Black_button = "assets/blackB2.png"
        Blue_button = "assets/blueB2.png"
        Green_button = "assets/greenB.png"
        Red_button = "assets/redB.png"
        My_board = "assets/pi.png"




    class NewPencil:
        pencil_color = '#000000'

    def __init__(self,tap_button_handler=None,tap_space_handler=None):
        super().__init__()
        self.__tap_button_handler=tap_button_handler
        self.__tap_space_handler=tap_space_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.widthV,self.Constants.heigthV)
        self.__new_position=[]
        self.__interfaz_configure()

    def __interfaz_configure(self):

        self.__line = None

        self.__fondo = PhotoImage(file = self.Images.My_board)

        self.__board =BackGround(self,100,18,image=self.__fondo,width=600)

        self.__canvas = Canvas(self, width = self.Constants.widthC , height=self.Constants.heigthC,bg="white")
        self.__canvas.place(x = 100,y = 30)

        self.__blackBi = PhotoImage(file=self.Images.Black_button)
        self.__black_button= ChangeColorButton(self ,13,30,self.Constants.Black,self.__blackBi,action=self.__did_button_tap)

        self.__blueBi=PhotoImage(file=self.Images.Blue_button)
        self.__blue_button= ChangeColorButton(self ,13,400,self.Constants.Blue,self.__blueBi,action=self.__did_button_tap)

        self.__redBi=PhotoImage(file=self.Images.Red_button)
        self.__red_button= ChangeColorButton(self ,710,30,self.Constants.Red,self.__redBi,action=self.__did_button_tap)

        self.__greenBi=PhotoImage(file=self.Images.Green_button)
        self.__green_button= ChangeColorButton(self ,710,400,self.Constants.Green,self.__greenBi,action=self.__did_button_tap)

    def __did_button_tap(self,color):
        if self.__tap_button_handler is None: return
        self.__tap_button_handler(color)

    def __did_space_tap(self,space):
        if self.__tap_space_handler is None: return
        self.__tap_space_handler()



    def update_canvas(self , Xvalue, Yvalue):

        if self.__new_position:
            self.__line= self.__canvas.create_line(self.__new_position[0],self.__new_position[1], Xvalue, Yvalue ,width=3,fill=self.NewPencil.pencil_color)
            self.__new_position[0]= Xvalue
            self.__new_position[1] = Yvalue
        else:
            self.__new_position.append(Xvalue)
            self.__new_position.append(Yvalue)

        self.bind(self.Constants.event_space, self.__did_space_tap)

    def clean_screen(self):
        self.__canvas.delete(self,ALL)


