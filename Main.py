from Board import Board
import numpy as np

board = Board(60, 9, True)
while True:
    board.players_play()
    winner = board.get_winner()
    if winner is not None:
        print(winner)
        break
# winners = {"angel": 0, "devil": 0}
# for i in range(2000):
#     while winner is None:
#         turn = board.angels_turn()
#         devil_turn = board.devils_turn()
#         winner = board.get_winner()
#         if winner is not None:
#             winners[winner] += 1
#             break
#     if i % 100 == 0:
#         print(i)
#         print(board.get_angel().get_moves())
#     board.train_angel(True if winner is "angel" else False)
#     board.reset()
#     winner = None
# print(winners)
