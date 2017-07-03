from Board import Board
from matplotlib import pyplot as plt

board = Board(60, 9, True)
while True:
    board.players_play()
    winner = board.get_winner()
    if winner is not None:
        print(winner)
        break
# board = Board(60, 9, False)
# ratios = []
# winners = {"angel": 0, "devil": 0}
# winner = None
# for i in range(80000):
#     while winner is None:
#         board.angels_turn()
#         board.devils_turn()
#         winner = board.get_winner()
#     winners[winner] += 1
#     if not i == 0 and i % 100 == 0:
#         print(i)
#         print(board.get_angel().moves)
#         print(winners)
#         ratios.append(winners["angel"] / winners["devil"])
#         winners = {"angel": 0, "devil": 0}
#     board.train_angel()
#     board.reset()
#     winner = None
# plt.scatter([i for i in range(len(ratios))], ratios)
# plt.show()