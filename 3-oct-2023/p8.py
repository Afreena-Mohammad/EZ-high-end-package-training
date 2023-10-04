#wap to print Q for 4x4 matrix where q should not be in same row or same column
def is_safe(board, row, col):
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1):
                return True

            board[i][col] = 0

    return False

def solve_n_queens():
    board = [[0 for _ in range(4)] for _ in range(4)]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    return board

def print_board(board):
    for row in board:
        print(' '.join(['Q' if x == 1 else '.' for x in row]))

# Solve and print the board
solution = solve_n_queens()

if solution:
    print_board(solution)
