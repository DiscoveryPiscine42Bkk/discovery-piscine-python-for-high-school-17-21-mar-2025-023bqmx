def validate_board(board):
    # Check if the board has any invalid letters.
    valid_pieces = {'P', 'R', 'Q', 'B', 'K', '.' , '|'} 
    for row in board:
        for piece in row:
            if piece not in valid_pieces:
                print("Error")
                return False
    return True

def find_king(board):
    """King position"""
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                return r, c
    return None

def is_under_attack(board, king_r, king_c):
    """Check if king has been attacked"""
    size = len(board)

    # check pawn
    if king_r > 0:
     if king_c > 0 and board[king_r + 1][king_c + 1] == 'P': #left diagonal
            return True
    if king_c < size - 1 and board[king_r + 1][king_c - 1] == 'P': #right diagonal
            return True

    # Check rook and queen in straight direction
    for d_r, d_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r, c = king_r, king_c
        while 0 <= r < size and 0 <= c < size:
            r += d_r
            c += d_c
            if 0 <= r < size and 0 <= c < size:
                if board[r][c] == 'R' or board[r][c] == 'Q':
                    return True
                if board[r][c] != '.':  # stop when it found something
                    break

    # Check rook and queen in diagonal direction
    for d_r, d_c in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        r, c = king_r, king_c
        while 0 <= r < size and 0 <= c < size:
            r += d_r
            c += d_c
            if 0 <= r < size and 0 <= c < size:
                if board[r][c] == 'B' or board[r][c] == 'Q':
                    return True
                if board[r][c] != '.':  # stop when it found something
                    break

    return False

def checkmate(board):
    """Check if king has been attacked"""
    
    for i in board:
        print(i)
    
    if not validate_board(board):
        return  # Stop when it have wrong word

    king_position = find_king(board)
    if not king_position:
        print("Fail")  # Not have king
        return
    
    king_r, king_c = king_position
    if is_under_attack(board, king_r, king_c):
        print("Success")  # King in check
    else:
        print("Fail")  # King is safe  