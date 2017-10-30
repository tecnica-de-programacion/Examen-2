from Views.MainView import MainView
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
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update()

    def run(self):
        self.__master.mainloop()

    def __handle_data(self, data):
        clean_values = data.strip(' \n\r').split(",")

        position_H= int(clean_values[1])
        position_V = int(clean_values[0])

        self.__master.space_work(position_H, position_V)
        self.__master.Constants.__pencil_pos(position_H, position_V)

    def __update(self):
        data = self.__arduino.readline().decode()
        self.__handle_data(data)
        self.__master.after(1, self.__update)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__" :
    app = MainApp()
    app.run()