class Coordinates:
    def __init__(self, coordinates_value):
        self.__x_coordinate = coordinates_value[1]
        self.__y_coordinate = coordinates_value[0]

    @property
    def x_coordinate(self):
        return int(self.__x_coordinate)

    @property
    def y_coordinate(self):
        return int(self.__y_coordinate)
