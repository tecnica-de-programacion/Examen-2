class DrawBrain:
    class Constants:
        heigth = 500
        width = 600

    def __init__(self):
        self.__vertical_initial = self.Constants.heigth
        self.__horizontal_initial = 0

    def start (self, vertical_value, horizontal_value):
        self.__vertical_initial = vertical_value
        self.__horizontal_initial = horizontal_value

    def coordinates(self, vertical_value, horizontal_value):
        coordinates = self.__horizontal_initial, self.__vertical_initial, horizontal_value, vertical_value
        self.start(vertical_value, horizontal_value)
        return coordinates


