from point import Point


class Neuron:
    def __init__(self, x, y):
        self.point = Point(x, y)

    def calculate_d(self, x, y):
        return pow(self.point.x - x, 2) + pow(self.point.y - y, 2)
