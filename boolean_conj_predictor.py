import os
import sys


def read_trainset(file_path):
    x, y, lines = [], [], []
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for l in lines:
        x.append(l.strip().split(' ')[:-1])
        y.append(l.strip().split(' ')[-1])
    return x, y


def write_to_file(hypothesis):
    output = ','.join(hypothesis)
    with open('output.txt', 'w') as f:
        f.write(output)


def create_init_hypothesis(len):
    h = []
    for i in xrange(len):
        h.append('x{}'.format(i + 1))
        h.append('not(x{})'.format(i + 1))
    return h


def calc_prediction(h, x):
    for index, val in enumerate(x):
        if (int(val) == 1 and h.__contains__('not(x{})'.format(index + 1))) or (int(val) == 0 and h.__contains__('x{}'.format(index + 1))):
            return 0
    return 1


def run_consistency_algorithm(x, y):
    h_t = create_init_hypothesis(x[0].__len__())

    for example, label in zip(x, y):
        y_pred = calc_prediction(h_t, example)
        if int(label) == 1 and y_pred == 0:
            for index, x in enumerate(example):
                if int(x) == 1:
                    if h_t.__contains__('not(x{})'.format(index + 1)):
                        h_t.remove('not(x{})'.format(index + 1))
                if int(x) == 0:
                    if h_t.__contains__('x{}'.format(index + 1)):
                        h_t.remove('x{}'.format(index + 1))
    return h_t


def main():
    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        raise Exception('Input file was not found\n')
    x, y = read_trainset(input_file)
    if len(x) == 0 or len(y) == 0:
        raise Exception('No training data was found')
    hypothesis = run_consistency_algorithm(x, y)
    write_to_file(hypothesis)


if __name__ == '__main__':
    main()
