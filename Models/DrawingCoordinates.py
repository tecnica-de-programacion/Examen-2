class DrawingCoordinates:
    def __init__(self, acutual_x_coordinate, actual_y_coordinate, modify_x_coordinate, modify_y_coordinate):
        self.__actual_x_coordinate = acutual_x_coordinate
        self.__actual_y_coordinate = actual_y_coordinate
        self.__modify_x_coordinate = modify_x_coordinate
        self.__modify_y_coordinate = modify_y_coordinate

    @property
    def actual_x_coordinate(self):
        return int(self.__actual_x_coordinate)

    @property
    def actual_y_coordinate(self):
        return int(self.__actual_y_coordinate)

    @property
    def modify_x_coordinate(self):
        return int(self.__modify_x_coordinate)

    @property
    def modify_y_coordinate(self):
        return int(self.__modify_y_coordinate)
