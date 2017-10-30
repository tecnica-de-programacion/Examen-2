from Views.MainView import MainView
import serial

class MainApp():
    class Constants:
        port = 'COM3'
        baud = 115200
        close_event = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__master = MainView(tap_button_handler = self.__did_button_tap, tap_space_handler = self.__did_space_tap)
        self.__port = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update_coordinate()

    def run(self):
        self.__master.mainloop()

    def __did_button_tap(self, color):
        self.__master.ChangeColor.line_color = color

    def __did_space_tap(self):
        self.__master.clean_screen()

    def __update_coordinate(self):
        coordinates = self.__port.readline().decode()
        self.__handle_coordinate(coordinates)
        self.__master.after(5, self.__update_coordinate)

    def __handle_coordinate(self, coordinate):
        clean_values = coordinate.strip(' \n\r').split(",")
        coordinate_y = int(clean_values[1])
        coordinate_x = int(clean_values[3])
        self.__master.update_canvas(coordinate_x, coordinate_y)

    def __on_closing(self):
        self.__port.close()
        self.__master.destroy()

if __name__ == '__main__':
    app = MainApp()
    app.run()