import pygame
from pygame.locals import *

margin = 60
sides = 11
size = sides * margin

pygame.init()
window = pygame.display.set_mode((size, size))
canvas = window.copy()

angel =  int(sides / 2) * sides + int(sides / 2)
devils = []

black = (0, 0, 0, 255)
white = (255, 255, 255)
red = (0, 0, 255)


def rect_equ(index):
    coord_y = int(index / sides) * margin
    coord_x = (index % sides) * margin
    return coord_x, coord_y, margin, margin

running = True
while running:
    window.fill(white)
    pygame.draw.rect(window, black, (rect_equ(angel)))

    pygame.draw.rect(window, red, (rect_equ(2)))
    # devil barriers
    for barrier in devils:
        pygame.draw.rect(window, red, (barrier[0] - margin / 2, barrier[1] - margin / 2, margin, margin))

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == K_RIGHT:
                angel += 1
            if e.key == K_LEFT:
                angel -= 1
            if e.key == K_UP:
                angel -= sides
            if e.key == K_DOWN:
                angel += sides
        if e.type == pygame.QUIT:
            running = False

    # grid
    for side in range(0, size, margin):
        pygame.draw.lines(window, black, False, ((side, 0), (side, size)))
        pygame.draw.lines(window, black, False, ((0, side), (size, side)))
    pygame.display.update()
