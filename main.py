from Views.MainView import MainView
from Models.LineManager import LineManager
from serial import Serial

class MainApp():
    def __init__(self):
        self.__master = MainView(color_handler=self.color_handler)
        self.__arduino = Serial('/dev/tty.usbmodem1451', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__coordinates = LineManager(update_handler=self.on_coordinates_change,
                                         reset_handler=self.reset_coordinates)
        self.__master.bind('<space>', self.on_space_clicked)

    def run(self):
        self.__update_clock()
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def __update_clock(self):
        data = self.__arduino.readline().decode()
        self.__coordinates.analize_data(data)
        self.__master.after(100, self.__update_clock)

    def update_coordintes(self, coordinates, color):
        self.__master.update_drawing(coordinates, color)

    def reset_coordinates(self):
        self.__master.reset_drawing()

    def on_coordinates_change(self, coordinates, color):
        self.update_coordintes(coordinates, color)

    def on_space_clicked(self, event):
        self.__coordinates.reset_values()

    def color_handler(self, color):
        print(color)
        self.__coordinates.update_line_color(color)


if __name__ == "__main__":
    app = MainApp()
    app.run()