import csv


n = 0.5
weights_matrix = []
teaching_vectors = []


def read_teaching_vectors(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader, None)
        for row in reader:
            teaching_vectors.append([float(value) for value in row])

    print("Teaching vector:")
    print(teaching_vectors)


def read_weights(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            weights_matrix.append([float(value) for value in row])

    print("Initialized weights:")
    print(weights_matrix)


def count_min_d(teaching_vector):
    d = []
    for weights in weights_matrix:
        sum = 0
        for num, value in enumerate(weights):
            sum += pow(float(teaching_vector[int(num)]) - float(value), 2)
        d.append(sum)
    return d.index(min(d))


def recalculate_weights(neuron_index, iteration):
    for i, value in enumerate(weights_matrix[neuron_index]):
        new_weight = value + n * (teaching_vectors[iteration][i] - value)
        weights_matrix[neuron_index][i] = new_weight


if __name__ == '__main__':
    read_teaching_vectors('lab1_teaching_vectors.csv')
    read_weights('lab1_weights.csv')

    for iteration in range(0, len(teaching_vectors)):
        min_d = count_min_d(teaching_vectors[iteration])
        recalculate_weights(min_d, iteration)
        print("Weights after {} iteration:".format(iteration))
        print(weights_matrix)
