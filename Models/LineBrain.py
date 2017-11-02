class LineBrain():
    def __init__(self):
        self.new_horizontal_value = 0
        self.new_vertical_value = 0

    def updating(self, new_x_value, new_y_value):
        try:
            if new_x_value != self.new_vertical_value or new_y_value != self.new_horizontal_value:

                self.last__horizontalvalue = new_y_value
                self.last_verticalvalue = new_x_value

                new_cordinates = self.new_vertical_value,self.new_horizontal_value ,self.last_verticalvalue, self.last__horizontalvalue
                self.new_vertical_value = new_x_value
                self.new_horizontal_value = new_y_value


            return new_cordinates
        except:
            return
