import random


class Devil:
    def __init__(self, sides):
        # self.blocks = [39, 43, 31,32,80,76,75,74,45]
        self.blocks = []
        self.sides = sides

    def get_blocks(self):
        return self.blocks

    def reset(self):
        self.blocks = []

    def god_place(self, place):
        self.blocks.append(place)

    def place_block(self, angel_pos):
        random_dir = random.randrange(0, 4)
        random_place = -1
        while random_place < 0 or random_place >= self.sides ** 2:
            if random_dir == 0:
                random_place = angel_pos - self.sides
            if random_dir == 1:
                random_place = angel_pos + 1
            if random_dir == 2:
                random_place = angel_pos + self.sides
            if random_dir == 3:
                random_place = angel_pos - 1
            random_dir = random.randrange(0, 4)
        self.blocks.append(random_place)
        return
