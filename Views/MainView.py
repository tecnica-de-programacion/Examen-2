from tkinter import Tk, Canvas, Label, N, S, E, W, Button
class MainView(Tk):
    class Constants:
        title = "PIZARRA MAGICA"
        heigth_outside = 700
        width_outside = 800
        center_main_window = N + S + E + W
        bar_offset = 300
        height_inside = 500
        width_inside = 600
        tecla = "<Enter>"


        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width_outside, cls.heigth_outside)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width_outside, self.Constants.heigth_outside)
        self.maxsize(self.Constants.width_outside,self.Constants.heigth_outside)
        self.lines = None

        self.label = Label(self)

        self.canvas = Canvas(self, width=self.Constants.width_inside, height=self.Constants.height_inside)
        self.label.grid(row=0, column=3, sticky=W)
        self.canvas.grid(row=0, column=0, sticky=self.Constants.center_main_window)
        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(1, weight=True)

        self.position_x = 0
        self.position_y = 0

        self.position_x_2 = 0
        self.position_y_2 = 0
        self.contador = 0
        self.button_black = None
        self.button_green = None
        self.button_blue = None
        self.button_red= None
        self.color = self.create_buttons()
        self.create_main_window_drawing()
        self.x = 350
        self.y = 350
        self.add = 5

    def create_drawing(self, horizontal, vertical):
        if self.lines is not None:
            self.canvas.delete(self.lines)
        nueva_y = horizontal-300
        nueva_x = vertical-250
        print(nueva_x,nueva_y)



    def create_main_window_drawing(self):
        self.canvas.create_rectangle(100,100,600,600, fill = "white")

    def create_buttons(self):
        self.button_black = self.canvas.create_rectangle((10,10,90,50) ,fill= "black")
        self.canvas.tag_bind(self.button_black, "<Button-1>", lambda x: self.setColor("black"))
        self.button_green = self.canvas.create_rectangle((110,10,190,50) ,fill= "green")
        self.canvas.tag_bind(self.button_green, "<Button-1>", lambda x: self.setColor("green"))
        self.button_blue = self.canvas.create_rectangle((210,10,290,50) ,fill= "blue")
        self.canvas.tag_bind(self.button_blue, "<Button-1>", lambda x: self.setColor("Blue"))
        self.button_red = self.canvas.create_rectangle((310,10,390,50) ,fill= "red")
        self.canvas.tag_bind(self.button_red, "<Button-1>", lambda x: self.setColor("red"))

    def setColor(self,newcolor):
        self.color = newcolor
        print(self.color)
        return self.color


