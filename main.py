from Views.MainView import MainView
from serial import Serial

class MainApp():
    def __init__(self):
        self.__master = MainView()
        self.__arduino = Serial('/dev/tty.usbmodem1451', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

    def run(self):
        self.__update_clock()
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def __update_clock(self):
        data = self.__arduino.readline().decode()
        self.__handle_data(data)
        self.__master.after(1, self.__update_clock)

    def __handle_data(self, data):
        clean_values = data.strip(" \n\r").split(",")

        print(clean_values)


if __name__ == "__main__":
    app = MainApp()
    app.run()