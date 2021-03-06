import numpy as np
from Old_Files.devil_training.NeuralNetwork import NeuralNetwork


class Devil:
    def __init__(self, sides):
        self.blocks = []
        self.sides = sides

        input_nodes = int(sides ** 2)
        hidden_nodes = 160
        output_nodes = int(sides ** 2)
        learning_rate = 0.2
        weight_wih = np.random.randn(hidden_nodes,
                                     int(input_nodes)) \
                     / np.sqrt(input_nodes)
        weight_who = np.random.randn(output_nodes, hidden_nodes) / np.sqrt(hidden_nodes)
        self.consciousness = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, weight_wih, weight_who,
                                           learning_rate, sides)

    def get_blocks(self):
        return self.blocks

    def reset(self):
        self.blocks = []
        self.consciousness.reset()

    def god_place(self, place):
        self.blocks.append(place)

    def place_block(self, board, angel_pos):
        turn = np.argmax(self.consciousness.query(board, angel_pos))
        self.blocks.append(turn)
        return

    def train(self, has_won):
        if has_won is "devil":
            self.consciousness.train(True)
        if has_won is "angel":
            self.consciousness.train(False)

    def get_wih(self):
        return self.consciousness.wih

    def get_who(self):
        return self.consciousness.who
