from NeuralNetwork import NeuralNetwork
import numpy as np
import random


class Devil:
    def __init__(self, sides, trained):
        self.blocks = []
        self.sides = sides

        self.identity = np.arange(self.sides ** 2).reshape(self.sides, self.sides)

        input_nodes = int(sides ** 2)
        hidden_nodes = 160
        output_nodes = int(sides ** 2)
        learning_rate = 0.2

        if not trained:
            weight_wih = np.random.randn(hidden_nodes, int(input_nodes)) / np.sqrt(input_nodes)
            weight_who = np.random.randn(output_nodes, hidden_nodes) / np.sqrt(hidden_nodes)
        else:
            devil_who = open("Files/devil_who.csv", 'r')
            devil_who_read = devil_who.readlines()
            devil_who.close()
            devil_wih = open("Files/devil_wih.csv", 'r')
            devil_wih_read = devil_wih.readlines()
            devil_wih.close()

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

    def random_place_block(self, angel_pos):
        random_dir = random.randrange(0, 8)
        random_place = -1

        # check_layer = self.check_on_out_layer(angel_pos)
        # new_devil_pos = (angel_pos + check_layer)
        # if not check_layer == 0 and 0 <= new_devil_pos < self.sides ** 2 \
        #         and new_devil_pos not in self.blocks:
        #     self.blocks.append(new_devil_pos)
        #     return

        # for pos in self.determine_quad(angel_pos):
        #     if (angel_pos + pos) >= 0 and (angel_pos + pos) < self.sides ** 2 and (angel_pos + pos) \
        #       not in self.blocks:
        #         self.blocks.append(angel_pos + pos)
        #         print(str(angel_pos) + " " + str(self.blocks))
        #         return

        while random_place < 0 or random_place >= self.sides ** 2:
            if random_dir == 0:
                random_place = angel_pos - self.sides
            if random_dir == 1:
                random_place = angel_pos + 1
            if random_dir == 2:
                random_place = angel_pos + self.sides
            if random_dir == 3:
                random_place = angel_pos - 1
            if random_dir == 4:
                random_place = angel_pos - self.sides - 1
            if random_dir == 5:
                random_place = angel_pos + self.sides - 1
            if random_dir == 6:
                random_place = angel_pos - self.sides + 1
            if random_dir == 7:
                random_place = angel_pos + self.sides + 1
            random_dir = random.randrange(0, 4)
        self.blocks.append(random_place)
        return

    def check_on_out_layer(self, angel_pos):
        if (angel_pos - 1) % self.sides == 0:
            return -1
        elif (angel_pos + 1) % self.sides == self.sides - 2:
            return 1
        elif self.sides + 1 <= (angel_pos - self.sides) <= 2 * self.sides - 2:
            return -self.sides
        elif self.sides ** 2 - 2 * self.sides + 1 <= (angel_pos + self.sides) <= self.sides ** 2 - self.sides - 2:
            return self.sides
        return 0

        # def determine_quad(self, angel_pos):
        #     if angel_pos in self.identity[:int(self.sides / 2), :int(self.sides / 2)]:
        #         return [-1, -self.sides]
        #     elif angel_pos in self.identity[int(self.sides / 2):self.sides, :int(self.sides / 2)]:
        #         return [self.sides, -1]
        #     elif angel_pos in self.identity[:int(self.sides / 2), int(self.sides / 2):self.sides]:
        #         return [-self.sides, 1]
        #     else:
        #         return [1, self.sides]
