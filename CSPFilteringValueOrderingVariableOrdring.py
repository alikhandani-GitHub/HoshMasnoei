import itertools
import gzip

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def place_queens(n):
    board = [-1] * n
    solutions = []
    stack = [(0, board)]
    
    while stack:
        row, board = stack.pop()
        
        if row == n:
            solutions.append(board[:])
            continue
        
        for col in range(n):
            if is_valid(board, row, col):
                new_board = board[:]
                new_board[row] = col
                stack.append((row + 1, new_board))
    
    return solutions

def save_solutions(solutions, file_path):
    with gzip.open(file_path, 'wt') as file:
        for solution in solutions:
            for queen in solution:
                file.write(f'{queen} ')
            file.write('\n')

def main():
    n = 8
    solutions = place_queens(n)
    save_solutions(solutions, 'n_queen_solutions.gz')

if __name__ == "__main__":
    main()
