from Views.MainView import MainView
#from Models.PrincipalFuction import PrincipalFuction
import serial


class MainApp():

    def __init__(self):
        self.__master = MainView()
        #self.__principal = PrincipalFuction()
        self.__arduino = serial.Serial('/dev/tty.usbmodem1411', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__data_updates()

    def __data_updates(self):
        data = self.__arduino.readline().decode()
        update_data = data.strip(" \n\r").split(",")
        try:
          x = float(update_data[0])
          y = float(update_data[1])
          self.__master.drawing_function(x, y)
        except:
            pass


        self.__master.after(1, self.__data_updates)


    def run (self):
        self.__master.mainloop()



    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()


if __name__ == '__main__':
    app = MainApp()
    app.run()