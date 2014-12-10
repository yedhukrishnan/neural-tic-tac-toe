from board import Board
from validator import Validator
from printer import *
import time

def main():
    print("Hello, World!")
    file_name = "games/game" + str(time.time())
    game_file = open(file_name, "w+")
    board = Board()
    print_board(board)
    validator = Validator(board)
    while not validator.game_over():
        pos = input()
        board.play(int(pos))
        print_board(board)
        indices = [i for i, x in enumerate(board.full_board()) if x == "."]
        print(indices)
        game_file.write("".join(board.full_board()) + "\n")
    print("Game over!")
    game_file.close()
    

if __name__ == "__main__":
    main()
