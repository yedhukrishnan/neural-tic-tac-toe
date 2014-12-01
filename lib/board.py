class Board:
    def __init__(self):
        self.board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    
    def play(self, position):
        try:
            piece = self.find_piece()
            self.board[position] = piece
            return True
        except IndexError:
            return False
    
    def get_board(self):
        return self.board

    def find_piece(self):
        o = self.board.count('o')
        x = self.board.count('x')
        if x == o:
            return 'x'
        return 'o'
