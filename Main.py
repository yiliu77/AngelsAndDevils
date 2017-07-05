from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
from Board import Board

# board = Board(60, 9, False)
# while True:
#     board.players_play()
#     winner = board.get_winner()
#     if winner is not None:
#         print(winner)
#         break
board = Board(60, 9, False)
ratios = []
winners = {"angel": 0, "devil": 0}
winner = None
for i in range(800000):
    while winner is None:
        board.devils_turn()
        board.angels_turn()
        winner = board.get_winner()
    winners[winner] += 1
    if i % 100 == 0 and not winners["angel"] == 0:
        print(i)
        print(board.get_devil().get_blocks())
        print(board.get_angel().moves)
        print(winners)
        print(board.get_reason())
        ratios.append(winners["devil"] / winners["angel"])
        winners = {"angel": 0, "devil": 0}

    board.train_angel()
    board.train_devil()
    board.reset()
    winner = None
plt.scatter([i for i in range(len(ratios))], ratios)
plt.show()

# board = Board(60, 9, False, True)
# np.savetxt('Files/angel_who.csv', board.get_angel().get_who(), delimiter=',')
# np.savetxt('Files/angel_wih.csv', board.get_angel().get_wih(), delimiter=',')
#
# board.init_draw()
# board.display_board()
# board.angels_turn()
# while True:
#     board.display_board()
#     pressed = board.button_pressed()
#     if pressed is True:
#         board.angels_turn()
