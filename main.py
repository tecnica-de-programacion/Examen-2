from Views.MainView import MainView
from serial import Serial
from serial.tools import list_ports


class MainApp:

    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)
        self.__master = MainView()
        self.__arduino = Serial('COM3', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__master.bind('<space>', self.__erase)

    def run(self):
        self.__update_clock()
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def __update_clock(self):
        data = self.__arduino.readline().decode()
        self.__handle_data(data)
        self.__master.after(1, self.__update_clock)

    def __handle_data(self, data):
        clean_values = data.strip("\n\r").split(",")
        print(clean_values)
        x_value = int(clean_values[3])
        y_value = int(clean_values[2])
        self.__master.update_dot(x_value, y_value)

    def __erase(self, event):
        self.__master.erase_window()


if __name__ == "__main__":
    app = MainApp()
    app.run()