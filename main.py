from Views.MainView import MainView
from Models.DataHandler import DataHandler
import serial
from serial.tools import list_ports

class MainApp():
    class Constants:
        port = "COM7"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)
        self.__master = MainView()
        self.__data = DataHandler()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update_clock()


    def run(self):
        self.__master.mainloop()

    def __update_clock(self):
        arduino = self.__arduino.readline().decode()
        data = self.__data.clean_data(arduino)
        try:
            self.__master.set_pencil(int(data[0]), int(data[1]))
        except ValueError:
            self.__master.after(1, self.__update_clock)
        except IndexError:
            self.__master.after(1, self.__update_clock)
        else:
            self.__master.after(1, self.__update_clock)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()
