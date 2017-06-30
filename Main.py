from Board import Board

board = Board(60, 9)
while True:
    board.run()
    winner = board.get_winner()
    if winner is not None:
        print(winner)
        break
# for i in range(100):
