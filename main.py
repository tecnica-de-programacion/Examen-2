from Views.MainView import MainView
from Models.DrawBrain import DrawBrain
import serial
from serial.tools import list_ports

class MainApp ():
    class Constants:
        port = "COM8"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"
        heigth = 500
        width = 600

    def __init__(self):
        for port in list_ports.comports(include_links= True):
            print(port.device, port.name, port.description)

        self.__master = MainView()
        self.__brain = DrawBrain()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__initial_position = False
        self.__update_clock()
        self.__color = None


    def run(self):
        self.__master.mainloop()

    def __handle_data(self, data):
        clean_values = data.strip(' \r\n').split(',')
        try:
            vertical_value = self.Constants.heigth - int(clean_values[0])
            horizontal_value = int(clean_values[1])
        except Exception:
            return
        else:
            if self.__initial_position:
                coordinates = self.__brain.coordinates(vertical_value, horizontal_value)
                self.__master.update_line(coordinates)
            else:
                self.__brain.start(vertical_value, horizontal_value)
                self.__initial_position = True
            self.__master.update_position('Posición: '+ str(horizontal_value) + ',' + str(clean_values[0]))

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