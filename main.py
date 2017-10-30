from Views.MainView import MainView
import serial


class MainApp():
    class Constants:
        port = "COM3"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"


    def __init__(self):
        self.__master = MainView()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.__update()

    def __update(self):
        data = self.__arduino.readline().decode()
        clean_data = data.strip(" \n\r").split(",")
        try:
            x = int(clean_data[0])
            y = int(clean_data[1])
            self.__master.draw_line(x, y)
        except:
            pass
        self.__master.after(1, self.__update)


    def run(self):
        self.__master.mainloop()

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app=MainApp()
    app.run()




