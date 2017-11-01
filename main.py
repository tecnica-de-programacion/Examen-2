from Views.MainView import MainView
import serial
from serial.tools import list_ports

class MainApp():
    class Constants:
        port = "COM6"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)
        self.__master = MainView()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update_clock()

    def run(self):
        self.__master.mainloop()

    def __handle_data(self, data):
        clean_values = data.strip(' \n\r').split(",")
        y_value = int(clean_values[3])
        x_value = int(clean_values[1])
        self.__master.update_line(x_value+200, y_value+20)

    def __update_clock(self):
        data = self.__arduino.readline().decode()
        self.__handle_data(data)
        self.__master.after(1, self.__update_clock)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()