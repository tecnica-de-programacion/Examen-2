from Views.MainView import MainView
import serial
from Models.InteractiveCanvasBrain import InteractiveCanvasBrain

class MainApp():
    class Constants:
        port = "/dev/cu.usbmodem1411"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = MainView()
        self.__magic_board = InteractiveCanvasBrain()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update_clock()

    def run(self):
        self.__master.mainloop()

    def __handler_data(self, data):
        clean_values = data.strip(' \n\r').split(",")
        try:
            x_coordinate = int(clean_values[1])
            y_coordinate = int(clean_values[0])
        except IndexError:
            return
        self.draw(x_coordinate, y_coordinate)

    def __update_clock(self):
        data = self.__arduino.readline().decode()
        self.__handler_data(data)
        self.__master.after(1, self.__update_clock)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def draw(self, x_coordinate, y_coordinate):
        coordinates = self.__magic_board.get_composed_coordinates(x_coordinate, self.__magic_board.Constants.canvas_heigth - y_coordinate)
        self.__master.new_line(coordinates)

if __name__ == "__main__":
    app = MainApp()
    app.run()