
class HandleData():

    def clean_data(self, data_arduino):
        data = data_arduino.strip(' \n\r').split(",")
        return data
