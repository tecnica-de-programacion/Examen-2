from Views.MainView import MainView
import serial


class MainApp():

    def __init__(self):
        self.__master = MainView()
        self.__arduino = serial.Serial('/dev/tty.usbmodem1411', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)


    def run (self):
        self.__master.mainloop()



    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()


if __name__ == '__main__':
    app = MainApp()
    app.run()