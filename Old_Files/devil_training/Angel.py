import random


class Angel:
    def __init__(self, sides):
        self.sides = sides
        self.position = int(sides / 2) * sides + int(sides / 2)
        self.moves = []

    def get_last_move(self):
        if not len(self.moves) == 0:
            return self.moves[len(self.moves) - 1]

    def get_position(self):
        return self.position

    def reset(self):
        self.position = int(self.sides / 2) * self.sides + int(self.sides / 2)
        self.moves = []

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
    def angel_move(self, board, devils):
        turn = random.randrange(0, 4)
        if turn == 0 and self.position - self.sides not in devils:
            self.position += -self.sides
        elif turn == 1 and self.position + 1 not in devils:
            self.position += 1
        elif turn == 2 and self.position + self.sides not in devils:
            self.position += self.sides
        elif turn == 3 and self.position - 1 not in devils:
            self.position += -1
        else:
            self.position += -self.sides
        self.moves.append(turn)

    def angel_dumb(self, board, devils):
        turn = random.randrange(0, 4)
        if turn == 0:
            self.position += -self.sides
        elif turn == 1:
            self.position += 1
        elif turn == 2:
            self.position += self.sides
        elif turn == 3:
            self.position += -1
        self.moves.append(turn)
