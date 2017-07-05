from NeuralNetwork import NeuralNetwork
import numpy as np


class Devil:
    def __init__(self, sides):
        self.blocks = []
        self.sides = sides

        input_nodes = int(sides ** 2)
        hidden_nodes = 160
        output_nodes = int(sides ** 2)
        learning_rate = 0.2

        devil_who = open("Files/devil_who.csv", 'r')
        devil_who_read = devil_who.readlines()
        devil_who.close()

        devil_wih = open("Files/devil_wih.csv", 'r')
        devil_wih_read = devil_wih.readlines()
        devil_wih.close()

        # weight_wih = np.random.randn(hidden_nodes,
        #                              int(input_nodes)) \
        #              / np.sqrt(input_nodes)
        # weight_who = np.random.randn(output_nodes, hidden_nodes) / np.sqrt(hidden_nodes)
        weight_wih = np.asfarray([line.split(',') for line in devil_wih_read])
        weight_who = np.asfarray([line.split(',') for line in devil_who_read])
        self.consciousness = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, weight_wih, weight_who,
                                           learning_rate)

    def get_blocks(self):
        return self.blocks

    def reset(self):
        self.blocks = []

    def god_place(self, place):
        self.blocks.append(place)

    def place_block(self, board):
        turn = np.argmax(self.consciousness.query(board))
        self.blocks.append(turn)
        return

    def train(self, has_won):
        if has_won is "devil":
            self.consciousness.train(True)
        if has_won is "angel":
            self.consciousness.train(False)
        self.consciousness.reset()

    def get_wih(self):
        return self.consciousness.wih

    def get_who(self):
        return self.consciousness.who
