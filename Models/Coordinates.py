class Coordinates:
    def __init__(self, coordinates_value):
        try:
            self.__x_coordinate = coordinates_value[1]
            self.__y_coordinate = coordinates_value[0]
        except IndexError:
            pass

    @property
    def x_coordinate(self):
        try:
            return int(self.__x_coordinate)
        except ValueError:
            return None

    @property
    def y_coordinate(self):
        try:
            return int(self.__y_coordinate)
        except ValueError:
            return None
