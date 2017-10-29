from Views.ButtonPrototype import ButtonPrototype

class KeypadView():

    def __init__(self, master):
        black_button = ButtonPrototype(master, "Black", "#000000")
        black_button.position(3, 0)
        red_button = ButtonPrototype(master, "Red", "#FF0000")
        red_button.position(3, 1)
        green_button = ButtonPrototype(master, "Green", "#138D75")
        green_button.position(3, 2)
        blue_button = ButtonPrototype(master, "Blue", "#2980B9")
        blue_button.position(3, 3)
