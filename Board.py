import pygame
from pygame.locals import *

margin = 60
sides = 11
size = sides * margin

pygame.init()
window = pygame.display.set_mode((size, size))
canvas = window.copy()

angel = int(sides / 2) * sides + int(sides / 2)
devils = []

black = (0, 0, 0, 255)
white = (255, 255, 255)
gray = (220, 220, 220)
silver = (192, 192, 192)
red = (255, 0, 0)


def rect_equ(index):
    coord_y = int(index / sides) * margin
    coord_x = (index % sides) * margin
    return coord_x, coord_y, margin, margin


def angel_move(angel, move):
    for barrier in devils:
        if barrier == (angel + move):
            return angel
    return angel + move


running = True
while running:
    window.fill(white)
    # grid
    for side in range(0, size, margin):
        pygame.draw.lines(window, gray, False, ((side, 0), (side, size)))
        pygame.draw.lines(window, gray, False, ((0, side), (size, side)))

    # angel
    pygame.draw.rect(window, silver, (rect_equ(angel)))

    # devil barriers
    for barrier in devils:
        pygame.draw.rect(window, red, (rect_equ(barrier)))

    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x_box = int(pos[0] / margin)
            y_box = int(pos[1] / margin)
            index = x_box + sides * y_box
            devils.append(index)

        if e.type == pygame.KEYDOWN:
            if e.key == K_RIGHT:
                angel = angel_move(angel, 1)
            if e.key == K_LEFT:
                angel = angel_move(angel, -1)
            if e.key == K_UP:
                angel = angel_move(angel, -sides)
            if e.key == K_DOWN:
                angel = angel_move(angel, sides)
        if e.type == pygame.QUIT:
            running = False

    pygame.display.update()
