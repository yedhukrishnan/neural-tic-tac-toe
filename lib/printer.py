def print_board(board):
    position = 0
    for row in range(0, 3):
        for col in range(0, 3):
            print board.piece(position),
            position += 1
        print ""
