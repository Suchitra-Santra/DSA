def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))


def is_valid(board, row, col, num):
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):

            # Find an empty cell
            if board[row][col] == 0:

                # Try numbers 1-9
                for num in range(1, 10):

                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # Recursively solve
                        if solve_sudoku(board):
                            return True

                        # Backtrack
                        board[row][col] = 0

                return False

    return True


# 0 means empty
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


print("Original Sudoku:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("\nNo solution exists.")