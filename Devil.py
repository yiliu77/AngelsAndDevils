import random


class Blocks:
    def __init__(self):
        self.positions = []

    def get_positions(self):
        return self.positions

    def add_block(self, angel_position, position):
        if angel_position == position:
            return
        self.positions.append(position)


class Devil:
    def __init__(self, sides):
        self.blocks = Blocks()
        self.sides = sides

    def place_block(self, angel):
        random_place = random.randrange(0, self.sides ** 2)
