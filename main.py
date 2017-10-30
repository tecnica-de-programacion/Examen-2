from Views.MainView import MainView
from Models.Brain import Brain
from serial.tools import list_ports
import serial

class MainApp():
    class Constants:
        port = "COM5"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)

        self.__master = MainView()
        self.__controller = Brain()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.first_data = self.__controller.handle_data(self.__arduino.readline().decode())
        self.__last_x = self.first_data[0]
        self.__last_y = self.first_data[1]
        self.__draw()

    def run(self):
        self.__master.mainloop()


    def __create_figure(self, data):
        final_point = self.__master.draw_line(self.__last_x, self.__last_y, data)
        self.__last_x = final_point[0]
        self.__last_y = final_point[1]

    def __draw(self):
        coordinates = self.__controller.validator_data(self.__arduino.readline().decode())
        self.__create_figure(coordinates)
        self.__master.after(20,self.__draw)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()
