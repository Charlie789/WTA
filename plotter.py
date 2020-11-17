import matplotlib.pyplot as plt
import init_generator as gen


def draw_plot(series):
    plt.plot(series['init']['x'], series['init']['y'], 'bs')
    plt.plot(series['teaching_vectors']['x'], series['teaching_vectors']['y'], 'rs')
    plt.ylabel('some numbers')
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


if __name__ == '__main__':
    series = {}
    init_neurons = gen.generate_neurons(10)
    teaching_vectors = gen.generate_swarms(10)
    series['init'] = neuron_to_series(init_neurons)
    series['teaching_vectors'] = points_to_series(teaching_vectors)
    draw_plot(series)
