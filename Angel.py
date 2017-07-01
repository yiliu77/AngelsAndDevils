from NeuralNetwork import NeuralNetwork
import numpy as np


class Angel:
    def __init__(self, sides):
        self.sides = sides
        self.position = int(sides / 2) * sides + int(sides / 2)
        # initially in the center
        self.moves = []

        self.escaped = False

        input_nodes = sides ** 2
        hidden_nodes = 200
        output_nodes = 4
        learning_rate = 0.1
        weight_wih = np.random.normal(0.0, pow(hidden_nodes, -0.5), (hidden_nodes, input_nodes))
        weight_who = np.random.normal(0.0, pow(output_nodes, -0.5), (output_nodes, hidden_nodes))
        self.consciousness = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, weight_wih, weight_who,
                                           learning_rate)

    def has_escaped(self):
        return self.escaped

    def get_position(self):
        return self.position

    def get_moves(self):
        return self.moves

    def reset(self):
        self.moves = []
        self.position = int(self.sides / 2) * self.sides + int(self.sides / 2)
        self.escaped = False

    def angel_move(self, all_blocks, move, move_direction):
        self.moves.append(move_direction)
        if (self.position + move) in all_blocks.get_positions():
            return False
        if self.position + move < 0 or self.position + move > self.sides ** 2 - 1:
            self.escaped = True
        if (self.position % self.sides == self.sides - 1 and (self.position + move) % self.sides == 0) or (
                            self.position % self.sides == 0 and (self.position + move) % self.sides == self.sides - 1):
            self.escaped = True
        self.position += move
        return True

    def query(self, board):
        return self.consciousness.query(board)

    def train(self, boards, has_won):
        win_error = 1 if has_won else 0
        for i in range(len(boards)):
            reinforced_error = np.array([None, None, None, None]).reshape(4, 1)
            reinforced_error[self.moves[i], 0] = win_error
            self.consciousness.train(boards[i], reinforced_error)
