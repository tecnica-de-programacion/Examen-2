class MainModel():
    def __init__(self):
        pass

    def handle_data(self, data):
        new_coordinates = data.strip('\n\r').split(',')
        print(new_coordinates)
        coordinates = (int(new_coordinates[0]),int(new_coordinates[1]))
        return coordinates

    def validator_data(self, data):
        for i in range(0,5):
            try:
                datas = data.strip('\n\r').split(',')
                x = datas[0]
                y = datas[1]
            except Exception as error:
                print('error')
            else:
                return data