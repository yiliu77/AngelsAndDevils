import random

class Devil:
    def __init__(self, sides):
        self.blocks = []
        self.sides = sides

    def get_blocks(self):
        return self.blocks

    def reset(self):
        self.blocks = []

    def god_place(self, place):
        self.blocks.append(place)

    def place_block(self, angel_pos):
        random_place = random.randrange(0, self.sides ** 2)
        while angel_pos == random_place or random_place in self.blocks:
            random_place = random.randrange(0, self.sides ** 2)
        self.blocks.append(random_place)
