
class MainModel():

    def __init__(self):
        pass

    def handle_data(self,data):
        tupla = data.strip(' \n\r').split(',')
        print(tupla)
        x_value = int(tupla[0])
        y_value = int(tupla[1])
        coordinates = (x_value,y_value)
        return coordinates

    def validator_of_data(self,data):
        try:
            tupla_aux = data.strip(' \n\r').split(',')
            x = tupla_aux[0]
            y = tupla_aux [1]
        except Exception as error:
            return False
        else:
            return True





