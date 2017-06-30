import pygame
from pygame.locals import *
from Angel import Angel
from Devil import Blocks


class Board:
    def __init__(self, margin, sides):
        self.margin = margin
        self.sides = sides
        self.size = self.sides * self.margin

        pygame.init()
        self.window = pygame.display.set_mode((self.size, self.size))
        self.canvas = self.window.copy()

        self.black = (0, 0, 0, 255)
        self.white = (255, 255, 255)
        self.gray = (220, 220, 220)
        self.silver = (192, 192, 192)
        self.red = (255, 0, 0)

        self.angel = Angel(self.sides)
        self.blocks = Blocks()
        self.winner = None

    def machinery(self):
        self.window.fill(self.white)
        if self.angel.has_escaped():
            self.winner = "angel"
        if self.angel.is_trapped(self.blocks):
            self.winner = "devil"
        # grid
        for side in range(0, self.size, self.margin):
            pygame.draw.lines(self.window, self.gray, False, ((side, 0), (side, self.size)))
            pygame.draw.lines(self.window, self.gray, False, ((0, side), (self.size, side)))

        # angel
        pygame.draw.rect(self.window, self.silver, self.rect_equ(self.angel.get_position()))

        # devil barriers
        for devil in self.blocks.get_positions():
            pygame.draw.rect(self.window, self.red, (self.rect_equ(devil)))

    def rect_equ(self, position):
        return (
            (position % self.sides) * self.margin, int(position / self.sides) * self.margin, self.margin, self.margin)

    def representation(self):
        board_rep = []
        for i in range(self.sides ** 2):
            if i == self.angel.get_position():
                board_rep.append(1)
            elif i in self.blocks.get_positions():
                board_rep.append(0.5)
        return board_rep

    def get_angel(self):
        return self.angel

    def get_winner(self):
        return self.winner

    def train_angel(self):
        self.machinery()

        angel.query()
        return True

    def run(self):
        self.machinery()

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x_box = int(pos[0] / self.margin)
                y_box = int(pos[1] / self.margin)
                box_index = x_box + self.sides * y_box
                self.blocks.add_block(self.angel.get_position(), box_index)

            if e.type == pygame.KEYDOWN:
                if e.key == K_RIGHT:
                    move = self.angel.angel_move(self.blocks, 1)
                    if not move:
                        self.winner = "devil"
                if e.key == K_LEFT:
                    move = self.angel.angel_move(self.blocks, -1)
                    if not move:
                        self.winner = "devil"
                if e.key == K_UP:
                    move = self.angel.angel_move(self.blocks, -self.sides)
                    if not move:
                        self.winner = "devil"
                if e.key == K_DOWN:
                    move = self.angel.angel_move(self.blocks, self.sides)
                    if not move:
                        self.winner = "devil"

        pygame.display.update()
