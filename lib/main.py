from board import Board
from validator import Validator
from printer import *
import time
import random

def main():
    file_name = "games/game" + str(time.time())
    game_file = open(file_name, "w+")
    board = Board()
    print_board(board)
    validator = Validator(board)
    while not validator.game_over():
        possible_positions = [i for i, x in enumerate(board.full_board()) if x == "."]
        if board.next_player() == 'o':
            pos = random.choice(possible_positions)
        else:
            pos = input()
        board.play(int(pos))
        print_board(board)
        print possible_positions
        game_file.write("".join(board.full_board()) + "\n")
    print "Game over!"
    game_file.close()


if __name__ == "__main__":
    main()
