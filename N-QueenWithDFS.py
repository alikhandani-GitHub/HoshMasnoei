def Tadakhol(board, row, col):
    for i in range(col):
        if board[i] == row or board[i] == row - col + i or board[i] == row + col - i:
            return False
    return True

def HaleNqueen(n):
    def backTrack(col):
        if col == n:
            return True
        
        for row in range(n):
            if Tadakhol(board, row, col):
                board[col] = row
                if backTrack(col + 1):
                    return True
        return False

    board = [-1] * n
    if backTrack(0):
        return board
    else:
        return None

n = int(input())
result = HaleNqueen(n)
print(result) 