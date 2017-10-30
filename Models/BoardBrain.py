class BoardBrain():

    class Constants:
        heigth = 500
        width = 600

    def __init__(self):
        self.__is_initialized = True

    def get_coordinates(self, x_coordinate, y_coordinate):
        if self.__is_initialized:
            self.initial_y_coordinate = y_coordinate
            self.initial_x_coordinate = x_coordinate
            self.__is_initialized = False
        coordinate = self.initial_x_coordinate, self.initial_y_coordinate, x_coordinate, y_coordinate
        self.initial_x_coordinate = x_coordinate
        self.initial_y_coordinate = y_coordinate
        return coordinate