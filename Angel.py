from NeuralNetwork import NeuralNetwork
import numpy as np


class Angel:
    def __init__(self, sides):
        self.sides = sides
        self.position = int(sides / 2) * sides + int(sides / 2)
        self.moves = []
        self.board_pos = []

        input_nodes = sides ** 2
        hidden_nodes = 200
        output_nodes = 4
        learning_rate = 0.1
        weight_wih = np.random.normal(0.0, pow(hidden_nodes, -0.5), (hidden_nodes, input_nodes))
        weight_who = np.random.normal(0.0, pow(output_nodes, -0.5), (output_nodes, hidden_nodes))
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
        self.board_pos = []

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

    def angel_move(self, board):
        self.board_pos.append(board)

        turn = np.argmax(self.consciousness.query(board))
        if np.argmax(turn) == 0:
            self.position = -self.sides
        if np.argmax(turn) == 1:
            self.position = 1
        if np.argmax(turn) == 2:
            self.position = self.sides
        if np.argmax(turn) == 3:
            self.position = -1
        self.moves.append(turn)


    def train(self, has_won):
        win_error = 1 if has_won else 0
        for i in range(len(self.board_pos)):
            reinforced_error = np.array([None, None, None, None]).reshape(4, 1)
            reinforced_error[self.moves[i], 0] = win_error
            self.consciousness.train(self.board_pos[i], reinforced_error)
