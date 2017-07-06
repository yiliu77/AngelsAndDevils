import numpy as np

from NeuralNetwork import NeuralNetwork


class Angel:
    def __init__(self, sides, trained=False):
        self.sides = sides
        self.position = int(sides / 2) * sides + int(sides / 2)
        self.moves = []

        input_nodes = int(sides ** 2)
        hidden_nodes = 140
        output_nodes = 4
        learning_rate = 0.2

        if not trained:
            weight_wih = np.random.randn(hidden_nodes, int(input_nodes)) / np.sqrt(input_nodes)
            weight_who = np.random.randn(output_nodes, hidden_nodes) / np.sqrt(hidden_nodes)
        else:
            angel_who = open("Files/angel_who.csv", 'r')
            angel_who_read = angel_who.readlines()
            angel_who.close()
            angel_wih = open("Files/angel_wih.csv", 'r')
            angel_wih_read = angel_wih.readlines()
            angel_wih.close()

            weight_wih = np.asfarray([line.split(',') for line in angel_wih_read])
            weight_who = np.asfarray([line.split(',') for line in angel_who_read])

        self.consciousness = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, weight_wih, weight_who,
                                           learning_rate)

    def get_last_move(self):
        if not len(self.moves) == 0:
            return self.moves[len(self.moves) - 1]

    def get_position(self):
        return self.position

    def reset(self):
        self.position = int(self.sides / 2) * self.sides + int(self.sides / 2)
        self.moves = []
        self.consciousness.reset()

    # only for AI mode
    def angel_move(self, board):
        turn = np.argmax(self.consciousness.query(board))
        if turn == 0:
            self.position += -self.sides
        if turn == 1:
            self.position += 1
        if turn == 2:
            self.position += self.sides
        if turn == 3:
            self.position += -1
        self.moves.append(turn)

    # train angel
    def train(self, has_won):
        if has_won is "devil":
            self.consciousness.train(False)
        if has_won is "angel":
            self.consciousness.train(True)

    # only for player mode
    def god_move(self, move):
        if move == -self.sides:
            self.moves.append(0)
        if move == 1:
            self.moves.append(1)
        if move == self.sides:
            self.moves.append(2)
        if move == -1:
            self.moves.append(3)
        self.position += move

    def get_wih(self):
        return self.consciousness.wih

    def get_who(self):
        return self.consciousness.who