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
        self.__times_launched = 0

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
        if self.__times_launched < 2: self.__master.clear_window()
        self.__times_launched += 1
        clean_values = data.strip("\n\r").split(",")
        print(clean_values)
        new_x = int(clean_values[3])
        new_y = int(clean_values[2])
        self.__master.update_line(new_x, new_y)

    def __erase(self, event):
        self.__master.clear_window()


if __name__ == "__main__":
    app = MainApp()
    app.run()