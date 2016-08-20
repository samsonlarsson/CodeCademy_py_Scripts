board = []

for loop in range(0, 5):
    chess = ["O"] * 5
    board.append(chess)

def print_board(board):
    for row in board:
        print " ".join(row)
        # print row

print print_board(board)