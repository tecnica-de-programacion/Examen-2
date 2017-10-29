from Views.MainView import MainView
import serial


class MainApp():

    def __init__(self):
        self.__master = MainView()


    def run (self):
        self.__master.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.run()