#polygon exercise 

class Polygon: 
    def __init__(self, no_of_sides):
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = ...