from Views.MainView import MainView
import serial
from serial.tools import list_ports
import threading

class MainApp():
    class Constants:
        port = "COM5"
        baud =115200
        close_event ="WM_DELETE_WINDOW"

    def __init__ (self):
        self.__master= MainView()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update_signal()

    def __update_signal (self):
        data = self.__arduino.readline().decode()
        self.__handle_data (data)
        self.__master.after(1,self.__update_signal)

    def __handle_data (self,data):
        clean_values = data.strip(' \n\r').split(",")
        print (clean_values)
        vertical_move = int(clean_values[0])
        horizontal_move = int(clean_values[1])

        self.__master.update_line(vertical_move, horizontal_move)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def run (self):
        self.__master.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.run()