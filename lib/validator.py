
class Validator:
    def __init__(self, board):
        self.board = board
        self.win_board_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        self.winner = ''

    def game_over(self):
        for trio in self.win_board_combinations:
            if (self.board.piece(trio[0]) == self.board.piece(trio[1]) == self.board.piece(trio[2])) and self.board.piece(trio[0]) != '.': 
                self.winner = self.board.piece(trio[0])
                return True
        return self.board.full_board().count('.') == 0

    def winner(self):
        return self.winner
