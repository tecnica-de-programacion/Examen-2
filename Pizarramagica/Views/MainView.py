from tkinter import Tk, Canvas, PhotoImage,ALL
from Views.Buttons import ChangeColorButton
from Views.Labels import BackGround
class MainView(Tk):
    class Constants:
        title = "Pizarra magica"
        heigthV = 900
        widthV = 890
        event_space = '<space>'
        heigthC = 500
        widthC = 600
        widthB=630
        widthP = 320
        widthPs = 288
        widthT = 66
        widthPencil = 3
        bg = '#FFFFFF'
        board_bg = '#006400'
        Red = '#FF0000'
        Black = '#000000'
        Green = '#7FFF00'
        Blue = '#00BFFF'

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.widthV, cls.heigthV)

    class Images:
        Black_button = "assets/blackB.png"
        Blue_button = "assets/blueB.png"
        Green_button = "assets/greenB.png"
        Red_button = "assets/redB.png"
        My_board = "assets/pi.png"
        alone_pig = "assets/puerco.png"
        pigs = "assets/puercos.png"
        angryB = "assets/angry birds.png"
        angryB2 = "assets/angry birds2.png"


    class Positions:
        x_canv = 145
        y_backg = 0
        x_backg = 131
        x_title = 38
        y_title = 110
        y_title2= 150
        x_black_blue = 35
        y_canv_redB_blackB = 16
        y_blue_gren = 430
        x_red_green_t2 = 780
        x_pig = 5
        x_pigs=600
        y_pig = 600
        y_pigs = 550

    class NewPencil:
        pencil_color = '#000000'

    def __init__(self, tap_button_handler = None, tap_space_handler = None):
        super().__init__()
        self.__tap_button_handler = tap_button_handler
        self.__tap_space_handler = tap_space_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.configure(bg=self.Constants.bg)
        self.minsize(self.Constants.widthV, self.Constants.heigthV)
        self.maxsize(self.Constants.widthV,self.Constants.heigthV)
        self.__new_position = []
        self.__interfaz_configure()

    def __interfaz_configure(self):

        self.__line = None



        self.__lienzo = PhotoImage(file = self.Images.My_board)
        self.__board = BackGround(self, self.Positions.x_backg, self.Positions.y_backg, image = self.__lienzo, width = self.Constants.widthB)

        self.__canvas = Canvas(self, width = self.Constants.widthC , height = self.Constants.heigthC, bg = self.Constants.board_bg)
        self.__canvas.place( x = self.Positions.x_canv, y = self.Positions.y_canv_redB_blackB)

        self.__puerco = PhotoImage(file=self.Images.alone_pig)
        self.__pig= BackGround(self, self.Positions.x_pig, self.Positions.y_pig, image=self.__puerco,
                                  width=self.Constants.widthP)

        self.__title = PhotoImage(file=self.Images.angryB)
        self.__pig = BackGround(self, self.Positions.x_title, self.Positions.y_title, image=self.__title,
                                width=self.Constants.widthT)

        self.__title2 = PhotoImage(file=self.Images.angryB2)
        self.__pig = BackGround(self, self.Positions.x_red_green_t2, self.Positions.y_title2, image=self.__title2,
                                width=self.Constants.widthT)

        self.__puercos = PhotoImage(file=self.Images.pigs)
        self.__pigs = BackGround(self, self.Positions.x_pigs, self.Positions.y_pigs, image=self.__puercos,
                                width=self.Constants.widthPs)

        self.__blackBi = PhotoImage(file = self.Images.Black_button)
        self.__black_button = ChangeColorButton(self, self.Positions.x_black_blue, self.Positions.y_canv_redB_blackB, self.Constants.Black,self.__blackBi,action = self.__did_button_tap)

        self.__blueBi = PhotoImage(file = self.Images.Blue_button)
        self.__blue_button = ChangeColorButton(self, self.Positions.x_black_blue, self.Positions.y_blue_gren, self.Constants.Blue, self.__blueBi,action = self.__did_button_tap)

        self.__redBi = PhotoImage(file = self.Images.Red_button)
        self.__red_button = ChangeColorButton(self, self.Positions.x_red_green_t2, self.Positions.y_canv_redB_blackB, self.Constants.Red, self.__redBi,action = self.__did_button_tap)

        self.__greenBi = PhotoImage(file = self.Images.Green_button)
        self.__green_button = ChangeColorButton(self, self.Positions.x_red_green_t2, self.Positions.y_blue_gren, self.Constants.Green, self.__greenBi,action = self.__did_button_tap)

    def __did_button_tap(self, color):
        if self.__tap_button_handler is None: return
        self.__tap_button_handler(color)

    def __did_space_tap(self, space):
        if self.__tap_space_handler is None: return
        self.__tap_space_handler()

    def update_canvas(self, Xvalue, Yvalue):

        if self.__new_position:
            self.__line = self.__canvas.create_line(self.__new_position[0], self.__new_position[1], Xvalue, Yvalue, width = self.Constants.widthPencil, fill = self.NewPencil.pencil_color)
            self.__new_position[0] = Xvalue
            self.__new_position[1] = Yvalue
        else:
            self.__new_position.append(Xvalue)
            self.__new_position.append(Yvalue)

        self.bind(self.Constants.event_space, self.__did_space_tap)

    def clean_screen(self):
        self.__canvas.delete(self,ALL)


