from board import Board
from validator import Validator
from printer import *

def main():
    print("Hello, World!")
    board = Board()
    print_board(board)
    validator = Validator(board)
    while not validator.game_over():
        pos = input()
        board.play(int(pos))
        print_board(board)
    print("Game over!")
    

if __name__ == "__main__":
    main()
