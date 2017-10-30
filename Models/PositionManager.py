class PositionManager:

    def __init__(self):
        self.__x_coord = 0
        self.__y_coord = 0

    def get_position_x(self):
        return int(self.__x_coord)

    def get_position_y(self):
        return int(self.__y_coord)

    def set_position(self, actual_x, actual_y):
        self.__x_coord = actual_x
        self.__y_coord = actual_y



