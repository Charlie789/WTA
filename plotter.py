import matplotlib.pyplot as plt
import init_generator as gen
from random import randrange
from math import inf


def draw_plot():
    plt.plot(series['teaching_vectors']['x'], series['teaching_vectors']['y'], 'rs')
    plt.plot(series['init']['x'], series['init']['y'], 'bs')
    plt.plot(series['final']['x'], series['final']['y'], 'gs')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.show()


def neuron_to_series(neurons):
    serie = {'x': [], 'y': []}
    for neuron in neurons:
        serie['x'].append(neuron.point.x)
        serie['y'].append(neuron.point.y)

    return serie


def points_to_series(points):
    serie = {'x': [], 'y': []}
    for point in points:
        serie['x'].append(point.x)
        serie['y'].append(point.y)

    return serie


def recalculate_weights(neuron_id, teaching_vector):
    init_neurons[neuron_id].point.x = recalculate_weight(init_neurons[neuron_id].point.x, teaching_vector.x)
    init_neurons[neuron_id].point.y = recalculate_weight(init_neurons[neuron_id].point.y, teaching_vector.y)


def recalculate_weight(old_weight, teaching_value):
    return old_weight + 0.5 * (teaching_value - old_weight)


if __name__ == '__main__':
    series = {}
    init_neurons = gen.generate_neurons(10)
    teaching_vectors = gen.generate_swarms(10)
    series['init'] = neuron_to_series(init_neurons)
    series['teaching_vectors'] = points_to_series(teaching_vectors)

    for i in range(0, 100):
        rand_vector_id = randrange(0, len(teaching_vectors))
        print('vector_id = {}, x = {}, y = {}'.format(rand_vector_id, teaching_vectors[rand_vector_id].x, teaching_vectors[rand_vector_id].y))
        min_d = inf
        min_d_id = -1
        for neuron_id, neuron in enumerate(init_neurons):
            value = neuron.calculate_d(teaching_vectors[rand_vector_id].x, teaching_vectors[rand_vector_id].y)
            print(value)
            if min_d > value:
                min_d = value
                min_d_id = neuron_id
                print('new min_d = {}, id = {}'.format(min_d, min_d_id))

        recalculate_weights(min_d_id, teaching_vectors[rand_vector_id])
    series['final'] = neuron_to_series(init_neurons)
    draw_plot()
