import numpy
import scipy.special


class NeuralNetwork:
    def __init__(self, input_node, hidden_node, output_node, initial_wih, initial_who, learn_rate):
        self.i_nodes = input_node
        self.h_nodes = hidden_node
        self.o_nodes = output_node

        self.wih = initial_wih
        self.who = initial_who

        self.lr = learn_rate
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train(self, inputs_list, targets_list):
        input_array = numpy.array(inputs_list, ndmin=2).T
        target_array = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, input_array)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        for i in range(self.o_nodes):
            if target_array[i] is None:
                target_array[i] = final_outputs[i]
        output_errors = target_array - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)

        self.who += self.lr * (output_errors * final_outputs * (1.0 - final_outputs)) * numpy.transpose(hidden_outputs)
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(input_array))
        pass

    def query(self, input_list):
        input_list = numpy.array(input_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, input_list)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

    def return_wih(self):
        return self.wih

    def return_who(self):
        return self.who
