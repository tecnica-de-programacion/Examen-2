from Views.MainView import MainView
import serial
from serial.tools import list_ports

class MainApp():
    class Constants:
        port = "/dev/tty.usbmodem1421"
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
        if clean_values[0] == "Horizontal":
            position_value = int(clean_values[2])
            value_text = clean_values[1]
            axis = clean_values[0]
            print(axis,position_value,value_text)

        elif clean_values[0] == "Vertical":
            position_value = int(clean_values[2])
            value_text = clean_values[1]
            axis = clean_values[0]
            print(axis, position_value, value_text)

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
