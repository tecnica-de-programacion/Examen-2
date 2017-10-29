from Views.MainView import MainView
import serial
from serial.tools import list_ports
import threading

class MainApp():
    class Constants:
        port = "COM3"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        for port in list_ports.comports(include_links = True):
            print(port.device, port.name, port.description)
        self.__master = MainView()

    def run(self):
        self.__master.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.run()

