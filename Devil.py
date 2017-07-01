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

    def place_block(self, angel, all_blocks):
        random_place = random.randrange(0, self.sides ** 2)
        while angel.get_position() == random_place or random_place in all_blocks.get_positions():
            random_place = random.randrange(0, self.sides ** 2)
        return random_place
