from Views.MainViews import MainView
from Models.HandleData import HandleData
import serial
from serial.tools import list_ports
import threading

class MainApp():
    class Constants:
        port = "COM3"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)

        self.__master = MainView()
        self.__data = HandleData()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update_sketch()


    def run(self):
        self.__master.mainloop()

    def __update_sketch(self):
        data_arduino = self.__arduino.readline().decode()
        data = self.__data.clean_data(data_arduino)
        try:
            self.__master.update_line(int(data[0]), int(data[1]))
        except:
            pass

        self.__master.after(1, self.__update_sketch)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()