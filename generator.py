import sys
import numpy as np


def test_hyp(hypothesis, instance):
    # This function performs a functional XNOR (Not + XOR)
    # If the hypothesis is ever 0 (not) and the input is 1 -> returns 0 -> False
    # Similarly, if the hypothesis is 1 (value) and the input is 0 -> returns 0
    for index, hyp_val in hypothesis.iteritems():
        x_instance = instance[abs(index) - 1]
        if hyp_val != x_instance:
            return 0
    return 1


num_examples = 1000
num_variables = 5
correct = 1,-2,-3,-4,5
hyp_form = {int(x): (0 if int(x) < 0 else 1) for x in correct}

with open('test-data2.txt', 'w') as outfile:
    for i in range(num_examples):
        train = np.random.randint(2, size=num_variables, dtype=int)
        classify = test_hyp(hyp_form, train)
        train = np.append(train, classify)
        print np.array_str(train)[1:-1]
        outfile.write(np.array_str(train)[1:-1] + '\n')