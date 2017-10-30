from Views.Button import ColorButton

class ColorMenuView ():
    class Constants:
        colors = ['red', 'blue', 'green', 'black']
    def __init__(self, master):
        self.color = "black"

        for index_row, key in enumerate(self.Constants.colors):
            button = ColorButton(master, key, action = self.__did_tap)
            button.position(index_row+1 , 1)

    def __did_tap(self, sender):
        self.color = sender






