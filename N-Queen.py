def is_valid(board, row, col):
    # Check if there is another minister in the same column
    for i in range(row):
        if board[i] == col:
            return False
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def place_ministers(board, row, n):
    if row == n:
        return [board[:]]

    solutions = []
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solutions += place_ministers(board, row + 1, n)
    return solutions

def main():
    n = 4
    board = [-1] * n
    solutions = place_ministers(board, 0, n)
    for solution in solutions:
        print(solution)

if __name__ == '__main__':
    main()