import numpy as np
import scipy.special


class NeuralNetwork:
    def __init__(self, input_node, hidden_node, output_node, initial_wih, initial_who, learn_rate):
        self.i_nodes = input_node
        self.h_nodes = hidden_node
        self.o_nodes = output_node

        self.wih = initial_wih
        self.who = initial_who

        self.lr = learn_rate
        self.sigmoid = lambda x: scipy.special.expit(x)

        self.inputs = []
        self.hidden_outputs = []
        self.final_outputs = []

    def reset(self):
        self.inputs = []
        self.hidden_outputs = []
        self.final_outputs = []

    def train(self, has_won):
        who_update = np.zeros_like(self.who)
        wih_update = np.zeros_like(self.wih)
        for k in range(len(self.inputs)):
            move = np.argmax(self.final_outputs[k])

            target_array = self.final_outputs[k]
            target_array[move] = 0.99 if has_won else 0.01

            output_errors = target_array - self.final_outputs[k]
            hidden_errors = np.dot(self.who.T, output_errors)

            # error1 = (output_errors * final_outputs *
            #                        (1.0 - final_outputs)) * numpy.transpose(hidden_outputs)
            # error2 = numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
            #                                 numpy.transpose(input_array))
            who_update += self.lr * (output_errors * self.final_outputs[k] *
                                     (1.0 - self.final_outputs[k])) * np.transpose(self.hidden_outputs[k])
            wih_update += self.lr * np.dot((hidden_errors * self.hidden_outputs[k] * (1.0 - self.hidden_outputs[k])),
                                           np.transpose(self.inputs[k]))
        self.who += who_update
        self.wih += wih_update
        pass

    def query(self, input_list):
        input_list = np.array(input_list, ndmin=2).T
        self.inputs.append(input_list)

        hidden_inputs = np.dot(self.wih, input_list)
        hidden_outputs = self.sigmoid(hidden_inputs)
        self.hidden_outputs.append(hidden_outputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.sigmoid(final_inputs)
        self.final_outputs.append(final_outputs)

        return final_outputs

    def return_wih(self):
        return self.wih

    def return_who(self):
        return self.who
