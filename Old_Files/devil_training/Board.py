import pygame
from Old_Files.devil_training.Angel import Angel
from pygame.locals import *

from Old_Files.devil_training.Devil import Devil


class Board:
    def __init__(self, margin, sides, display=True):
        self.margin = margin
        self.sides = sides
        self.side_length = self.sides * self.margin

        self.display = display
        if display:
            pygame.init()
            self.window = pygame.display.set_mode((self.side_length, self.side_length))
            self.canvas = self.window.copy()

            self.black = (0, 0, 0, 255)
            self.white = (255, 255, 255)
            self.gray = (220, 220, 220)
            self.silver = (192, 192, 192)
            self.red = (255, 0, 0)

        self.angel = Angel(self.sides)
        self.devil = Devil(self.sides)
        self.winner = None
        self.reason = None

    def reset(self):
        self.angel.reset()
        self.devil.reset()
        self.winner = None

    def representation(self):
        board_rep = []
        for i in range(self.sides ** 2):
            if i == self.angel.get_position():
                board_rep.append(0.5)
            elif i in self.devil.get_blocks():
                board_rep.append(0.99)
            else:
                board_rep.append(0.0)
        return board_rep

    def get_reason(self):
        return self.reason

    def check_winner(self, current_player):
        if current_player == "angel":
            if self.angel.get_position() in self.devil.get_blocks():
                self.winner = "devil"
                self.reason = "move into devil block"
            elif self.angel.get_last_move() == 3 and self.angel.get_position() % self.sides == self.sides - 1:
                self.winner = "angel"
                self.reason = "angel escaped"
            elif self.angel.get_last_move() == 1 and self.angel.get_position() % self.sides == 0:
                self.winner = "angel"
                self.reason = "angel escaped"
            elif self.angel.get_position() < 0 or self.angel.get_position() > self.sides ** 2 - 1:
                self.winner = "angel"
                self.reason = "angel escaped"
        if current_player == "devil":
            if self.angel.get_position() in self.devil.get_blocks():
                self.winner = "angel"
                self.reason = "place on angel"
            if len(self.devil.get_blocks()) != len(set(self.devil.get_blocks())):
                self.winner = "angel"
                self.reason = "repeat place"


    def players_play(self):
        self.window.fill(self.white)

        # grid
        for side in range(0, self.side_length, self.margin):
            pygame.draw.lines(self.window, self.gray, False, ((side, 0), (side, self.side_length)))
            pygame.draw.lines(self.window, self.gray, False, ((0, side), (self.side_length, side)))

        # angel
        if self.winner is None:
            pygame.draw.rect(self.window, self.silver, self.rect_equ(self.angel.get_position()))

        # devil barriers
        for devil in self.devil.get_blocks():
            pygame.draw.rect(self.window, self.red, (self.rect_equ(devil)))

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x_box = int(pos[0] / self.margin)
                y_box = int(pos[1] / self.margin)
                box_index = x_box + self.sides * y_box
                self.devil.god_place(box_index)

            if e.type == pygame.KEYDOWN:
                if e.key == K_RIGHT:
                    self.angel.god_move(1)
                if e.key == K_LEFT:
                    self.angel.god_move(-1)
                if e.key == K_UP:
                    self.angel.god_move(-self.sides)
                if e.key == K_DOWN:
                    self.angel.god_move(self.sides)
        self.check_winner("angel")
        pygame.display.update()

    def angels_turn(self):
        self.angel.angel_move(self.representation(), self.devil.get_blocks())
        self.check_winner("angel")

    def dumb_angels_turn(self):
        self.angel.angel_dumb(self.representation(), self.devil.get_blocks())
        self.check_winner("angel")

    def devils_turn(self):
        self.devil.place_block(self.representation(), self.angel.get_position())
        self.check_winner("devil")

    def train_devil(self):
        self.devil.train(self.winner)

    def get_winner(self):
        return self.winner

    # TODO Remove
    def get_angel(self):
        return self.angel

    def get_devil(self):
        return self.devil

    def rect_equ(self, position):
        return (
            (position % self.sides) * self.margin, int(position / self.sides) * self.margin, self.margin,
            self.margin)

    def init_draw(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.side_length, self.side_length))
        self.canvas = self.window.copy()


        self.black = (0, 0, 0, 255)
        self.white = (255, 255, 255)
        self.gray = (220, 220, 220)
        self.silver = (192, 192, 192)
        self.red = (255, 0, 0)

    def display_board(self):
        self.window.fill(self.white)

        # grid
        for side in range(0, self.side_length, self.margin):
            pygame.draw.lines(self.window, self.gray, False, ((side, 0), (side, self.side_length)))
            pygame.draw.lines(self.window, self.gray, False, ((0, side), (self.side_length, side)))

        # angel
        if self.winner is None:
            pygame.draw.rect(self.window, self.silver, self.rect_equ(self.angel.get_position()))

        # devil barriers
        for devil in self.devil.get_blocks():
            pygame.draw.rect(self.window, self.red, (self.rect_equ(devil)))

        pygame.display.update()

