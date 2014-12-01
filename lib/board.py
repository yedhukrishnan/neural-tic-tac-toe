class Board:
    def __init__(self):
        self.board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    
    def play(self, position):
        try:
            piece = self.find_next_player_piece()
            self.board[position] = piece
            return True
        except IndexError:
            return False
    
    def find_next_player_piece(self):
        o = self.board.count('o')
        x = self.board.count('x')
        if x == o:
            return 'x'
        return 'o'

    def piece(self, position):
        return self.board[position]
