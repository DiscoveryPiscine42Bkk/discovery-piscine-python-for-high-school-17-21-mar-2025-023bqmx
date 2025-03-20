def validate_board(board):
    """ตรวจสอบว่ากระดานมีตัวอักษรที่ไม่ถูกต้องหรือไม่"""
    valid_pieces = {'P', 'R', 'Q', 'B', 'K', '.'}  # ตัวหมากรุกที่ถูกต้อง
    for row in board:
        for piece in row:
            if piece not in valid_pieces:
                print("Error")
                return False
    return True

def find_king(board):
    """ค้นหาตำแหน่งของ King (K)"""
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                return r, c
    return None

def is_under_attack(board, king_r, king_c):
    """ตรวจสอบว่า King ถูกโจมตีหรือไม่"""
    size = len(board)

    # ตรวจสอบ Pawn (P) - โจมตีเฉพาะแนวทแยงด้านหน้า #fix this
    if king_r > 0:
     if king_c > 0 and board[king_r + 1][king_c + 1] == 'P':
            return True
    if king_c < size - 1 and board[king_r + 1][king_c - 1] == 'P':
            return True

    # ตรวจสอบ Rook (R) และ Queen (Q) - แนวตรง
    for d_r, d_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r, c = king_r, king_c
        while 0 <= r < size and 0 <= c < size:
            r += d_r
            c += d_c
            if 0 <= r < size and 0 <= c < size:
                if board[r][c] == 'R' or board[r][c] == 'Q':
                    return True
                if board[r][c] != '.':  # หยุดถ้ามีสิ่งกีดขวาง
                    break

    # ตรวจสอบ Bishop (B) และ Queen (Q) - แนวทแยง
    for d_r, d_c in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        r, c = king_r, king_c
        while 0 <= r < size and 0 <= c < size:
            r += d_r
            c += d_c
            if 0 <= r < size and 0 <= c < size:
                if board[r][c] == 'B' or board[r][c] == 'Q':
                    return True
                if board[r][c] != '.':  # หยุดถ้ามีสิ่งกีดขวาง
                    break

    return False

def checkmate(board):
    """ตรวจสอบว่า King ถูกโจมตีหรือไม่"""
    if not validate_board(board):
        return  # หยุดทำงานถ้ากระดานมีตัวอักษรผิด

    king_position = find_king(board)
    if not king_position:
        print("Fail")  # ไม่มี King ในกระดาน
        return
    
    king_r, king_c = king_position
    if is_under_attack(board, king_r, king_c):
        print("Success")  # King อยู่ใน "Check"
    else:
        print("Fail")  # King ปลอดภัย