class DataHandler():

    def clean_data(self, arduino):
        data = arduino.strip(' \n\r').split(",")
        return data