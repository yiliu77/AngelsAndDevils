from Board import Board
import numpy as np

board = Board(60, 9, False)
winner = None
# while True:
#     board.players_play()
#     winner = board.get_winner()
#     if winner is not None:
#         print(winner)
#         break
# print(board.get_board_positions())
winners = {"angel": 0, "devil": 0}
while winner is None:
    turn = board.angels_turn()
    devil_turn = board.devils_turn()
    winner = board.get_winner()
    if winner is not None:
        winners[winner] += 1
board.train_angel(True if winner is "angel" else False)

print(board.get_blocks())
print(winners)
