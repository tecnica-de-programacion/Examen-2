class InteractiveCanvasBrain():
    class Constants:
        canvas_heigth = 500
        canvas_width = 600

    def __init__(self):
        self.state = True

    def get_coordinates(self, new_x_value, new_y_value):
        if self.state:
            self.last_x_value = new_x_value
            self.last_y_value = new_y_value
            self.state = False
        composed_coordinates = self.last_x_value, self.last_y_value, new_x_value, new_y_value
        self.last_x_value = new_x_value
        self.last_y_value = new_y_value
        return composed_coordinates