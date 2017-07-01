import pygame
from pygame.locals import *
from Angel import Angel
from Devil import Blocks
from Devil import Devil
import numpy as np


class Board:
    def __init__(self, margin, sides, display=True):
        self.margin = margin
        self.sides = sides
        self.size = self.sides * self.margin

        self.display = display
        if display:
            pygame.init()
            self.window = pygame.display.set_mode((self.size, self.size))
            self.canvas = self.window.copy()

            self.black = (0, 0, 0, 255)
            self.white = (255, 255, 255)
            self.gray = (220, 220, 220)
            self.silver = (192, 192, 192)
            self.red = (255, 0, 0)

        self.angel = Angel(self.sides)
        self.devil = Devil(self.sides)
        self.blocks = Blocks()
        self.winner = None

        self.board_pos = [self.representation()]

    def get_angel(self):
        return self.angel

    def get_blocks(self):
        return self.blocks.get_positions()

    def get_winner(self):
        return self.winner

    def get_board_positions(self):
        return self.board_pos

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
            else:
                board_rep.append(0)
        return board_rep

    # def train_angel(self):
    #     self.machinery()
    #
    #     angel.query()
    #     return True

    def machinery(self):
        if self.angel.has_escaped():
            self.winner = "angel"

        if self.display:
            self.window.fill(self.white)
            # grid
            for side in range(0, self.size, self.margin):
                pygame.draw.lines(self.window, self.gray, False, ((side, 0), (side, self.size)))
                pygame.draw.lines(self.window, self.gray, False, ((0, side), (self.size, side)))

            # angel
            if self.winner is None:
                pygame.draw.rect(self.window, self.silver, self.rect_equ(self.angel.get_position()))

            # devil barriers
            for devil in self.blocks.get_positions():
                pygame.draw.rect(self.window, self.red, (self.rect_equ(devil)))

    def players_play(self):
        self.machinery()

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x_box = int(pos[0] / self.margin)
                y_box = int(pos[1] / self.margin)
                box_index = x_box + self.sides * y_box
                self.blocks.add_block(self.angel.get_position(), box_index)

            if e.type == pygame.KEYDOWN:
                move = True
                if e.key == K_RIGHT:
                    move = self.angel.angel_move(self.blocks, 1, 1)
                if e.key == K_LEFT:
                    move = self.angel.angel_move(self.blocks, -1, 3)
                if e.key == K_UP:
                    move = self.angel.angel_move(self.blocks, -self.sides, 0)
                if e.key == K_DOWN:
                    move = self.angel.angel_move(self.blocks, self.sides, 2)
                if not move:
                    self.winner = "devil"
        pygame.display.update()

    def angels_turn(self):
        self.machinery()

        turn = self.angel.query(self.representation())
        move = 0
        if np.argmax(turn) == 0:
            move = -self.sides
        if np.argmax(turn) == 1:
            move = 1
        if np.argmax(turn) == 2:
            move = self.sides
        if np.argmax(turn) == 3:
            move = -1
        move = self.angel.angel_move(self.blocks, move, np.argmax(turn))
        if not move:
            self.winner = "devil"
        self.board_pos.append(self.representation())

    def train_angel(self, winner):
        self.angel.train(self.board_pos, winner)

    def devils_turn(self):
        block_pos = self.devil.place_block(self.angel, self.blocks)
        self.blocks.add_block(self.angel, block_pos)
        return block_pos
