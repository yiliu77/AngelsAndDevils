from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
from devil_training.Board import Board

# board = Board(60, 9, True)
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
    if not i == 0 and i % 100 == 0 and not winners["angel"] == 0:
        print(i)
        print(board.get_devil().get_blocks())
        print(winners)
        ratios.append(winners["devil"] / winners["angel"])
        winners = {"angel": 0, "devil": 0}
    board.train_devil()
    board.reset()
    winner = None
plt.scatter([i for i in range(len(ratios))],ratios)
slope, intercept, r_value, p_value, std_err = stats.linregress([i for i in range(len(ratios))],ratios)
print(slope)
plt.show()

np.savetxt('Files/devil_who.csv', board.get_devil().get_who(), delimiter=',')
np.savetxt('Files/devil_wih.csv', board.get_devil().get_wih(), delimiter=',')

# board.init_draw()
# board.display_board()
# board.angels_turn()
# while True:
#     board.display_board()


