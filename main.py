from Views.MainView import MainView
import serial
from serial.tools import list_ports


class MainApp():
    class Constants:
        port = "/dev/cu.usbmodem1411"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        for port in serial.tools.list_ports.comports(include_links = True):
            print(port.device, port.name, port.description)

            self.__master = MainView()
            self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
            self.__master.protocol(self.Constants.close_event, self.__on_closing)


    def run(self):
        self.__master.mainloop()


    def __handle_data(self, data):
        clean_values = data.strip(' \n\r').split(',')
        y_value = int(clean_values[0])
        x_value = int(clean_values[1])

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()
