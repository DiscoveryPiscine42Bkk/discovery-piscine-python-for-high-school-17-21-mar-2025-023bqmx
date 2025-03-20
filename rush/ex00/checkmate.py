def valid_board(board):
    # Check if the board has any invalid letters.
    valid_pieces = {'P', 'R', 'Q', 'B', 'K', '[' , ']' , '.'} 

    for row in board:
        for piece in row:
           
            if piece not in valid_pieces:
                print("Error")
                return False
    
    return True

def find_k(board):
    # """King position"""
    counter = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 'K':
                counter += 1               
                return x, y
            
    return None

def under_attack(board, king_x, king_y):
    # """Check if king has been attacked"""
    size = len(board)

    # check pawn
    if king_x > 0:
     if king_x > 0 and board[king_x + 1][king_y + 1] == 'P': #left diagonal
            return True
    if king_y < size - 1 and board[king_x + 1][king_y - 1] == 'P': #right diagonal
            return True

    # Check rook & queen in straight direction
    for d_x, d_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = king_x, king_y
        while 0 <= x < size and 0 <= y < size:
            x += d_x
            y += d_y
            if 0 <= x < size and 0 <= y < size:
                if board[x][y] == 'R' or board[x][y] == 'Q':
                    return True
                if board[x][y] != '.':  # stop when it found something
                    break

    # Check rook & queen in diagonal direction
    for d_x, d_y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        x, y = king_x, king_y
        while 0 <= x < size and 0 <= y < size:
            x += d_x
            y += d_y
            if 0 <= x < size and 0 <= y < size:
                if board[x][y] == 'B' or board[x][y] == 'Q':
                    return True
                if board[x][y] != '.':  # stop when it found something
                    break

    return False

def checkmate(board):
    # """Check if king has been attacked"""
    
    
    for i in board:
        print(i)
        
        king_count = sum(row.count('K') for row in board)
    if king_count > 1:
            print("Error")
            return False
    
    if not valid_board(board):
        return  # Stop when it have wrong word

    king_position = find_k(board)
    if not king_position:
        print("Fail")  # Not have king
        return
    
    king_x, king_y = king_position
    if under_attack(board, king_x, king_y):
        print("Success")  # King in check
    else:
        print("Fail")  # King is safe 