from Views.MainView import MainView
from Models.CoordinatesManager import CoordinatesManager
from serial import Serial

class MainApp():
    def __init__(self):
        self.__master = MainView()
        self.__arduino = Serial('/dev/tty.usbmodem1451', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__coordinates = CoordinatesManager(update_handler=self.on_coordinates_change)

    def run(self):
        self.__update_clock()
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def __update_clock(self):
        data = self.__arduino.readline().decode()
        self.__coordinates.analize_data(data)
        self.__master.after(10, self.__update_clock)

    def update_coordintes(self, coordinates):
        self.__master.update_drawing(coordinates)

    def on_coordinates_change(self, coordinates):
        self.update_coordintes(coordinates)



if __name__ == "__main__":
    app = MainApp()
    app.run()