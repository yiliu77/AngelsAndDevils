from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
from Board import Board

print("1: Player vs Player\n2: Player vs Angel \n3: Player vs Devil\n")
selection = input("Select Option: ")

if selection == "1":
    board = Board(60, 9)
    board.init_draw()
    while True:
        board.display_board()
        done = board.players_play()
        winner = board.get_winner()
        if winner is not None or done:
            print("===================")
            print("Winner: " + winner)
            print("Reason: " + board.get_reason())
            print("===================")
            break

if selection == "2":
    board = Board(60, 9, True, False)
    board.init_draw()
    board.angels_turn()
    while True:
        board.display_board()
        pressed = board.god_as_devil()
        winner = board.get_winner()
        if pressed is True:
            board.angels_turn()
        if winner is not None:
            print("===================")
            print("Winner: " + winner)
            print("Reason: " + board.get_reason())
            print("===================")
            break

if selection == "3":
    board = Board(60, 9, False, True)
    board.init_draw()
    while True:
        board.display_board()
        move = board.god_as_angel()
        winner = board.get_winner()
        if move is True:
            board.devils_turn()
        if winner is not None:
            print("===================")
            print("Winner: " + winner)
            print("Reason: " + board.get_reason())
            print("===================")
            break
#training
# board = Board(60, 9, False)
# ratios = []
# winners = {"angel": 0, "devil": 0}
# winner = None
# for i in range(800000):
#     while winner is None:
#         board.devils_turn()
#         board.angels_turn()
#         winner = board.get_winner()
#     winners[winner] += 1
#     if i % 100 == 0 and not winners["angel"] == 0:
#         print(i)
#         print(board.get_devil().get_blocks())
#         print(board.get_angel().moves)
#         print(winners)
#         print(board.get_reason())
#         ratios.append(winners["devil"] / winners["angel"])
#         winners = {"angel": 0, "devil": 0}
#
#     board.train_angel()
#     board.train_devil()
#     board.reset()
#     winner = None
# plt.scatter([i for i in range(len(ratios))], ratios)
# plt.show()


# np.savetxt('Files/angel_who.csv', board.get_angel().get_who(), delimiter=',')
# np.savetxt('Files/angel_wih.csv', board.get_angel().get_wih(), delimiter=',')