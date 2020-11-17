from random import uniform
from neuron import Neuron
from point import Point


def generate_neurons(quantity: int):
    neurons = []
    for i in range(0, quantity):
        neurons.append(Neuron(uniform(0, 10), uniform(0, 10)))

    return neurons


def generate_swarms(quantity: int):
    points = []
    for i in range(0, quantity):
        center = Point(uniform(0, 10), uniform(0, 10))
        for j in range(0, quantity):
            points.append(Point(center.x + uniform(-0.5, 0.5),
                                center.y + uniform(-0.5, 0.5)))

    return points
