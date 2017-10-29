from Views.Button import ColorButton

class ColorMenuView ():
    class Constants:
        colors = ['Red', 'Blue', 'Green', 'Black']
    def __init__(self, master):

        for index_row, key in enumerate(self.Constants.colors):
            button = ColorButton(master, key)
            button.position(index_row+1 , 1)
