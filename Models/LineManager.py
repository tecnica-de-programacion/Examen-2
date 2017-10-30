from Models.Coordinates import Coordinates
from Models.DrawingCoordinates import DrawingCoordinates

class LineManager():
    def __init__(self, update_handler=None,reset_handler=None):
        self.__actual_x_coordinate = None
        self.__actual_y_coordinate = None
        self.__update_handler = update_handler
        self.__reset_handler = reset_handler
        self.__color = 'black'

    def __clean_data(self, data):
        clean_values = data.strip(" \n\r").split(",")
        return clean_values

    def analize_data(self, data):

        coordinates_value = self.__clean_data(data)
        modify_coordinates = Coordinates(coordinates_value)

        if modify_coordinates.y_coordinate is None or modify_coordinates.x_coordinate is None:
             return

        if self.__actual_x_coordinate is None and self.__actual_y_coordinate is None:
            self.__actual_x_coordinate = modify_coordinates.x_coordinate
            self.__actual_y_coordinate = modify_coordinates.y_coordinate

        else:
            if modify_coordinates.x_coordinate != self.__actual_x_coordinate or \
               modify_coordinates.y_coordinate != self.__actual_y_coordinate:

                coordinates = DrawingCoordinates(self.__actual_x_coordinate, self.__actual_y_coordinate,
                                                 modify_coordinates.x_coordinate, modify_coordinates.y_coordinate)

                self.__actual_x_coordinate = modify_coordinates.x_coordinate
                self.__actual_y_coordinate = modify_coordinates.y_coordinate

                self.__update_handler(coordinates, self.__color)


    def reset_values(self):
        self.__actual_x_coordinate = None
        self.__actual_y_coordinate = None
        self.__reset_handler()

    def update_line_color(self, color):
        self.__color = color
