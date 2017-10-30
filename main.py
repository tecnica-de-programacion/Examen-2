from Views.MainView import MainView
import serial
from serial.tools import list_ports
from Models.MainModel import MainModel

class MainApp():
    class Constants:
        port = "/dev/cu.usbmodem1411"
        baud = 115200
        close_event = "WM_DELETE_WINDOW"
        first_time = True

    def __init__(self):
        for port in serial.tools.list_ports.comports(include_links = True):
            print(port.device, port.name, port.description)

        self.__master = MainView()
        self.__controler = MainModel()
        self.__arduino = serial.Serial(self.Constants.port, self.Constants.baud)
        self.__master.protocol(self.Constants.close_event, self.__on_closing)
        self.first_lecture = self.generate_data()
        self.__last_x = self.first_lecture[0]
        self.__last_y = self.first_lecture[1]
        self.__draw()
        self.__master.space_taped("<space>")



    def run(self):
        self.__master.mainloop()



    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

    def generate_data(self):
        for i in range(0,3):
            data = self.__arduino.readline().decode()
            data_to_send = data
            if self.__controler.validator_of_data(data) == True:
                return data_to_send
        return None


    def create_figure(self,data):
        new_coordenates = self.__master.draw_figure(self.__last_x, self.__last_y, data)
        if new_coordenates != None:
            self.__last_x = new_coordenates[0]
            self.__last_y = new_coordenates[1]





    def __draw(self):
            coordinates = self.generate_data()
            self.create_figure(coordinates)
            self.__master.after(20,self.__draw)




if __name__ == "__main__":
    app = MainApp()
    app.run()
