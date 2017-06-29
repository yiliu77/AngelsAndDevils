import pygame
from pygame.locals import *


class Angel:
    def __init__(self, sides):
        self.sides = sides
        self.position = int(sides / 2) * sides + int(sides / 2)
        self.escaped = False

    def has_escaped(self):
        return self.escaped

    def get_position(self):
        return self.position

    def angel_move(self, all_devils, move):
        for barrier in all_devils.get_positions():
            if barrier == (self.position + move):
                return
        if self.position + move < 0 or self.position + move > self.sides ** 2 - 1:
            self.escaped = True
            return
        if (self.position % self.sides == self.sides - 1 and (self.position + move) % self.sides == 0) or (
                            self.position % self.sides == 0 and (self.position + move) % self.sides == self.sides - 1):
            self.escaped = True
            return
        self.position += move


class Devils:
    def __init__(self):
        self.positions = []

    def get_positions(self):
        return self.positions

    def add_devil(self, angel_position, position):
        if angel_position == position:
            return
        self.positions.append(position)


class Board:
    def __init__(self, margin, sides):
        self.margin = margin
        self.sides = sides
        self.size = self.sides * self.margin

        pygame.init()
        self.window = pygame.display.set_mode((self.size, self.size))
        self.canvas = self.window.copy()
        self.running = True

        self.black = (0, 0, 0, 255)
        self.white = (255, 255, 255)
        self.gray = (220, 220, 220)
        self.silver = (192, 192, 192)
        self.red = (255, 0, 0)

        self.angel = Angel(self.sides)
        self.devils = Devils()

    def rect_equ(self, position):
        return (
            (position % self.sides) * self.margin, int(position / self.sides) * self.margin, self.margin, self.margin)

    def is_running(self):
        return self.running

    def run(self):
        self.window.fill(self.white)
        # grid
        for side in range(0, self.size, self.margin):
            pygame.draw.lines(self.window, self.gray, False, ((side, 0), (side, self.size)))
            pygame.draw.lines(self.window, self.gray, False, ((0, side), (self.size, side)))

        # angel
        if not self.angel.has_escaped():
            # noinspection PyTypeChecker
            pygame.draw.rect(self.window, self.silver, self.rect_equ(self.angel.get_position()))

        # devil barriers
        for devil in self.devils.get_positions():
            pygame.draw.rect(self.window, self.red, (self.rect_equ(devil)))

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x_box = int(pos[0] / self.margin)
                y_box = int(pos[1] / self.margin)
                box_index = x_box + self.sides * y_box
                self.devils.add_devil(self.angel.get_position(), box_index)

            if e.type == pygame.KEYDOWN:
                if e.key == K_RIGHT:
                    self.angel.angel_move(self.devils, 1)
                if e.key == K_LEFT:
                    self.angel.angel_move(self.devils, -1)
                if e.key == K_UP:
                    self.angel.angel_move(self.devils, -self.sides)
                if e.key == K_DOWN:
                    self.angel.angel_move(self.devils, self.sides)
            if e.type == pygame.QUIT:
                self.running = False

        pygame.display.update()


if __name__ == "__main__":
    board = Board(60, 11)
    while board.is_running():
        board.run()
