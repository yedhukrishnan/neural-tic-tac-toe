from board import Board
from printer import *

def main():
    print("Hello, World!")
    board = Board()
    print_board(board.get_board())
    while True:
        pos = input()
        print(board.play(int(pos)))
        print(board.get_board())
        print_board(board.get_board())
        

if __name__ == "__main__":
    main()
