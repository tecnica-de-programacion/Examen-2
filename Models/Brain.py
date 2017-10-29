class MainModel():
    def __init__(self):
        pass
    def handle_data(self, data):
        new_coordinates = data.strip('\n\r').split(',')
        print(new_coordinates)
        coordinates = (int(new_coordinates[0]),int(new_coordinates[1]))
        return coordinates

