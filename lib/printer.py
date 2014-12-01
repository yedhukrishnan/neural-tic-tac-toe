def print_board(board):
    i = 0
    for row in range(0, 3):
        for col in range(0, 3):
            print(board[i], end=" ")
            i += 1
        print("")
