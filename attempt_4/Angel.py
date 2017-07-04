import numpy as np

from attempt_4.NeuralNetwork import NeuralNetwork


class Angel:
    def __init__(self, sides):
        self.sides = sides
        self.position = int(sides / 2) * sides + int(sides / 2)
        self.moves = []

        input_nodes = int(sides ** 2)
        hidden_nodes = 140
        output_nodes = 1
        learning_rate = 0.1
        weight_wih = np.random.randn(hidden_nodes, int(input_nodes)) / np.sqrt(input_nodes)
        weight_who = np.random.randn(output_nodes, hidden_nodes) / np.sqrt(hidden_nodes)
        self.left = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, weight_wih, weight_who,
                                  learning_rate)

        weight_wih = np.random.randn(hidden_nodes, int(input_nodes)) / np.sqrt(input_nodes)
        weight_who = np.random.randn(output_nodes, hidden_nodes) / np.sqrt(hidden_nodes)
        self.right = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, weight_wih, weight_who,
                                   learning_rate)

        weight_wih = np.random.randn(hidden_nodes, int(input_nodes)) / np.sqrt(input_nodes)
        weight_who = np.random.randn(output_nodes, hidden_nodes) / np.sqrt(hidden_nodes)
        self.up = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, weight_wih, weight_who,
                                learning_rate)

        weight_wih = np.random.randn(hidden_nodes, int(input_nodes)) / np.sqrt(input_nodes)
        weight_who = np.random.randn(output_nodes, hidden_nodes) / np.sqrt(hidden_nodes)
        self.down = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, weight_wih, weight_who,
                                  learning_rate)

    def get_last_move(self):
        if not len(self.moves) == 0:
            return self.moves[len(self.moves) - 1]

    def get_position(self):
        return self.position

    def reset(self):
        self.position = int(self.sides / 2) * self.sides + int(self.sides / 2)
        self.moves = []
        self.left.reset()
        self.up.reset()
        self.right.reset()
        self.down.reset()

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

    # only for AI mode
    def angel_move(self, board):
        turn0 = self.up.query(board)
        turn1 = self.right.query(board)
        turn2 = self.down.query(board)
        turn3 = self.left.query(board)
        selection = np.argmax([turn0, turn1, turn2, turn3])

        if np.argmax(selection) == 0:
            self.up.save(board)
            self.position += -self.sides
        if np.argmax(selection) == 1:
            self.right.save(board)
            self.position += 1
        if np.argmax(selection) == 2:
            self.down.save(board)
            self.position += self.sides
        if np.argmax(selection) == 3:
            self.left.save(board)
            self.position += -1
        self.moves.append(selection)

    # train angel
    def train(self, has_won):
        if has_won is "devil":
            self.up.train(False)
            self.left.train(False)
            self.down.train(False)
            self.right.train(False)
        if has_won is "angel":
            self.up.train(True)
            self.left.train(True)
            self.down.train(True)
            self.right.train(True)
