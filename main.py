from Views.MainView import MainView
import serial
from serial.tools import list_ports


class MainApp():
    class Constants:
        port = "COM5"
        baud = 9600
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

        clean_values = data.strip('  \n\r').split(",")
        value_y = int(clean_values[0])
        value_x = int(clean_values[1])
        value_text = clean_values[0]
        self.__master.update_lines(value_x, value_y)
        print(self.__master.Constants.color)


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

