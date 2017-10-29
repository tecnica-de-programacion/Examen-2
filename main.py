from Views.MainView import MainView
import serial
from serial.tools import list_ports
from Models.MainModel import MainModel

class MainApp():
    class Constants:
        port = "/dev/cu.usbmodem1411"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        for port in serial.tools.list_ports.comports(include_links = True):
            print(port.device, port.name, port.description)

        self.__master = MainView()
        self.__controler = MainModel()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__master.update_pointer(self.generate_data())



    def run(self):
        self.__master.mainloop()


    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def generate_data(self):
        valid_data = False
        for i in range(0,3):
            data = self.__arduino.readline().decode()
            valid_data = self.__controler.validator_of_data(data)
            if valid_data == True:
                return data
        return None


if __name__ == "__main__":
    app = MainApp()
    app.run()
