from Views.MainView import MainView

class MainApp():
    def __init__(self):
        self.__master = MainView(tap_handler = self.__did_tap)

    def run(self):
        self.__master.mainloop()

    def __did_tap(self, color):
        #print(color)
        pass


if __name__ == '__main__':
    app = MainApp()
    app.run()